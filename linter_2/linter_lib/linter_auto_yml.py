from linter_defaults import *

REGEX_FIND_KEYS = re.compile(r"(^|\n)( *(\w+):\[([^\]]*)\]| *(\w+):(.*))")



def create_temp_path(filename, newname='_temp'):
    path_1 = os.path.splitext(filename)[0]
    path_2 = os.path.splitext(filename)[1]
    return path_1 + newname + path_2


def new_lesson_yml(new_level=float('inf')):
    with open("./lesson.yml", "w") as f:
        f.write(
            "level: {}".format(new_level if new_level != float('Inf') else ''))


def sort_tags_lesson_yml(key, tags):
    tag_lst = ['']*len(TAGS_[key])
    for tag in tags.split(', '):
        try:
            tag_lst[TAGS_REVERSE_[key][tag]] = tag
        except KeyError:
            continue
    return ', '.join(filter(None,tag_lst))


def update_lesson_yml(yml_data, new_level=float('Inf'), license = None):

    yml_data = re.sub('[\t ]', r'', yml_data)  # Remove all tabs/spaces
    yml_data = re.sub(r',(?! )', r', ', yml_data)  #Adds space after comma

    titles = ['']*len(KEYS_YML)
    titles_extra = []
    keys_str = ['']*len(KEYS)
    keys_extra = []
    tag = ['']

    has_keys = False
    for match in re.finditer(REGEX_FIND_KEYS, yml_data):
        if match.group(5): # This is level, license, tags
            title = match.group(5)
            content = match.group(6)
            if title == 'tags': tag[0] = 'tag:'
            elif title in KEYS_YML:
                titles[KEYS_YML_REVERSE_[title]] = '{}: {}'.format(title, content)
            else:
                titles_extra.append('{}: {}'.format(title, content))
        elif match.group(3): # topic, subject, grade
            has_keys = True
            key = match.group(3).strip()
            tags = sort_tags_lesson_yml(key, match.group(4).strip())
            if key in KEYS:
                keys_str[KEYS_REVERSE_[key]] = '{}{}: [{}]'.format(YML_INDENT_STR, key, tags)
            else:
                keys_extra.append(title)
    new_yml = titles + titles_extra
    if has_keys:
        new_yml.extend(tag + keys_str + keys_extra)
    return '\n'.join(filter(None,new_yml))
    # print(new_yml)


def lesson_yml(lesson_yml_path, new_level=float('inf')):
    lesson_yml_path_temp = create_temp_path(lesson_yml_path)
    if Path(lesson_yml_path).is_file():
        with open(lesson_yml_path, "r") as f:
            yml_data = f.read()
        with open(lesson_yml_path_temp, "w") as g:
            for line in update_lesson_yml(yml_data, new_level):
                g.write(line)

        if filecmp.cmp(lesson_yml_path, lesson_yml_path_temp):
            os.remove(lesson_yml_path_temp)
            print("File has not changed, removing temp")
        else:
            os.rename(lesson_yml_path_temp, lesson_yml_path)
            print("File has changed, renaming temp to perm")
    else:
        new_lesson_yml(new_level)


def main(yml_files, levels=[], liscence=[ ]):

    if not MOVE_LEVEL_2_LESSON_YML:
        for yml_file in yml_files:
            lesson_yml(yml_file)
    else:
        for i, yml_file in enumerate(yml_files):
            lesson_yml(yml_file, level[i])


if __name__ == "__main__":

    main([sys.argv[1]])
