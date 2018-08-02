from linter_defaults import *

REGEX_ALT_OUTSIDE_CODE = r"```.*?```|`.*?`|(<img(?!.*?alt=(['\"]).*?\2)[^>]*)(>)|(!\[\]\()"
REGEX_LONG_LINES_OUTSIDE_CODE = re.compile(
    r"```(.|\r?\n)*?```|`.*?`|(.{{{},}})".format(
        CODE_WIDTH * CODE_WIDTH_LEEWAY))
REGEX_FIND_YML = re.compile(r"^---[\s\S]+?---", re.DOTALL)

REGEX_BANNED_WORDS = re.compile(r'!\[|http|img|png|jpg|svg|script|\[.*\]\(')


def error_msg(string):
    return '{}'.format(color_word(string, ERROR_CLR))


def find_missing_alts(data):
    ''' In essence this finds every markdown, or html formated
    image missing an ALT tag, outside codeblocks.

    The regex: ```.*?``` finds every codeblocks and thus

                 ```.*?``` | (some other regex)

    would find 'some other regex' OUTSIDE of codeblocks. As all
    the codeblocks has already been captured in the first "group"
    this is sometimes known as the thrashcan principle.

    ( <img(?!.*?alt=(['\"]).*?\2)[^>]*)(> )

    Finds as you might except every img tag without an alt, similarly

    ( !\[\]( )

    Finds every image ![](....  with an empty alt tag. 
    '''

    missing_alts = []
    matches = re.finditer(REGEX_ALT_OUTSIDE_CODE, data, re.DOTALL)
    for match in matches:
        # This matches every img missing an alt: <img src="smiley.gif">
        if match.group(1):
            missing_alts.append((match.start(1), error_msg('ALT'),
                                 match.group(1)))
        # This matches every markdown image ![](smiley.gif) missing an ALT
        elif match.group(4):
            missing_alts.append((match.start(4), error_msg('ALT'),
                                 match.group(4)))
    return missing_alts


def find_long_lines(data):
    ''' Uses the same thrashcan principle as in find_missing_alts.
    Only difference is that we also exclude the lines containing the
    words from the BANNED_WORDS list.

    The reason why we exclude some words, is that we allow long lines
    for images, scripts, and long urls. As these can be hard or even
    impossible to break into smaller chunks.
    '''

    long_lines = []
    matches = re.finditer(REGEX_LONG_LINES_OUTSIDE_CODE, data)
    for match in matches:
        if match.group(2):
            banned_words = re.search(REGEX_BANNED_WORDS, match.group(2))
            if not banned_words:
                long_lines.append((match.start(2),
                                   error_msg('{}>'.format(CODE_WIDTH)),
                                   match.group(2)))
    return long_lines


def find_missing_or_wrong_yaml_title(title_match, title):
    missing_title = ''
    wrong_title = ''
    if not title_match:
        missing_title = (5, error_msg('missing'), color_word(
            title, CORRECT_CLR))
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


def find_incorrect_yaml(data, is_oppgaver):
    '''LOL. This needs to be rewritten as most of it is hardcoded. Extracts the
    yaml header from the .md file, then regex searches for errors
    '''

    match = re.findall(REGEX_FIND_YML, data)
    if not match:
        empty_yaml_titles = [(1, error_msg('YAML'), 'Missing YAML header')]
        return empty_yaml_titles if is_oppgaver else []

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
        # Author is supposed to be placed under title
        char_num_2_line_three = 3 + len('---') + len(
            title.group(0)) if title else 0
        empty_author, wrong_author = find_missing_or_wrong_yaml_title(
            author, 'author')
        empty_external, wrong_external = find_missing_or_wrong_yaml_title(
            external, 'external')
        if (empty_author and empty_external):
            empty_yaml_titles.append(
                (char_num_2_line_three, error_msg('missing'),
                 color_words_in_line('author/external', ['author', 'external'],
                                     CORRECT_CLR)))
        elif not empty_author:
            wrong_yaml_titles.append(wrong_author) if wrong_author else ''
        elif not empty_external:
            wrong_yaml_titles.append(wrong_external) if wrong_external else ''

    empty_yaml_titles.extend(wrong_yaml_titles)
    return empty_yaml_titles


def find_incorrect_class_in_headers(data):
    matches = re.finditer(r'#+ .*{?\.(\w+)}?\s\n', data)
    incorrect_classes = []
    for m in matches:
        if m.group(1) not in CLASSES_LIST:
            line = m.group(0).strip()
            bad_word = m.group(1)
            error_line = (m.start(0), error_msg('class'),
                          color_word_in_line(line, bad_word, ERROR_CLR))
            incorrect_classes.append(error_line)
    return incorrect_classes


def correct_linenumbers(lines_with_errors, data):
    '''Files are read as one long line, this converts
    the character where the error was found to a line number

    Example: Assume the contents of the file looks like:

    ---
    author: Bjørn Jørn
    title:
    language: nt
    ---

    then

    data = '---\nauthor: Bjørn Jørn\ntitle:\nlanguage: nt\n---'

    lines_with_errors = [
      (26, MISSING, title:), (34, ISO, language: nt)
    ]

    Then this program counts that there are exactly 2 \n's in the first 26
    characters of data (in other words data[0:26]), as such the first error
    occurs on line:

                line_number = 1 + data[0:26].count('\n')
                            = 1 + 2
                            = 3

    Now from the first error to the second (in other words in data[26:34])
    There are exactly 1 \n as such the line_number for the second error is

                line_number = 3 + data[26:34].count('\n')
                            = 3 + 1
                            = 4

    Of course it is also possible to simply compute data[0:char].count('\n')
    however this is somewhat computationally expensive, as the char count can
    be upwards of 10 000 lines, so the accumulative method above is prefered.
    '''

    new_lines = lines_with_errors
    prev = 0
    line_number = 1
    for i, line in enumerate(lines_with_errors):
        char = line[0]
        line_number += data[prev:char].count('\n')
        new_lines[i] = (line_number, *line[1:])
        prev = char
    return new_lines


def yml_path(md_path):
    # Replaces '../path/some_filename.md' with '../path/lesson.yml'
    return Path(re.sub(r'(?<=\/).*\.md', LESSON_YML, md_path))


def is_oppgave(md_path):
    # Every oppgave has a lesson.yml in the same folder
    return yml_path(md_path).is_file()


def find_lines_with_errors(data, md_path):
    '''Returns a sorted list of errors, where each element is a tuple:

        (line_number, error_msg, line)

    correct_linenumbers replaces the char number where the error occurs with
    the actual line number. See the function correct_linenumbers() for more
    information.
    '''

    return correct_linenumbers(
        sorted(
            find_missing_alts(data) + find_long_lines(data) +
            find_incorrect_class_in_headers(data) +
            find_incorrect_yaml(data, is_oppgave(md_path))), data)


def slicer(my_str, sub='../'):
    index = my_str.find(sub)
    if index != -1:
        return my_str[index:]
    return my_str


def print_lines_with_errors(md_filepath, data, lines_with_errors):

    # Removes everythin before ../ in the path and colors the path
    print('\n  {}'.format(color_word(slicer(md_filepath), MAIN_2_CLR)))

    for (line_number, error_type, line_w_error) in lines_with_errors:
        if len(line_w_error) > CODE_WIDTH:
            line_w_error = line_2_error[:CODE_WIDTH] + '...'
        color_i = color_word(str(line_number), MAIN_2_CLR)
        print('  {:>15}:{:<18} {}'.format(color_i, error_type, line_w_error))


def main(md_files):

    for md_filepath in md_files:
        with open(md_filepath, "r") as f:
            md_data = f.read()

        lines_with_errors = find_lines_with_errors(md_data, md_filepath)
        if lines_with_errors:
            print_lines_with_errors(md_filepath, md_data, lines_with_errors)


if __name__ == "__main__":

    print("Please run LKK_linter.py instead")
