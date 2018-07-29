import re
import glob
import os, sys
import subprocess
import filecmp
import pickle
import time
from pathlib import Path

from termcolor import colored

def create_new_path(list_of_filenames):
    return Path(os.path.join(os.path.sep,*list_of_filenames))

PATH_2_FILTERTAGS = create_new_path(["..","filtertags","keys.yml"])
PATH_2_SRC = create_new_path(['..','src'])
PATH_2_LINTER = create_new_path(['linter'])
PATH_2_LINTER_DEFAULTS = PATH_2_LINTER.joinpath('linter_defaults.py')
PATH_2_OBJ = PATH_2_LINTER.joinpath('')
PATH_2_KEYS_AND_TAGS = PATH_2_OBJ.joinpath('keys_and_tags.pkl')
PATH_2_TIMINGS = PATH_2_OBJ.joinpath('timings.pkl')


FILE_ENDINGS = ['md', 'lesson.yml']
DEFAULT_TYPES = ['md', 'yml']
DEFAULT_OPTIONS = ['a', 'l']
DEFAULT_ARGS = DEFAULT_TYPES + DEFAULT_OPTIONS

# Adds a subdirectory to path, so we can load the modules
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/linter")
import linter_md
import linter_auto_md
import linter_yml
import linter_auto_yml
from linter_defaults import *



def print_help():
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    toprule = '‾'*int(columns)
    midrule = '-'*int(columns)
    bottomrule = '_'*int(columns)
    print("""
    Help for using the LKK linter command! Usage:

    LKK_linter.py -options -path_2_filename

    By default the the program lints and autoformats, if you want to recursively lint/autoformat
    all files in SRC, no filename option is neccecary. Following options are recognized
{}
  | -a  | only autoformats (does not show linting errors)
  | -A  | same as -a but recursively
  | -f  | ignores when files were last linted / autoformated
  | -F  | same as -f but recursively
  | -l  | only shows linting errors (does not autoformat)
  | -L  | samme as -l but recursively
  | -r  | recursively search through SRC
  | -h  | brings up this help menu
  | -md | only look at the .md files
  | -yml| only look at the lesson.yml files

{}
The commands enabled by default are: -md, -yml, -a and -l.
    """.format(bottomrule, midrule, toprule))


def is_file(argument):
    for file_ending in FILE_ENDINGS:
        if argument.endswith("."+file_ending):
            return True, file_ending
    return False, ''

arg_filetypes = ['md', 'yml', 'level']
ARG_OPTIONS = ['a', 'f', 'l', 'o', 'r']
arg_files_or_options = arg_filetypes + ARG_OPTIONS

def get_args():

    # create_dict_objects()
    if len(sys.argv) == 1:
        print_help()
    else:
        arglist = sys.argv[1:-1]
        last_element = sys.argv[-1]
        is_filepath, _ = is_file(last_element)
        not_md_or_yml = True
        not_options = True
        if not is_filepath:
            arglist.append(last_element)
        arguments = set()
        for args in arglist:
            if args[0] != '-':
                continue
            arg = args[1:]
            if arg in arg_files_or_options:
                arguments.add(arg)
            elif arg.lower() in arg_files_or_options:
                arguments.update([arg.lower(), 'r'])
            else:
                for letter in arg:
                    if letter in ARG_OPTIONS:
                        arguments.add(letter)
                    elif letter.lower() in ARG_OPTIONS:
                        arguments.update([letter.lower(), 'r'])
        if not arguments:
            return DEFAULT_ARGS
        args = list(arguments)
        if not any(a in args for a in DEFAULT_TYPES):
            args.extend(DEFAULT_TYPES)
        if not any(a in args for a in ARG_OPTIONS):
            args.extend(DEFAULT_OPTIONS)
        return args
    return DEFAULT_ARGS


def yml_path(md_path):
    return Path(re.sub(r'\w+\.md', 'lesson.yml', md_path))

# If a file starts with "indexed: false" skip it
def is_indexed(filename):
    with open(filename, 'r') as f:
        first_line = f.readline().replace(" ", "").lower().strip()
        return first_line != "indexed:false"

def is_oppgave(md_path):
    # Every oppgave has a lesson.yml in the same folder
    return yml_path(md_path).is_file()


def get_md_and_yml(filename, markdown, oppgaver, yml, recursively, path=PATH_2_SRC):
    _, file_ending = is_file(filename)
    files_md = []
    files_yml = []
    if recursively:
        if markdown or oppgaver:
            files_md = glob.glob(path + '/**/*.md', recursive=True)
            if oppgaver or yml:
                opg_md, opg_yml = [], []
                for md_filename in files_md:
                    yml_filepath = yml_path(md_filename)
                    if yml_filepath.is_file():
                        opg_md.append(md_filename)
                        opg_yml.append(yml_filepath)
            if oppgaver: files_md = opg_md
            if yml: files_yml = opg_yml
        elif yml:
            files_yml = (glob.glob(path + '/**/lesson.yml', recursive=True))
    else:
        if file_ending == FILE_ENDINGS[0]: # .md
            yml_filepath = yml_path(filename)
            yml_exists = yml_filepath.is_file()
            if markdown and not oppgaver:
                files_md = [filename]
                if yml and yml_exists:
                    files_yml = [yml_filepath]
            elif oppgaver and yml_exists:
                files_md = [filename]
                files_yml = [yml_filepath]
        elif file_ending == FILE_ENDINGS[1] and yml: # lesson.yml
            files_yml = [filename]
    return (files_md, files_yml)


def main():
    # keys_and_tags_ = get_dict_obj()
    arguments = get_args()
    filename = sys.argv[-1]
    is_filepath, file_ending = is_file(filename)
    if not 'r' in arguments and not is_filepath:
        raise Warning("You need to provide a filename, unless you are working recursively")

    # Default argument settings:
    MARKDOWN = False
    OPPGAVER = False
    YML = True
    RECURSIVELY = False
    AUTO = False
    LINTING = False
    FORCE = False
    MOVE_LEVEL_FROM_MD_2_YML = False
    MOVE_LICENSE_FROM_MD_2_YML = False

    file_endings_ = dict()
    for argument in get_args():
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
        elif argument == 'f':
            FORCE = True
        elif argument == 'l':
            LINTING = True


    files_md, files_yml = get_md_and_yml(filename, MARKDOWN, OPPGAVER, YML, RECURSIVELY)

    # if YML and AUTO:
    #     linter_auto_yml.main(files_yml, keys_and_tags_, OPPGAVER)
    if YML and LINTING:
        linter_yml.main(files_yml, keys_and_tags_)
    # if MARKDOWN and AUTO:
    #     linter_auto_md.main(files_md, keys_and_tags_, OPPGAVER)
    # if MARKDOWN and LINTING:
    #     linter_md.main(files_md, keys_and_tags_, OPPGAVER)

    # for filename in files_yml:
    #     print(filename)
    # for filename in files_md:
    #     print(filename)


if __name__ == "__main__":

    main()
