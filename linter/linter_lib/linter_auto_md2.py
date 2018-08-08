import sys
import re

import textwrap

CODE_WIDTH = 80

VOID_HTML = [
    "area", "base", "br", "col", "command", "embed", "hr", "img", "input",
    "keygen", "link", "menuitem", "meta", "param", "source", "track", "wbr"
]

VOID_HTML_STR = 'area|base|br|col|command|embed|hr|img|input|keygen|link|menuitem|meta|param|source|track|wbr'
'''
The first line matches -, * or -
Second matches 10-19 if not found, it matches 1-9
this line matches 1.1 , 1.1.1.1. , eg sublists with elements lower than 19
this line matches the checkbox type of lists - [ ]
'''
REGEX_LST = [
    '-|\*|\+', '(1[0-9]|[1-9])\.', '((1[0-9]|[1-9])\.)+(1[0-9]|[1-9])\.?',
    '- \[ \]'
]


def check_if_table(i, md_data_lst):
    '''Tables looks something like:

    word | word    OR  | word | word | word |
    ---  | ---         | ---  |:----:|---:  |

    Thus, the smallest line that could possibly contain a table (with two
    columns) is 7 characters.

    Then, if we are not at the last line of the file it checks if the following
    line is on the form

    ---  | --- | ---

    e.g. Three or more - followed by | and at most one :
    '''

    line = md_data_lst[i].strip()
    if not line or len(line) < 7 or not '|' in line:
        return False
    is_last_line = i + 1 == len(md_data_lst)
    if is_last_line:
        return
    next_line = md_data_lst[i + 1].strip()
    # Finds ---| many times followed by an --- followed by 0 or 1 |
    if re.search('^\|?( *:?-{3,}:? *\|){1,}( *:?-{3,}:? *\|?)$', next_line):
        return True


def count_columns_in_table(line):
    return line[1:-1].strip().count('|') + 1


def format_table(table, columns=0):

    # Formats the table into a matrix of size rows, columns
    matrix = [list(filter(None, row.split('|'))) for row in table.split('\n')]
    rows, columns = len(matrix), len(matrix[0])

    # Finds the longest string in each column, also strips whitespace
    lengths = [0] * columns
    for row in range(rows):
        for column in range(columns):
            element = matrix[row][column].strip()
            lengths[column] = max(len(element), lengths[column])
            matrix[row][column] = element

    # This creates the formating string for the new table
    formating = [''] * columns
    for i, length in enumerate(lengths):
        length = str(length)
        line = matrix[1][i].replace(" ", "")
        if line.startswith(':-'):
            if line.endswith('-:'):
                formating[i] = '{:^' + length + '}'
                matrix[1][i] = ':{}:'.format('-' * (int(length) - 2))
            else:
                formating[i] = '{:' + length + '}'
                matrix[1][i] = ':{}'.format('-' * (int(length) - 1))
        elif line.endswith('-:'):
            formating[i] = '{:>' + length + '}'
            matrix[1][i] = '{}:'.format('-' * (int(length) - 1))
        else:
            formating[i] = '{:' + length + '}'
            matrix[1][i] = '{}'.format('-' * (int(length)))

    line_format = '| {} '.format(' | '.join(formating))
    new_table_lines = [line_format.format(*row) for row in matrix]
    return '\n'.join(new_table_lines)


def append_if_new(md_data_, line, current, nxt=''):
    if current != md_data_['last']:
        md_data_['last'] = current
        md_data_['lst'].append(line)
        md_data_[current].append(md_data_['counter'])
        md_data_['counter'] += 1
    else:
        md_data_['lst'][-1] += '\n' + line
    return md_data_ if not nxt else append_if_new(md_data_, '', nxt)


def split_md(md_data):

    md_data_ = dict(
        lst=[],
        textblocks=[],
        codeblocks=[],
        html=[],
        yaml=[],
        tables=[],
        counter=0,
        last='')

    html_key = ''
    yaml_count = 0
    table_columns = 0

    md_data_lst = md_data.split('\n')
    for i, line in enumerate(md_data_lst):

        if line:
            line = fix_leading_trailing_whitespace(line)

        # This codeblocks extracts the first yaml header
        if yaml_count == 0:
            if line.strip().startswith('--'):
                yaml_count = 1
                # md_data_ = append_if_new(md_data_, '---', 'yaml')
                continue
        elif yaml_count == 1:
            if line.strip().startswith('--'):
                yaml_count = 2
                # md_data_ = append_if_new(md_data_, '---', 'yaml')
                md_data_ = append_if_new(md_data_, '', 'textblocks')
            else:
                if line.strip():
                    md_data_ = append_if_new(md_data_, line, 'yaml')
            continue

        if md_data_['last'] == 'tables':
            # If the number of columns in this line, is the same
            # as in the current table, append to table. Otherwise
            # add to paragraph.
            is_table = count_columns_in_table(line) == table_columns
            md_data_ = append_if_new(md_data_,
                                     line,
                                     'tables' if is_table else 'textblocks')
            continue

        # If we are not in a html block, check if we are in a codeblock
        if not (md_data_['last'] == 'html'):

            is_codeblock = md_data_['last'] == 'codeblocks'
            codeblock_start_end = re.search('^ *((`{2,}([^`\n]+)`{2,})|((`{2,})(.*)))', line)
            # The regex above checks both for starting and ending backticks
            if codeblock_start_end or is_codeblock:
                md_data_ = append_if_new(md_data_, line, 'codeblocks')
                if codeblock_start_end:
                    is_oneliner = True if codeblock_start_end.group(2) else False
                    if is_codeblock or is_oneliner:
                        md_data_ = append_if_new(md_data_, '', 'textblocks')
                continue


        # If we are in a html block, use regex to check for end of block, else append
        if md_data_['last'] == 'html':
            # Searches for expressions of the form: </hide>
            match = re.search(r'( *< */ *({}).*?> *$)'.format(html_key), line)
            md_data_ = append_if_new(md_data_, line, 'html')
            if match:
                md_data_ = append_if_new(md_data_, '', 'textblocks')
            continue

        # This regex searches for html
        match = re.search(
            r'^ *(< *(\w+).*?>.*?< *\/\2.*?>|(< *(\w+).*?>)) *(\r?\n|$)|^ *(!?\[.*\]\(.*\)) *$',
            line)
        if match:
            if match.group(4):
                # Finds codeblocks with no end. Example: <style>
                html_key = match.group(4)
                md_data_ = append_if_new(md_data_, line, 'html')
                if html_key in VOID_HTML:
                    md_data_ = append_if_new(md_data_, '', 'textblocks')
            elif match.group(1) or match.group(6):
                # group 1: Matches html, that starts and ends on the same line
                # Example: <div id="boks"></div>
                # group 6: matches images and links of the form ![]() or []()
                md_data_ = append_if_new(md_data_, line, 'html', 'textblocks')
            continue

        # If we are not in a html, codeblock or yaml, check if tabla
        if check_if_table(i, md_data_lst):
            md_data_ = append_if_new(md_data_, line, 'tables')
            table_columns = count_columns_in_table(line)
            continue

        # Finally, if we are not in a table, html, codeblock or yaml add to text
        md_data_ = append_if_new(md_data_, line, 'textblocks')

    return md_data_


def fix_headers(header):
    # Makes sure every title has exactly one space after the last #
    header = re.sub(r'^ *(#+) *(.)', r'\1 \2', header)

    # Removes all punctuation from titles
    header = re.sub(r'^(#+ .*)(\.|\,|\;)', r'\1', header)

    # This fixes mistakes in the class, eg {{.intro} or .intro
    header = re.sub(r'^(#.*[^ {]) *(?:{*)(\.\w+)(?:}*)(.*)$', r'\1\3 {\2}',
                    header)

    # Makes sure every main header has an extra line above
    if header.startswith('# '):
        header = '\n{}'.format(header)
    return header


def fix_leading_trailing_newlines(line, before=0, after=0):
    if not line.strip():
        return '\n' * (before + after)
    for i in range(len(line)):
        if line[i] != '\n':
            break
    return '{}{}{}'.format(line.rstrip()[i::], '\n' * before, '\n' * after)


def add_newline_end_of_file(md_data):
    if md_data:
        return fix_leading_trailing_newlines(md_data, 0, 1)
    return md_data


def format_paragraph(paragraph, paragraph_type):
    '''Formats paragraphs into lines of max CODE_WIDTH (usually 80) length.
    The first line remove all tabs, spaces, newlines etc from the paragraph.
    Then the textwrap commands fills in the lines according to the rules set.
    '''

    line = paragraph[0]
    initial_indent = subsequent_indent = len(line) - len(line.lstrip())
    if initial_indent and initial_indent % 4 == 0:
        return paragraph

    if paragraph_type == 'list':
        subsequent_indent += TAB_INDENT

    return textwrap.fill(
        " ".join(paragraph.split()),
        width=CODE_WIDTH,
        initial_indent=' ' * initial_indent,
        subsequent_indent=' ' * subsequent_indent,
        break_long_words=False,
        break_on_hyphens=False)
    return new_paragraph


TAB_INDENT = 2
REGEX_PARAGRAPH = '([\s\S]+?)((\r?\n{2})|$)'


def fix_leading_trailing_whitespace(line):
    ''' Removes all trailing whitespace in line, it also
    makes sure that the leading whitespace is a multiple
    of TAB INDENT'''

    leading_indent_len = len(line) - len(line.lstrip())
    if leading_indent_len:
        leading_indent_len -= leading_indent_len % TAB_INDENT
    return ' ' * leading_indent_len + line.strip()


def fix_list(line):
    # This makes sure checklists look like - [ ] not -[] or -[ ] etc
    line = re.sub(r'^( *-) *\[ *\] *(.)', r'\1 [ ] \2', line)

    # This makes sure -, +, * look like '* ' not '*' or '*   ' etc
    line = re.sub(r'^( *(\*|\-|\+)) *(.)', r'\1 \3', line)

    # This makes sure '1.', '1.2.3.' look like '1. text' and not '1.text'
    line = re.sub(
        r'^((?:(?:1[0-9]|[1-9])\.)+(?:1[0-9]|[1-9])?)( *)(?![0-9\.])', r'\1 ',
        line)

    return line


def is_header_or_list(line, symbol, text, can_be_quickfixed=True):
    print('''
HEADER ERROR: The following line starts with a \'{}\'\n\n  {}
'''.format(symbol, line))
    ask = input(
        'Every {typ} needs to start with \'{sym} \' ({sym} then space) is the line above a {typ}? [y/n]: '.
        format(typ=text, sym=symbol))
    if can_be_quickfixed:
        print(
            'You can avoid this error by writing \'\{sym}\' whenever a \'{sym}\' starts a line\n'.
            format(sym=symbol))
    return ask.lower() in ['yes', 'ok', 'y', 'j', 'ja']


def is_header(line):
    '''First it uses some simple regex to determine whether the line starts with a
    #. If it does not it is obviously not an header. Then it checks if this #
    is followed by a space. If it is, then the line is an header, otherwise it
    asks the user to confirm whether the line is an header.
    '''

    header = re.search(r'^(#+)( *).', line)
    if not header:
        return False
    if header.group(2):
        return True
    return is_header_or_list(line, '#', 'header')


def is_list_symbol(line):
    lst = re.search(r'^(\*|\-|\+)( *).', line)
    if not lst:
        return False
    symbol = lst.group(1)
    spacing = lst.group(2)
    if symbol == '*' and re.search(r'^\*.*\*', line):
        return False
    if spacing:
        return True
    return is_header_or_list(line, symbol, 'element')


def is_list_number(line):
    number_lst = re.search(
        r'^((?:(?:1[0-9]|[1-9])\.)+(?:1[0-9]|[1-9])?)( *)(?![0-9\.])', line)
    if not number_lst:
        return False
    enumeration = number_lst.group(1)
    spacing = number_lst.group(2)
    if spacing:
        return True
    return is_header_or_list(line, enumeration, 'element', False)


def update_paragraph(text_, next_category):
    if text_['paragraph']:
        line = ' '.join(text_['paragraph'])
        formated_paragraph = format_paragraph(line, text_['category'])
        text_['text_new'].append(formated_paragraph)
        text_['paragraph'] = []
        text_['category'] = next_category
    return text_


def fix_md_text(text):

    text_ = dict(
        text_new = [],
        category = '',
        paragraph = [],
        )
    for line in text.split('\n'):
        lline = line.lstrip()
        if not line.strip():
            text_ = update_paragraph(text_, '')
            continue

        if is_header(lline):
            text_ = update_paragraph(text_, 'header')
            text_['text_new'].append(fix_headers(line))

        elif is_list_symbol(lline) or is_list_number(lline):
            text_ = update_paragraph(text_, 'list')
            text_['text_new'].append(fix_list(line))

        else:
            if not text_['category']:
                text_['category'] = 'text'
            text_['paragraph'].append(line)

    return '\n\n'.join(text_['text_new'])


def format_md(md_data):
    md_data_ = split_md(md_data)

    for i in md_data_['html']:
        html = md_data_['lst'][i]

    for i in md_data_['tables']:
        table = md_data_['lst'][i]
        md_data_['lst'][i] = format_table(table)

    for i in md_data_['textblocks']:
        text = md_data_['lst'][i]
        if not text.strip():
            md_data_['lst'][i] = ''
        else:
            md_data_['lst'][i] = fix_md_text(text)

    md_data = '\n\n'.join(filter(None, md_data_['lst']))
    return add_newline_end_of_file(md_data)


if __name__ == "__main__":

    filename = sys.argv[1]
    with open(filename, "r") as f:
        md_data = f.read()

    md_data = format_md(md_data)

    print(md_data)
