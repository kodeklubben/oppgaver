import re
import filecmp
import sys
import pickle
import os

from pathlib import Path


#=============================================================
#             GENERAL
#=============================================================

MAX_LEVEL = 4
MIN_LEVEL = 1
LEVEL_STR = '[{}-{}]'.format(MIN_LEVEL, MAX_LEVEL)

LINTER_LIB_FOLDER = 'linter_lib'
# If we are in the ./linter_lib folder, this gets us the path
# to the parent folder. This makes sure all our absolute urls work
PATH = Path.cwd() # current path
if PATH.parts[-2] == 'linter': #Checks if parent folder name is linter
    PATH = PATH.parent

PATH_2_LIB = PATH.pathjoin(LINTER_LIB_FOLDER)


# method independent of operating system of appending filepaths
def create_new_path(list_of_filenames):
    return Path(os.path.join(os.path.sep,PATH,*list_of_filenames))

PATH_2_FILTERTAGS = create_new_path(["..","filtertags","keys.yml"])
PATH_2_SRC = create_new_path(['..','src'])
PATH_2_OBJ = PATH_2_LIB.joinpath('')

# When this file is loaded into LKK_linter.py the file
# PATH_2_KEYS_AND_TAGS
# might not exist. As LKK_linter creates this file,
# for the submodules this file will always exist.
PATH_2_KEYS_AND_TAGS = PATH_2_OBJ.joinpath('keys_and_tags.pkl')
if PATH_2_KEYS_AND_TAGS.is_file():
    SETTINGS = pickle.load(open(PATH_2_KEYS_AND_TAGS, "rb"))
    TAGS_ = SETTINGS['tags_lst_']
    KEYS = SETTINGS['keys']
    KEYS_REVERSE_ = SETTINGS['keys_reverse_']
    TAGS_REVERSE_ = SETTINGS['tags_lst_reverse_']

PATH_2_FILE_INFO = PATH_2_OBJ.joinpath('src_files_info.pkl')
if PATH_2_FILE_INFO.is_file():
    FILE_INFO = pickle.load(PATH_2_KEYS_AND_TAGS, "rb")


#=============================================================
#             AUTO MD SETTINGS
#=============================================================

CLASSES = "intro|activity|check|flag|challenge|tip|save|protip|try|sjekkliste"
CLASSES_LST = CLASSES.split('|')
YAML_TITLES = ["title", "author", "translator", "language", "external", "level"]
YAML_TITLES_REVERSE_ = dict(
    title=0,
    author=1,
    translator=2,
    language=3,
    external=4,
    level=5,
)

MOVE_TITLES = ["license"]
# MOVE_TITLES = ["license", "level"]
#=============================================================

#=============================================================
#             AUTO YML SETTINGS
#=============================================================
YML_INDENT = 2
YML_INDENT_STR = ' ' * YML_INDENT

KEYS_YML = ['level', 'license']
KEYS_YML_REVERSE_ = dict(
    level=0,
    license=1,
    tag=2,
)
ALLOW_EXTRA_HEADERS = True
MOVE_LEVEL_2_LESSON_YML = False
#=============================================================

#=============================================================
#             AUTO MD SETTINGS
#=============================================================
TAB_INDENT = 2
TAB_INDENT_STR = ' ' * TAB_INDENT

#=============================================================



def create_temp_path(filename, newname='_temp'):
    path_1 = os.path.splitext(filename)[0]
    path_2 = os.path.splitext(filename)[1]
    return path_1 + newname + path_2


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j +
                                      1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def save_FILE_INFO(data):
    output = open(PATH_2_FILE_INFO, 'wb')
    pickle.dump(data, output)
    output.close()
