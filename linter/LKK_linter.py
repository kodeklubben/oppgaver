import re
import glob
import os, sys
import subprocess
import filecmp
import pickle
import time
from pathlib import Path

# Adds a subdirectory to path, so we can load the sub modules
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/linter_lib")

# This updates keys, tags and other dict files so that linter_defaults is updated
import linter_update_objects
from linter_defaults import *

import linter_md
import linter_auto_md
import linter_yml
import linter_auto_yml

FILE_ENDINGS = ['md', LESSON_YML]
DEFAULT_TYPES = ['md', 'yml']
DEFAULT_OPTIONS = ['a', 'l']
DEFAULT_ARGS = DEFAULT_TYPES + DEFAULT_OPTIONS

arg_filetypes = ['md', 'yml']
ARG_OPTIONS = ['a', 'l', 'o']
arg_files_or_options = arg_filetypes + ARG_OPTIONS + ['r']

def print_help():
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    toprule = '‾'*int(columns)
    midrule = '-'*int(columns)
    bottomrule = '_'*int(columns)

    print("""    usage: python LKK_linter.py [options] ... [filetype] ... path_2_file / path_2_folder

    Most common usage:

    python LKK_linter.py ../SRC/language/path/file.md      |OR|     python LKK_linter.py -r ../SRC/language/
   \                                                 /            \                                          /
            Lints and autoformats the files                          autoformats every .md and lesson.yml
            ../SRC/language/path_2_file.md,                          file in the /language/ folder recursively
            ../SRC/language/path/lesson.yml

    NOTE: If no folder is provided when working recursively it will default to ../SRC/

    Following options are recognized
{}
    -a    :   only autoformats (does not show linting errors)
    -A    :   same as -a but recursively
    -l    :   only shows linting errors (does not autoformat)
    -L    :   samme as -l but recursively
    -r    :   recursively search through SRC
    -md   :   only look at the .md files
    -yml  :   only look at the lesson.yml files
{}
    The commands enabled by default are: -md, -yml, -a and -l.
    """.format(midrule, midrule))

def get_args():
    ''' Get all the legal options for LKK_linter.py from sys.argv.
    (sys.arg are every option given to python from the command line)
    Example:

    sys.argv = ['LKK-linter.py', '-md', '-rLA', '-o', '../SRC/microbit']

    The comments in the following code shows what happens to the list above
    '''

    arglist = [arg[1:] for arg in sys.argv if arg.startswith('-')]
    # arglist = ['md', 'rLA', 'O']

    arguments = set() # Make sure every argument only appears once
    # The following code splits up every option and adds the one from
    # arg_files_or_options
    for arg in arglist:
        if arg in arg_files_or_options:
            arguments.add(arg)
            # arguments = ('md')
        elif arg.lower() in arg_files_or_options:
            # Capital letters O, A, L means letter + recursive
            arguments.update([arg.lower(), 'r'])
            # arguments = ('md', 'o', 'r')
        else:
            # -option can contain several options e.g. -ol.
            for letter in arg:
                # This iterates through the letters of 'rLA'
                # as it is not a valid option by itself
                if letter in ARG_OPTIONS:
                    arguments.add(letter)
                elif letter.lower() in ARG_OPTIONS:
                    arguments.update([letter.lower(), 'r'])
                    # This would add 'l' and 'r' to arguments, however 'r' already exists
                    # arguments = ('md', 'o', 'r', 'l', 'a')

    if not arguments:
        return DEFAULT_ARGS

    args = list(arguments)
    # args = ['md', 'o', 'r', 'l', 'a']
    if not any(a in args for a in DEFAULT_TYPES):
        # Use the default types if no types is found in args
        # For an example if only -r,-l,-a,-o is used include -md, and -yml
        args.extend(DEFAULT_TYPES)
    if not any(a in args for a in ARG_OPTIONS):
        # Use the default options if no options is found in args
        # For an example if only -md or -yml is used include -a,-l
        args.extend(DEFAULT_OPTIONS)
    return args


def yml_path(md_path):
    return Path(re.sub(r'\w+\.md', LESSON_YML, md_path))

# If a file starts with "indexed: false" skip it
def is_indexed(filename):
    with open(filename, 'r') as f:
        first_line = f.readline().replace(" ", "").lower().strip()
        return first_line != "indexed:false"

def is_oppgave(md_path):
    # Every oppgave has a lesson.yml in the same folder
    return yml_path(md_path).is_file()


def get_md_and_yml(filename, markdown, oppgaver, yml, recursively, path):
    ''' Creates the list of files to lint / autoformat.

    If the recursive option is NOT set, this code simply wraps the filename in a list.
    The code also finds every lesson.yml that belongs to the .md file if waranted.
    '''

    files_md = []
    files_yml = []
    if recursively:
        if markdown or oppgaver:
            files_md = glob.glob(str(path) + '/**/*.md', recursive=True)
            if oppgaver or yml:
                opg_md, opg_yml = [], []
                for md_filename in files_md:
                    yml_filepath = yml_path(md_filename)
                    if yml_filepath.is_file():
                        opg_md.append(md_filename)
                        opg_yml.append(yml_filepath)
            # If 'oppgaver = True' replace every .md file with
            # only those who have an accompanying 'lesson.yml' file
            if oppgaver: files_md = opg_md
            if yml: files_yml = opg_yml
        elif yml:
            files_yml = (glob.glob(str(path) + '/**/{}'.format(LESSON_YML), recursive=True))
    else:
        file_ending = get_file_ending(filename)
        if file_ending == FILE_ENDINGS[0]: # .md
            yml_filepath = yml_path(filename)
            yml_exists = yml_filepath.is_file()
            if markdown and not oppgaver:
                files_md = [filename]
                if yml and yml_exists:
                    files_yml = [str(yml_filepath)]
            elif oppgaver and yml_exists:
                # If 'oppgaver = True' Only add filename if yml exists
                files_md = [filename]
                files_yml = [str(yml_filepath)]
        elif file_ending == FILE_ENDINGS[1] and yml: # lesson.yml
            files_yml = [filename]
    return (files_md, files_yml)


def get_file_ending(filename):
    for endings in FILE_ENDINGS:
        if filename.endswith("."+endings):
            return endings

def main():
    ''' Comments and formats markdown files and lesson.yml files according
    to common practices in programming and in the rules defined in LKK's styleguide

    see https://github.com/kodeklubben/oppgaver/wiki/Stilguide-for-kode-og-tekst
    for the specific requirements.

    The program is split into four parts:

        md_linting, md_auto_lint, yml_auto_lint, yml_lint,

    The auto_lint files formats files, while the linter checks for errors. This
    order is VERY important to keep. Files are sometimes moved from md -> yml.
    See the specific files for more information on how each part works. For
    information about how to use the program run 'LKK_linter.py' without any options.
    '''

    linter_update_objects.update_keys_and_tags_if_needed()
    linter_update_objects.update_file_info_if_needed()

    if len(sys.argv) == 1:
        # If no options is given show the help menu and return
        print_help()
        return

    arguments = get_args()
    filename = sys.argv[-1]
    file_ending = get_file_ending(filename)

    src = PATH_2_SRC
    if not 'r' in arguments and not Path(filename).is_file():
        raise Warning("You need to provide a filename, unless you are working recursively")
    elif 'r' in arguments and Path(filename).is_dir():
        src = Path(filename)

    # Default argument settings:
    MARKDOWN = False
    OPPGAVER = False
    YML = True
    RECURSIVELY = False
    AUTO = False
    LINTING = False

    # Gives the short hand options more descriptive names
    for argument in arguments:
        if argument == 'r':
            RECURSIVELY = True
        elif argument == 'md':
            MARKDOWN = True
        elif argument == 'o':
            OPPGAVER = True
        elif argument == 'yml':
            YML = True
        elif argument == 'a':
            AUTO = True
        elif argument == 'l':
            LINTING = True

    files_md, files_yml = get_md_and_yml(filename, MARKDOWN, OPPGAVER, YML, RECURSIVELY, src)

    if MARKDOWN and AUTO and files_md:
        linter_auto_md.main(files_md)

    if MARKDOWN and LINTING and files_md:
        linter_md.main(files_md)

    if YML and AUTO and files_yml:
        linter_auto_yml.main(files_yml)

    if YML and LINTING and files_yml:
        linter_yml.main(files_yml)


if __name__ == "__main__":

    main()
