from linter_defaults import *

REGEX_FIND_KEYS = re.compile(r"(^|\n)( *(\w+) *: *\[([^\]]*)\]| *(\w+) *: *(.*))")


def new_level(yml_path):
    # Makes the user create a level number within the set paramaters
    level = -1
    while True:
        try:
            level = int(
                input("\nOppgave: {}\n  level {}: ".format(
                    yml_path, LEVEL_STR)))
        except ValueError:
            pass
        if MIN_LEVEL <= level and level < MAX_LEVEL:
            return level
        print("Ooops level must be an integer from {} to {}".format(
            MIN_LEVEL, MAX_LEVEL))


def new_lesson_yml(new_yml_path):
    '''If a oppgave lacks a lesson.yml this creates that file.

    In detail, it first checks if 'FILE_INFO' contains lines that needs to be
    written into 'lesson.yml'. Examples are 'license' or 'level' Otherwise it
    uses 'new_level()' and makes user write in the level.
    '''

    settings_from_md_ = load_FILE_INFO()
    has_data = False
    with open(new_yml_path, "w") as f:
        try:
            info_from_md_ = settings_from_md_['move'].pop(new_yml_path)
        except KeyError:
            f.write("level: {}".format(new_level(new_yml_path)))
            return

        new_str = [''] * len(KEYS_YML)
        for key, content in info_from_md_.items():
            if key in YAML_TITLES:
                new_str[KEYS_YML_REVERSE_[key]] = content

        save_FILE_INFO(settings_from_md_)
        f.write('\n'.join(filter(None, new_str)))
        f.write('\n')


def sort_tags_lesson_yml(key, tags):
    tag_lst = [''] * len(TAGS_[key])
    for tag in tags.split(', '):
        if not tag in TAGS_[key]:
            tag = levenshtein_lst(tag, TAGS_[key], '{}: {}'.format(key, tags))
        if tag in TAGS_[key]:
            tag_lst[TAGS_REVERSE_[key][tag]] = tag
    return ', '.join(filter(None, tag_lst))

def fix_parenthesis(temp_content):
    # Removes the outer layer of quotations
    content = re.sub(r'^(\"|\')(.*)(\"|\')$', r'\2', temp_content)
    # Changes all internal quotations to ' and '
    content = re.sub(r'\"(.*)\"', r"'\1'", content)
    # Add back the quotations if need be
    if re.search(r"[^\w\sæøåÆØÅ]", content):
        content = '"{}"'.format(content)
    return content

def update_lesson_yml(yml_data, yml_path):

    yml_data = re.sub('\t', r'{}'.format(YML_INDENT_STR), yml_data) # replaces all tabs

    titles = [''] * len(KEYS_YML)
    titles_extra = []
    keys_str = [''] * len(KEYS)
    keys_extra = []
    tag = ['']

    # This part finds all lines of the form key: word or key: [words]
    # then it checks if key is a legal key, otherwise correct it using
    # the levenshtein_lst function. All these legal keys are then sorted
    # according to the order they appear in the file ../filtertags/keys.yml
    # the tags in [words] are similarly have their spelling checked and sorted
    has_keys = False
    remaining_titles = list(KEYS_YML)
    remaining_keys = list(KEYS)
    for match in re.finditer(REGEX_FIND_KEYS, yml_data):
        if match.group(5):  # This is level, license, tags
            title = match.group(5)
            content = match.group(6)
            if title == 'tags': tag[0] = 'tags:'
            elif title in remaining_titles:
                remaining_titles.remove(title)
                if title == 'license':
                    content = fix_parenthesis(content)
                titles[KEYS_YML_REVERSE_[title]] = '{}: {}'.format(
                    title, content)
            else:
                new_title = levenshtein_lst(title, remaining_titles)
                titles_extra.append('{}: {}'.format(new_title, content))

        elif match.group(3):  # topic, subject, grade
            has_keys = True
            key = match.group(3).strip()
            tags = sort_tags_lesson_yml(key, match.group(4).strip())
            if key in remaining_keys:
                remaining_keys.remove(key)
                keys_str[KEYS_REVERSE_[key]] = '{}{}: [{}]'.format(
                    YML_INDENT_STR, key, tags)
            else:
                new_key = levenshtein_lst(key, remaining_keys)
                keys_extra.append('{}{}: [{}]'.format(YML_INDENT_STR, new_key,
                                                      tags))

    # This part loads in any lines moved from the corresponding markdown file
    if PATH_2_FILE_INFO.is_file():
        file_info = load_FILE_INFO()
        settings_from_md_ = file_info['move'].pop(str(yml_path), None)

        if settings_from_md_:
            for key, title_and_content in settings_from_md_.items():
                number = KEYS_YML_REVERSE_[key]
                if not titles[number]:
                    titles[number] = title_and_content
                    continue
                elif titles[number] == title_and_content:
                    continue
                print(yml_path)
                print("  Oops, it looks like this line already exists:")
                print("    '{}'".format(titles[number]))
                print("  Do you want to replace the line above with")
                print("    '{}'".format(title_and_content))
                answer = input('  [y/n] ')
                if answer.lower().strip() in ['y', 'ja', 'yes', 'ok']:
                    titles[number] = title_and_content
            save_FILE_INFO(file_info)

    new_yml = titles + titles_extra
    if has_keys:
        new_yml.extend(tag + keys_str + keys_extra)
    return '\n'.join(filter(None, new_yml))
    # print(new_yml)


def lesson_yml(lesson_yml_path):
    lesson_yml_path_temp = create_temp_path(lesson_yml_path)
    if Path(lesson_yml_path).is_file():
        with open(lesson_yml_path, "r") as f:
            yml_data = f.read()
        new_yml_data = update_lesson_yml(yml_data, lesson_yml_path)
        with open(lesson_yml_path_temp, "w") as g:
            for line in new_yml_data:
                g.write(line)
            if new_yml_data:
                if not line.endswith('\n'):
                    g.write('\n')

        if filecmp.cmp(lesson_yml_path, lesson_yml_path_temp):
            # File has not changed, removing temp
            os.remove(lesson_yml_path_temp)
        else:
            # File has changed, renaming temp to perm
            os.rename(lesson_yml_path_temp, lesson_yml_path)
    else:
        new_lesson_yml(lesson_yml_path)


def main(yml_files):
    '''This file auto formats lesson.yml files, which can be broken into four
    parts:

    1. Create new yaml files if needed:
    If no loaded files are present, it prompts the user to write in a level.
    This is the bare minimum allowed for a lesson.yml file.

    2. Load moved titles.
    This simply read the moved lines into an existing, or new lesson.yml file
    file if none exists. The loaded titles are then sorted along with any
    existing keys pair.

    3. Fixing spelling mistakes.
    While sorting the keys and tags spelling mistakes are checked. If a key or
    tag is not found, it checks how close it is to a legal key/tag. If it is
    'close enough' it is automatically fixed, otherwise the user is prompted by
    a menu with the closest matches to choose from. For a detailed information
    on how mistakes are found see the 'levenshtein' functions in the
    'linter_defaults.py' for more information.

    4. Sort keys and tags
    This sorts the order of topic, subject, grade according to
    ../src/filtertags/keys.yml. In addition it also sorts the tags in subject,
    grade according to the same file.
    '''

    for yml_file in yml_files:
        lesson_yml(yml_file)
    settings_from_md_ = load_FILE_INFO()


if __name__ == "__main__":

    print("Please run LKK_linter.py in the directory above instead")
