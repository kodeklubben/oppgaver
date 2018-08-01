import re
import filecmp
import sys
import pickle
import os
import subprocess

from termcolor import colored
import colorama

from pathlib import Path

from collections import defaultdict

#=============================================================
#             GENERAL
#=============================================================

MAX_LEVEL = 4
MIN_LEVEL = 1
LEVEL_STR = '[{}-{}]'.format(MIN_LEVEL, MAX_LEVEL)

LESSON_YML = 'lesson.yml'

LINTER_LIB_FOLDER = 'linter_lib'
# If we are in the ./linter_lib folder, this gets us the path
# to the parent folder. This makes sure all our absolute urls work
PATH = Path.cwd()  # current path
if PATH.parts[-2] == 'linter_2':  #Checks if parent folder name is linter
    PATH = PATH.parent

PATH_2_LIB = PATH.joinpath(LINTER_LIB_FOLDER)


# method independent of operating system of appending filepaths
def create_new_path(list_of_filenames):
    return Path(os.path.join(os.path.sep, PATH, *list_of_filenames))


PATH_2_FILTERTAGS = create_new_path(["..", "filtertags", "keys.yml"])
PATH_2_SRC = create_new_path(['..', 'src'])
PATH_2_OBJ = PATH_2_LIB.joinpath(
    '')  #Change this if you want a subfolder for the pickle objects

PATH_2_KEYS_AND_TAGS = PATH_2_OBJ.joinpath('keys_and_tags.pkl')
if PATH_2_KEYS_AND_TAGS.is_file():
    SETTINGS_ = pickle.load(open(PATH_2_KEYS_AND_TAGS, "rb"))
    TAGS_ = SETTINGS_['tags_lst_']
    TAGS_STR_ = SETTINGS_['tags_str_']
    KEYS = SETTINGS_['keys_lst']
    KEYS_REVERSE_ = SETTINGS_['keys_reverse_']
    TAGS_REVERSE_ = SETTINGS_['tags_reverse_']
    LANGUAGE_LIST = SETTINGS_['tags_lst_']['language']

PATH_2_FILE_INFO = PATH_2_OBJ.joinpath('src_files_info.pkl')
if PATH_2_FILE_INFO.is_file():
    FILE_INFO = pickle.load(open(PATH_2_FILE_INFO, "rb"))

# Color settings
ERROR_CLR = 'red'
CORRECT_CLR = 'green'
MAIN_1_CLR = '' # Use the terminal default color
MAIN_2_CLR = 'yellow'

#=============================================================
#             AUTO MD SETTINGS
#=============================================================

CLASSES = "intro|activity|check|flag|challenge|tip|save|protip|try|sjekkliste"
CLASSES_LIST = CLASSES.split('|')

YAML_TITLES = [
    "title", "author", "translator", "language", "external", "level"
]
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
YML_INDENT = 2  #Changes the indent in lesson.yml files
YML_INDENT_STR = ' ' * YML_INDENT

KEYS_YML = ['level', 'license']  #Which titles are recognized in lesson.yml
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
    ''' The levenshtein distance is a method of giving meaning
    to the distance between two strings. In other words this calculates
    how different two strings are. In short it has three 'moves'

        1. Switch two letters, 2. Add a new leter, 3. remove a letter

    Then it calculuates the least number of moves neccecary to get from s1 to s2.
    The lower the levenshtein distance is the more similar two strings are.
    '''

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

# See levenshtein_lst for detailed explenation of these two constants. 
LEVENSHTEIN_AUTO_MAX = 3  # less than (so 3 would be 0, 1, 2)
LEVENSHTEIN_ASK_MAX = 7  # less than (so 10 would be 3, 4, 5, 6)


def levenshtein_lst(word, word_lst, line=''):
    ''' This takes in a word and a word_list and calculates the levenshtein
    distance to every word in word_lst. Then it sorts the words in word_list
    from best to worst. There are then two cases to consider:

    1. If a match in word_lst is less than LEVENSHTEIN_AUTO_MAX _and_ it is unique;
    meaning there are no other words with the same distance, then the word is replaced
    automatically with the match.

    2. If there is no unique best match, then the program lists every word in word_list
    which has a lower levenshtein distance then LEVENSHTEIN_ASK_MAX and _asks_ the user
    to either keep the word, or pick the best match from the list.

    Example:             word
                      /       \
    ## Noen lure råd {.checkliste}                    | this is the argument 'line'

        (0): sjekkliste  (1): check  (2): challenge   | created by print_levenshtein_wordlist()

    Write in a number from the list above to replace 'checkliste' or hit RETURN to keep: 
                                                      \        /
                                                         word
    '''

    ask_max_lst = defaultdict(list)
    auto_max_lst = defaultdict(list)
    for correct_word in word_lst:
        d = levenshtein(word, correct_word)
        if d < LEVENSHTEIN_AUTO_MAX:
            auto_max_lst[d].append(correct_word)
        elif d < LEVENSHTEIN_ASK_MAX:
            ask_max_lst[d].append(correct_word)

    possible_words = []
    first_hit = True
    # There is no point listing matches with levenshtein distance 0, as then the words
    # would be identical. Since this file is only triggered when word is NOT in word_lst
    # this case never happens. Thus, we start i from 1 instead of 0.
    for i in range(1, LEVENSHTEIN_AUTO_MAX):
        if not auto_max_lst[i]:  # If we do not have any 1 distance hits, continue
            continue
        if len(
                auto_max_lst[i]
        ) == 1:  # If the first non-empy hit below AUTO_MAX is unique, return it
            if first_hit:
                return auto_max_lst[i][0]
        first_hit = False
        possible_words.extend(sorted(auto_max_lst[i]))
    # Sorts the matches first by levenshtein distance, then alphabetically.
    for key in sorted(ask_max_lst.keys()):
        possible_words.extend(sorted(ask_max_lst[key]))

    if line: # If line is non empty, color the incorrect word.
        print('\n{}'.format(line.replace(word, colored(word, ERROR_CLR))))
    print_levenshtein_wordlist(possible_words)
    num, is_num = get_num_from_list(word, possible_words)

    if is_num:
        return possible_words[num]
    return word


def color_word(word, color):
    return colored(word, color) if color else word


def print_levenshtein_wordlist(wordlist):
    ''' Example output

        (0): sjekkliste  (1): check  (2): challenge

    '''

    # Get the terminal size
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    # Linebreaks every 90th character or terminal width, if smaller than 90 characters
    char_count_limit = min(90, int(columns))
    char_count = 0
    spacing = 3  # Every line has three space characters

    print('')
    for i, word in enumerate(wordlist):
        char_count += max(len(str(i)), 4) + spacing + max(len(word), 12)
        if char_count > char_count_limit:
            char_count = 0
            print('')
        # The keyword end='' continues to print on the same line
        print(
            '  {:>4}: {:12}'.format('({})'.format(color_word(i, MAIN_2_CLR)),
                                    color_word(word, CORRECT_CLR)),
            end='')
    print('')


def get_num_from_list(word, wordlist):
    wordlen = len(wordlist)
    num = -1
    while True:
        ask = input(
            '\nWrite in a number from the list above to replace \'{}\' or hit RETURN to keep: '.
            format(color_word(word, ERROR_CLR)))
        try:
            num = int(ask)
        except ValueError:
            pass
        if 0 <= num and num < wordlen:
            return (num, True)
        elif not ask:
            return ('', False)
        else:
            print("Oops the number has to be <= \'num\' < {}".format(wordlen))


# FILE INFO is just a temp file for moving between MD and YML
# This makes sure this temp file is removed after use
def save_FILE_INFO(data):
    if not data['move']:
        os.remove(PATH_2_FILE_INFO)
    else:
        output = open(PATH_2_FILE_INFO, 'wb')
        pickle.dump(data, output)
        output.close()


def update_file_info_if_needed():
    if not PATH_2_FILE_INFO.is_file():
        file_info_ = dict()
        for name in ['move', 'md', 'auto_md', 'yml', 'auto_yml']:
            file_info_[name] = dict()
        output = open(PATH_2_FILE_INFO, 'wb')
        pickle.dump(file_info_, output)
        output.close()


def load_FILE_INFO():
    if not PATH_2_FILE_INFO.is_file():
        update_file_info_if_needed()
    return pickle.load(open(PATH_2_FILE_INFO, "rb"))


if __name__ == "__main__":

    print("Please run LKK_linter.py instead")
