import re
import os
import filecmp

PATH_2_FILTERTAGS = '../filtertags/keys.yml'
PATH_2_SRC = '../src'


def generate_keys_and_tags(path_2_yml_keys=PATH_2_FILTERTAGS):
    keys_w_tags = []
    # Opens the folder filtertags and extracts all the keys and tags
    with open(path_2_yml_keys, 'r') as f:
        for line in f:
            # Every key starts with WORD then :
            key_match = re.search('(\w+):', line)
            if key_match:
                if len(keys_w_tags):
                    # If previous keys, replace the last | with "
                    keys_w_tags[-1] = keys_w_tags[-1][:-1] + "\""
                keys_w_tags.append(key_match.group(1).upper() + " = \"")
            else:
                # every tag starts with not a # and then - followed by word
                tag_match = re.search('^\s*[^#]\s*-\s*(\w+)', line)
                if tag_match:
                    keys_w_tags[-1] += tag_match.group(1) + "|"
    # replace the last | in the last key with "
    keys_w_tags[-1] = keys_w_tags[-1][:-1] + "\""
    return keys_w_tags


def update_file_with_keys_and_tags(filename, keys_w_tags):
    filename_temp = '{}_temp.{}'.format(*filename.split("."))

    # Write file into a temp file, replace the part between
    # "# KEYS START HERE..." and "# KEYS END HERE"
    # from the "keys_w_tags" list. 
    with open(filename_temp, "w") as g:
        lines_past_tags = False
        lines_in_tags = False
        with open(filename, "r") as f:
            for line in f:
                if lines_past_tags:
                    g.write(line)
                else:
                    if line == "# KEYS START HERE (DO NOT REMOVE THESE LINES)\n":
                        g.write(line)
                        lines_in_tags = True
                        for tag in keys_w_tags:
                            g.write(tag + "\n")
                    elif line == "# KEYS END HERE (DO NOT REMOVE THESE LINES)\n":
                        lines_in_tags = False
                        lines_past_tags = True
                    if not lines_in_tags:
                        g.write(line)
    # Overwrite filename with temp file
    os.rename(filename_temp, filename)


def is_filtertag_modified_after_file(filename):
    filtertags_last_modified = os.path.getmtime(PATH_2_FILTERTAGS)
    filename_last_modified = os.path.getmtime(filename)
    return filtertags_last_modified > filename_last_modified


def update_if_needed(files):

    keys_w_tags = []
    for filename in files:
        if is_filtertag_modified_after_file(filename):
            # Only generate the new keys, if a file needs to be updated
            if not keys_w_tags:
                keys_w_tags = generate_keys_and_tags()
            print('{} is outdated, '.format(filename))
            update_file_with_keys_and_tags(filename, keys_w_tags)
            print("File has been updated!")


def main():

    update_if_needed(['md_linter.py', 'yml_linter.py'])

    # Import the files after having updated them
    from md_linter import md_linter
    from yml_linter import yml_linter

    yml_linter(PATH_2_SRC)
    md_linter(PATH_2_SRC)


if __name__ == "__main__":

    main()
