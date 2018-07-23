import re
import glob
from termcolor import colored

# KEYS START HERE (DO NOT REMOVE THESE LINES)
LANGUAGE = "nb|nn|en|da"
TOPIC = "app|electronics|step_based|block_based|text_based|minecraft|web|game|robot|animation|sound|cryptography"
SUBJECT = "mathematics|science|programming|technology|music|norwegian|english|arts_and_crafts|social_science"
GRADE = "preschool|primary|secondary|junior|senior"
# KEYS END HERE (DO NOT REMOVE THESE LINES)

CLASSES = "intro|activity|check|flag|challenge|tip|save|protip|try|sjekkliste"

CLASSES_LIST = CLASSES.split("|")
LANGUAGE_LIST = LANGUAGE.split("|")

REGEX_ALT_OUTSIDE_CODE = r"```.*?```|`.*?`|(<img(?!.*?alt=(['\"]).*?\2)[^>]*)(>)|(!\[\]\()"
REGEX_LONG_LINES_OUTSIDE_CODE = r"```(.|\n)*?```|`.*?`|(.{100,})"
REGEX_FIND_YML = re.compile(r"^---[\s\S]+?---", re.DOTALL)

PATH_2_SRC = '../src'

def error_msg(string):
    return '{}'.format(colored(string, 'red'))


def find_missing_alts(data):
    missing_alts = []
    matches = re.finditer(REGEX_ALT_OUTSIDE_CODE, data, re.DOTALL)
    for match in matches:
        if match.group(1):
            missing_alts.append((match.start(1), error_msg('ALT'),
                                 match.group(1)))
    return missing_alts


def find_long_lines(data):
    long_lines = []
    matches = re.finditer(REGEX_LONG_LINES_OUTSIDE_CODE, data)
    for match in matches:
        if match.group(2):
            banned_words = re.search(
                r'!\[|http|img|png|jpg|svg|script|\[.*\]\(', match.group(2))
            if not banned_words:
                long_lines.append((match.start(2), error_msg('80>'),
                                   match.group(2)))
    return long_lines


def find_missing_or_wrong_yaml_title(title_match, title):
    missing_title = ''
    wrong_title = ''
    if not title_match:
        missing_title = (5, error_msg('missing'), title)
    else:
        if not title_match.group(2):
            wrong_title = (title_match.start(0), error_msg('empty'),
                           title_match.group(1))
        elif "language" == title:
            iso = title_match.group(2)
            if iso not in LANGUAGE_LIST:
                wrong_title = (title_match.start(0), error_msg('iso'),
                               '{} {}'.format(
                                   title_match.group(1), colored(iso, 'red')))
    return missing_title, wrong_title


def find_incorrect_yaml(data, is_oppgaver=True):
    match = re.findall(REGEX_FIND_YML, data)
    if not match:
        if is_oppgaver:
            return [(1, error_msg('YAML'), 'Missing YAML header')]
        else:
            return []

    yaml_header = match[0]
    empty_yaml_titles = []
    wrong_yaml_titles = []

    title = re.search(r"(title:) *(.*)", yaml_header)
    author = re.search(r"(author:) *(.*)", yaml_header)
    external = re.search(r"(external:) *(.*)", yaml_header)
    lang = re.search(r"(language:) *(\w*) *", yaml_header)

    empty_title, wrong_title = find_missing_or_wrong_yaml_title(title, "title")
    empty_yaml_titles.append(empty_title) if empty_title else ''
    wrong_yaml_titles.append(wrong_title) if wrong_title else ''

    empty_title, wrong_title = find_missing_or_wrong_yaml_title(
        lang, "language")
    empty_yaml_titles.append(empty_title) if empty_title else ''
    wrong_yaml_titles.append(wrong_title) if wrong_title else ''

    if is_oppgaver:
        empty_author, wrong_author = find_missing_or_wrong_yaml_title(
            author, 'author')
        empty_external, wrong_external = find_missing_or_wrong_yaml_title(
            external, 'external')
        if (empty_author and empty_external):
            empty_yaml_titles.append('author/external')
        elif not empty_author:
            wrong_yaml_titles.append(wrong_author) if wrong_author else ''
        elif not empty_external:
            wrong_yaml_titles.append(wrong_external) if wrong_external else ''

    empty_yaml_titles.extend(wrong_yaml_titles)
    return empty_yaml_titles


# Colors the words from bad_words red in a line
def color_incorrect(bad_words, line):
    line = re.sub(r'\b(' + '|'.join(bad_words) + r')\b', '{}', line)
    return line.format(*[colored(w, 'red') for w in bad_words])


def find_incorrect_class_in_headers(data):
    matches = re.finditer(r'#+ .*{?\.(\w+)}?\s\n', data)
    incorrect_classes = []
    for m in matches:
        if m.group(1) not in CLASSES_LIST:
            line_w_fixed_brackets = m.group(0).replace('{', '{{').replace(
                '}', '}}').strip()
            incorrect_classes.append((m.start(0), error_msg('class'),
                                      color_incorrect([m.group(1)],
                                                      line_w_fixed_brackets)))
    return incorrect_classes


def find_correct_line_numbers(lines_with_errors, data):
    char_list = [i[0] for i in lines_with_errors]
    line_numbers = []
    prev = 1
    line = 1
    for char in char_list:
        line += data[prev:char].count('\n')
        line_numbers.append(line)
        prev = char
    return line_numbers


def find_lines_with_errors(data, is_oppgave):

    lines_with_errors = []
    lines_with_errors.extend(find_missing_alts(data))
    lines_with_errors.extend(find_long_lines(data))
    lines_with_errors.extend(find_incorrect_class_in_headers(data))
    lines_with_errors.extend(find_incorrect_yaml(data, is_oppgave))
    lines_with_errors.sort()
    return lines_with_errors


def is_oppgaver_path(filepath):
    match = re.search(r"src\/\w+\/\w+\/", filepath)
    if match:
        playlist_match = re.search(r"playlists", filepath)
        return not playlist_match
    else:
        return False


def print_lines_with_errors(filepath):
    with open(filepath, "r") as f:
        data = f.read()

    is_oppgaver = is_oppgaver_path(filepath)
    lines_with_errors = find_lines_with_errors(data, is_oppgaver)
    if lines_with_errors:
        print('\n{}'.format(colored(filepath, 'yellow')))
        line_numbers = find_correct_line_numbers(lines_with_errors, data)

        for i, line in enumerate(lines_with_errors):
            print('{:>15}:{:<18} {}'.format(
                colored(str(line_numbers[i]), 'yellow'), line[1],
                (line[2][:80] + '...') if len(line[2]) > 80 else line[2]))


def md_linter(path=PATH_2_SRC):
    files = glob.glob(path + '/**/*.md', recursive=True)
    for f in files:
        print_lines_with_errors(f)


if __name__ == "__main__":

    print("Please run LKK_linter instead")
    # md_linter()
