from linter_defaults import *


# If a file starts with "indexed: false" skip it
def is_indexed(filename):
    with open(filename, 'r') as f:
        first_line = f.readline().replace(" ", "").lower().strip()
        return first_line != "indexed:false"


# Colors the words from bad_words red in a line
def color_incorrect(bad_words, line):
    line = re.sub(r'\b(' + '|'.join(bad_words) + r')\b', '{}', line)
    return line.format(*[colored(w, 'red') for w in bad_words])


def find_incorrect_titles(title_count, titles):
    missing = []
    extra = []
    for title in titles:
        if title_count[title.lower()] > 1:
            extra.append(colored(title.lower(), 'red'))
        elif title_count[title.lower()] < 1:
            missing.append(colored(title.lower(), 'red'))
    miss_str = 'missing: ' + ', '.join(missing) if missing else ''
    extra_str = 'extra: ' + ', '.join(extra) if extra else ''
    if miss_str:
        return miss_str + ' | ' + extra_str if extra_str else miss_str
    else:
        return extra_str


def find_incorrect_tags(filename):
    title_count = defaultdict(int)  # Counts number of titles, topics, etc
    incorrect_tags = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            for title, tag in tags_.items():
                if not line.startswith(title.lower()):
                    continue
                title_count[title.lower()] += 1
                n = True

                # Finds every non-legal tag as defined at the start of the file
                regex = r'\b(?!{0}|{1}\b)\w+'.format(title.lower(), tag)
                m = re.findall(regex, line)  # Places the words in a list
                if m:  # If we got any hits, this means the words are wrong
                    line = color_incorrect(m, line)  # color the words

                # This block finds titles without any legal words (empty).
                else:
                    if title != "level":
                        regex_legal = r'{0}: *\[( *({1}),? *)+\]'.format(
                            title.lower(), tag)
                    else:
                        regex_legal = r'{0}: *( *({1}),? *)+'.format(
                            title.lower(), tag)
                        n = re.search(regex_legal, line)
                    # If no legal words has been found, color the line red
                    if not n:
                        line = colored(line, 'red')

                if m or not n:  # Add line to list of incorrect tags
                    incorrect_tags.append(
                        (' ' * 4 if title != "level" else " ") + line)
                break

    # We find if any title, topic, subject does not appear exactly once
    return (incorrect_tags, title_count)


def slicer(my_str, sub='../'):
    index = my_str.find(sub)
    if index != -1:
        return my_str[index:]
    return my_str


def print_incorrect_titles_and_tags(filename):
    incorrect_tags, title_count = find_incorrect_tags(filename)
    incorrect_titles = find_incorrect_titles(title_count, tags_.keys())
    # If any errors are found we print them
    if incorrect_titles or incorrect_tags:
        print('  {}: {}'.format(
            colored(slicer(str(filename)), 'yellow'), incorrect_titles))
        for incorrect_tag in incorrect_tags:
            print('  {}'.format(incorrect_tag))


def main(files, ):
    global tags_
    tags_ = TAGS_STR_
    tags_.pop('language', None)
    tags_['level'] = LEVEL_STR

    for f in files:
        print_incorrect_titles_and_tags(f)


if __name__ == "__main__":

    print("Please run LKK_linter.py in the directory above instead")
