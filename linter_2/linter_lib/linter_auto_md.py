from linter_defaults import *

REGEX_FIND_YML = re.compile(r"(?<=^---\s)[\s\S]+?(?=\r?\n---)", re.DOTALL)
REGEX_FIND_REM = re.compile(
    r"\n(?!(title|author|translator|language|external|level)) *([^\n\r:]*:) *(.*)"
)

REGEX_FIND_TITLES = re.compile(r" *(\w+) *: *(.*)")

def sort_yml_in_md(md_data, remove_level):
    match = re.findall(REGEX_FIND_YML, md_data)
    if not match:
        return

    yaml_header = match[0]
    empty_yaml_titles = []
    wrong_yaml_titles = []

    # Exctract header
    yaml_header = re.sub(r' *(\"|\')(.*)(\"|\') *', r' \2', yaml_header)

    title = re.search(r"(title:) *(.*)", yaml_header)
    level = re.search(r"(level:) *([1-4])", yaml_header)
    author = re.search(r"(author:) *(.*)", yaml_header)
    external = re.search(r"(external:) *(.*)", yaml_header)
    licence = re.search(r"(license:) *(.*)", yaml_header)
    lang = re.search(r"(language:) *(\w*) *", yaml_header)
    translator = re.search(r"(translator:) *(.*) *", yaml_header)
    rem = re.finditer(REGEX_FIND_REM, yaml_header)

    sorted_yaml = add_legal_tags(
        [title, level, author, translator, licence, lang, external], remove_level, 1)
    if ALLOW_EXTRA_HEADERS:
        sorted_yaml += add_legal_tags(rem, remove_level, 2)

    if level and remove_level:
        if level.group(2):
            return (sorted_yaml[:-1], level.group(2))
    return (sorted_yaml[:-1], float('Inf'))


def add_legal_tags(tags, remove_level, group_num):
    result_str = ''
    for match in tags:
        if not match:
            continue
        if not match.group(0).strip():
            continue
        if match.group(group_num) == 'level:' and remove_level:
            continue
        non_word = re.search(r"[^\w\sæøåÆØÅ]", match.group(group_num + 1))
        result_str += '{} {}{}{}\n'.format(
            match.group(group_num), '"' if non_word else '',
            match.group(group_num + 1).strip(), '"' if non_word else '')
    return result_str


def update_md(md, filepath):
    # Remove trailing whitespace if it exists
    md = [line.rstrip() for line in md]

    # Replace tab with spaces as defined in linter_defaults.py (usually 2 or 4)
    md_string = re.sub(r'\t', r'{}'.format(TAB_INDENT_STR), '\n'.join(md))

    # Finds the YAML header, removes whitespace and makes sure it has exactly three dashes ---
    md_string = re.sub(r'^\n* *---?-?((.|\n)*?) *---?-?\n*(.*)', r'---\1---\n\n\3', md_string)

    # Corrects all titles with punctuation
    md_string = re.sub(r'\n(#+ .*)(\.|\:|\;) *\n', r'\n\1\n', md_string)

    # Corrects all titles with incorrect brackets {}
    # Titles should be formated: # Title {.word}
    md_string = re.sub(r'(#.*[^ {]) *({*)(\.\w+)(}*)( *\n)', r'\1 {\3}\5', md_string)

    # Autoformats main lists (- [ ]). Inserts one blank line above
    md_string = re.sub(r'(.)\n+(- ?\[ ?\] ?)(.)', r'\1\n\n- [ ] \3', md_string)

    # Insert blank space above and below code blocks
    md_string = re.sub(r'\n*( *```\w*\n[\s\S]*?```)\n*', r'\n\n\1\n\n', md_string)

    # searches the line with "#" sign (all cases matches - Titles, SubTitles, etc),
    # takes all its upper empty lines and converts them to the one empty line
    md_string = re.sub(r'\n+(#[^\n]+)', r'\n\n\1', md_string)

    # again, searches the line with "#" sign, take all its bottom empty lines
    # and converts them to the one empty line
    md_string = re.sub(r'(\n#[^\n]+)\n+', r'\1\n\n', md_string)

    # finds two blank lines or more replaces it with a single newline
    md_string = re.sub(r'(?<!.)\n{2,}', r'\n', md_string)

    # searches the single "#" sign (Titles only),
    # takes all its upper newlines (at this moment only two of them are there,
    # because of previous substitutions)
    # and converts them to three newlines
    md_string = re.sub(r'\n+(#[^\n#]+)', r'\n\n\n\1', md_string)

    sort_yml_in_md_2(md_string, filepath)

    return md_string


def sort_yml_in_md_2(md_data, filepath):
    match = re.findall(REGEX_FIND_YML, md_data)
    if not match:
        return

    yaml_header = match[0]
    empty_yaml_titles = []
    wrong_yaml_titles = []

    # Replace all parenthesis surrounding words

    new_title = ['']*len(YAML_TITLES)
    extra_title = []
    matches = re.finditer(REGEX_FIND_TITLES, yaml_header)
    for match in matches:
        title = match.group(1)
        content = re.sub(r' *(\"|\')(.*)(\"|\') *', r'\2', match.group(2))
        if title == 'level':
            content = '{}'.format(min(max(int(content), MIN_LEVEL), MAX_LEVEL))
        if re.search(r"[^\w\sæøåÆØÅ]", content):
            content = '"{}"'.format(content)

        title_and_content = '{}: {}'.format(title, content)
        if title in MOVE_TITLES:
            yml_lesson_path = re.sub(r'\w+\.md', 'lesson.yml', filepath)
            FILE_INFO['move'][yml_lesson_path][title] = title_and_content
            save_FILE_INFO(FILE_INFO)
            continue
        try:
            new_title[YAML_TITLES_REVERSE_[title]] = title_and_content
        except KeyError:
            extra_title.append(title_and_content)
            continue
    print('\n'.join(filter(None,new_title)))


def auto_lint_md(filename):
    temp_file = create_temp_path(filename)

    with open(filename, "r") as md:
        with open(temp_file, "w") as md_new:
            for line in update_md(md, filename):
                md_new.write(line)

    if filecmp.cmp(filename, temp_file):
        # os.remove(temp_file)
        print("File has not changed, removing temp")
    else:
        # os.rename(temp_file, filename)
        print("File has changed, renaming temp to perm")

def main():
    auto_lint_md('05_tegne.md')


if __name__ == "__main__":

    main()

