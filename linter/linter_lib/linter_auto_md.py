from linter_defaults import *
import textwrap

# REGEX_FIND_YML = re.compile(r"(?<=^---\s)[\s\S]+?(?=\r?\n---)", re.DOTALL)
REGEX_FIND_YML = re.compile(r"^---[\s\S]*?---", re.DOTALL)
REGEX_FIND_TITLES = re.compile(r" *(\w+) *: *(.*)")

REGEX_4_CODEBLOCKS = '```[\s\S]*?```|`[\s\S]*?`'

REGEX_PARAGRAPHS = re.compile(r' *```[\s\S]*?```|`[\s\S]*?`|(((?<=\n\n)|(?<=(\r\n){2}))( *)([a-z A-Z æøåÆØÅ][\s\S]*?)(?=(\r?\n){2}))', re.DOTALL)
REGEX_LISTS = re.compile(
    r' *```[\s\S]*?```|`[\s\S]*?`|(((?<=\n\n)|(?<=(\r\n){2}))( *)((- \[ \]|[1-2]?[1-9]\.|\-|\+|\*) \w[\s\S]*?)(?=\n\n|(\r\n){2}|$))'
    , re.DOTALL)


def fix_wrong_class_names(md_string):
    ''' Searches through all headers with classes, if the class
    is not in CLASSES_LIST; it corrects the mistake. Based on
    the severity of the mistake either it is fixed automatically
    or a simple menu shows up, showing the user for the closest matches
    Example:
              first_part_of_header   class_name = "intror"
                /              \       /    \
                 # introduction      {.intror}
                \                             /
                           header
    '''

    matches = re.finditer(r'((\n|^)#+ .*){.(\w+)}', md_string)
    for match in matches:
        if not match.group(3).strip():
            continue
        class_name = match.group(3)
        first_part_of_header = match.group(1)
        header = match.group(0)
        if class_name not in CLASSES_LIST:
            new_class_name = levenshtein_lst(class_name, CLASSES_LIST,
                                             header.strip())
            new_header = '{} {{.{}}}'.format(first_part_of_header,
                                             new_class_name)
            md_string = re.sub(re.compile(header), new_header, md_string)
    return md_string


def format_paragraph(paragraph, initial_indent, subsequent_indent):
    '''Formats paragraphs into lines of max CODE_WIDTH (usually 80) length.
    The first line remove all tabs, spaces, newlines etc from the paragraph.
    Then the textwrap commands fills in the lines according to the rules set.
    '''

    return textwrap.fill(
        " ".join(paragraph.split()),
        width = CODE_WIDTH,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
        break_long_words=False,
        break_on_hyphens=False)


def round_down_2_multiple_of_div(indent, div=TAB_INDENT):
    ''' This makes sure indent is a multiple of div or
    more commonly TAB_INDENT. Example:

            before:         after
            ''              ''
            ' '             ''
            '  '            '  '
            '   '           '  '
            '    '          '    '
            '     '         '    '
    '''
    num = len(indent)
    return ' '*(1+(num - (num%div)))


def format_paragraphs(data, REGEX, name):
    ''' Formats paragraphs starting with words, or paragraphs starting with
    -, +, 1. or - [ ] into the correct number of indents.
    '''
    matches = re.finditer(REGEX, data)
    if name == 'lists':
        for m in matches:
            if not m.group(1):
                continue

            paragraph, indent = m.group(1), m.group(4)
            # The following should NOT be neccecary, but is added as an failsafe
            if '```' in paragraph:
                continue

            # If the intent is not a multiple of 2 round it down
            if len(indent) % TAB_INDENT != 0:
                indent = ' '*(len(indent) - (len(indent)%TAB_INDENT))
            formated_paragraph = format_paragraph(paragraph, indent, indent + TAB_INDENT_STR)
            data = data.replace(paragraph, str(formated_paragraph))
    elif name == 'paragraphs':
        for m in matches:
            # The m.group(0) is the thrashcan, we only want group 1.
            if not m.group(1):
                continue

            paragraph, indent = m.group(1), m.group(4)
            # The following should NOT be neccecary, but is added as an failsafe
            if '```' in paragraph:
                continue

            # In markdown paragraphs with indent 4, 8 etc are treated as
            # codeblocks and as such should not be indented.
            if indent and len(indent) % 4 == 0:
                continue
            if len(indent) % TAB_INDENT != 0:
                indent = ' '*(len(indent) - (len(indent)%TAB_INDENT))
            formated_paragraph = format_paragraph(paragraph, indent, indent)
            data = data.replace(paragraph, str(formated_paragraph))
    return data


def regex_exclude_codeblock_add_newlines(regex, before, after, md_string):
    regex_outside_codeblocks = '{}|({})'.format(REGEX_4_CODEBLOCKS, regex)
    matches = re.finditer(r'{}'.format(regex_outside_codeblocks), md_string)
    for m in matches:
        if not m.group(1):
            continue
        match = m.group(1)
        return_match = '\n'*before + match.strip() + '\n'*after
        md_string = re.sub(match, r'{}'.format(return_match), md_string)
    return md_string


def update_md(md, filepath):
    # Remove trailing whitespace if it exists
    md = [line.rstrip() for line in md]

    # Replace tab with spaces as defined in linter_defaults.py (usually 2 or 4)
    md_string = re.sub(r'\t', r'{}'.format(TAB_INDENT_STR), '\n'.join(md))

    # Finds the YAML header, removes whitespace and makes sure it has exactly three dashes ---
    md_string = re.sub(r'^(\r?\n)* *---?-?((.|\r?\n)*?) *---?-?(\r?\n)*(.*)',
                       r'---\2---\n\n\5', md_string)

    # Removes all punctuation from titles
    md_string = re.sub(r'\r?\n(#+ .*)(\.|\,|\;) *\r?\n', r'\n\1\n', md_string)

    # Corrects all titles with incorrect brackets {}
    # Titles should be formated: # Title {.word}
    md_string = re.sub(r'\r?\n *(#.*[^ {]) *({*)(\.\w+)(}*)( *\r?\n)',
                       r'\1 {\3}\5', md_string)

    # Fixes misspellings in the classes of headers (# some text {.CLASS_NAME})
    md_string = fix_wrong_class_names(md_string)

    # Autoformats main lists (- [ ]). Inserts one blank line above
    md_string = re.sub(r'(.)(\r?\n)+(- ?\[ ?\] ?)(.)', r'\1\n\n- [ ] \4',
                       md_string)

    # Insert blank space above and below code blocks
    md_string = re.sub(r'(\r?\n)*( *```\w*(\r?\n)[\s\S]*?```)(\r?\n)*',
                       r'\n\n\2\n\n', md_string)

    # searches the line with "#" sign (all cases matches - Titles, SubTitles, etc),
    # takes all its upper empty lines and converts them to the one empty line
    md_string = regex_exclude_codeblock_add_newlines('(\r?\n)*(#+ .*)', 2, 0, md_string)

    # again, searches the line with "#" sign, take all its bottom empty lines
    # and converts them to the one empty line
    md_string = regex_exclude_codeblock_add_newlines('(#+ .*)(\r?\n)*', 0, 2, md_string)

    # finds two blank lines or more replaces it with a single newline
    md_string = re.sub(r'(?<!.)(\r?\n){2,}', r'\n', md_string)

    # searches the single "#" sign (Titles only),
    # takes all its upper newlines (at this moment only two of them are there,
    # because of previous substitutions)
    # and converts them to three newlines
    md_string = regex_exclude_codeblock_add_newlines('\n+# [^#\n]*', 3, 0, md_string)

    # finds three blank lines or more replaces it with a single newline
    md_string = re.sub(r'(?<!.)(\r?\n){3,}', r'\n', md_string)

    new_yml_header = sort_yml_in_md(md_string, filepath)
    # Replaces the old YML header with the one defined in sort_yml_md
    if new_yml_header:
        md_string = re.sub(REGEX_FIND_YML, new_yml_header, md_string)

    md_string = format_paragraphs(md_string, REGEX_LISTS, 'lists')

    md_string = format_paragraphs(md_string, REGEX_PARAGRAPHS, 'paragraphs')

    return md_string



def sort_yml_in_md(md_data, filepath):
    '''Sorts and corrects titles in YAML header. Example

    BEFORE                                   AFTER
    ---                                      ---
    languagr: nb                             title: Tegning med SVG
    ttitle: "Tegning med SVG"                author: Teodor Heggelund
    level: 3                                 language: nb
    aauthor: 'Teodor Heggelund'              ---
    ---

    Details:
    * Remvoves ' and " unless the line contains special characters
    * Fixes simple spelling mistakes, for more severe spelling mistakes a menu
      shows up
    * Sorts the keys in order see linter_defaults.py for the specific sorting
      order
    * Saves the titles in MOVE_TITLES in a temp file called FILE_INFO (this is
      put into the lesson.yml file)
    '''

    match = re.findall(REGEX_FIND_YML, md_data)
    if not match:
        return

    # The yaml_header is match[0]
    matches = re.finditer(REGEX_FIND_TITLES, match[0])
    new_title = [''] * len(YAML_TITLES)
    extra_title = []
    for match in matches:
        title = match.group(1)
        content = generate_content(match.group(2), title)
        title_and_content = '{}: {}'.format(title, content)
        if title in MOVE_TITLES:
            save_titles_to_be_moved_2_lesson_yml(title, title_and_content, filepath)
            continue

        if title in YAML_TITLES:
            new_title[YAML_TITLES_REVERSE_[title]] = title_and_content
            continue
        title_2 = levenshtein_lst(title, YAML_TITLES, title_and_content)
        if title_2:
            title_and_content_2 = '{}: {}'.format(title_2, content)
            new_title[YAML_TITLES_REVERSE_[title_2]] = title_and_content_2
        else:
            extra_title.append(title_and_content)

    return '---\n' + '\n'.join(filter(None, new_title)) + '\n---'


def generate_content(temp_content, title):
    content = re.sub(r' *(\"|\')(.*)(\"|\') *', r'\2', temp_content)
    if title == 'level':
        content = '{}'.format(min(max(int(content), MIN_LEVEL), MAX_LEVEL))
    elif title == 'language' and (content not in TAGS_['language']):
        error_line = '{}: {}'.format(title, content)
        content = levenshtein_lst(content, TAGS_['language'], error_line)
    # Changes all internal quotations to ' and ' while outer quotation is " and "
    content = re.sub(r'\"(.*)\"', r"'\1'", content)
    if re.search(r"[^\w\sæøåÆØÅ]", content):
        content = '"{}"'.format(content)
    return content


def save_titles_to_be_moved_2_lesson_yml(title, title_and_content, md_filepath):
    yml_lesson_path = re.sub(r'\w+\.md', LESSON_YML, md_filepath)
    if not Path(yml_lesson_path).is_file():
        return
    file_info = load_FILE_INFO()
    try:
        file_info['move'][yml_lesson_path]
    except KeyError:
        file_info['move'][yml_lesson_path] = dict()
    file_info['move'][yml_lesson_path][title] = title_and_content
    save_FILE_INFO(file_info)


def auto_lint_md(filename):
    temp_file = create_temp_path(filename)

    with open(filename, "r") as md:
        data_md_new = update_md(md, filename)
        # By creating the data_md_new first, it avoids creating the
        # temp file if errors is found in the function 'update_md'.
        with open(temp_file, "w") as md_new:
            for line in data_md_new:
                md_new.write(line)
            if not line.endswith('\n'):
                md_new.write('\n')

    if filecmp.cmp(filename, temp_file):
        # File has not changed, removing temp
        os.remove(temp_file)
    else:
        # File has changed, renaming temp to perm
        os.rename(temp_file, filename)


def main(files_md):
    '''This file autoformats md files, which can be broken into four parts:

    1. Sort and fix yaml titles.
    See sort_yml_in_md() for a detailed explenation. This fixes the order of
    the titles in the YAML header, removes titles that should be moved, as well
    as adding quotation marks " " only where deemed neccecary.

    2. Save titles to be moved.
    See save_titles_to_be_moved_2_lesson_yml(). The purpose is to save the
    lines to be moved in a temp file. This temp file is then accessed by
    auto_lint_md.py, which puts the lines into lesson.yml file and then deletes
    the file.

    3. Fixing spelling mistakes.
    This is done several places in the code. In short it corrects very minor
    mistakes automatically, while more severe mistakes triggers a menu and user
    interaction. For a detailed explanation of how mistakes are fixed see the
    'levenshtein_distance()' functions in the 'linter_defaults.py' module.

    4. Style the files accoding to the style guide.
    This fixes everything from trailing whitespace, to incorrect spacing in
    headers see 'update_md()' for the full list of changes.
    '''

    for file_md in files_md:
        auto_lint_md(file_md)


if __name__ == "__main__":

    print("Please run LKK_linter.py in the directory above instead")
