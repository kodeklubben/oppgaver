from linter_defaults import *

# When this file is loaded into LKK_linter.py the file
# PATH_2_KEYS_AND_TAGS
# might not exist. As LKK_linter creates this file,
# for the submodules this file will always exist.


def generate_keys_and_tags(path_2_yml_keys=PATH_2_FILTERTAGS):
    keys_w_tags_ = dict()
    keys = []
    current_key = ''
    # Opens the folder filtertags and extracts all the keys and tags
    with open(path_2_yml_keys, 'r') as f:
        for line in f:
            # Every key starts with WORD then :
            key_match = re.search('(\w+):', line)
            if key_match:
                current_key = key_match.group(1)
                keys_w_tags_[current_key] = list()
                keys.append(current_key)
            else:
                # every tag starts with not a # and then - followed by word
                tag_match = re.search('^\s*[^#]\s*-\s*(\w+)', line)
                if tag_match:
                    tag = tag_match.group(1)
                    if current_key:
                        keys_w_tags_[current_key].append(tag)
    # replace the last | in the last key with "
    return keys_w_tags_, keys


def create_keys_and_tags_file():
    keys_and_tags_ = dict()
    keys_w_tags_, keys = generate_keys_and_tags()

    tags_str_ = dict()
    tags_reverse_ = dict()
    for key in keys:
        tags = keys_w_tags_[key]
        tags_reverse_[key] = dict()
        tags_str_[key] = '|'.join(tags)
        for i, tag in enumerate(tags):
            tags_reverse_[key][tag] = i

    keys_reverse_ = dict()
    for i, key in enumerate(keys):
        keys_reverse_[key] = i

    keys_and_tags_['tags_lst_'] = keys_w_tags_
    keys_and_tags_['tags_str_'] = tags_str_
    keys_and_tags_['keys_lst'] = keys
    keys_and_tags_['keys_str'] = '|'.join(keys)
    keys_and_tags_['tags_reverse_'] = tags_reverse_
    keys_and_tags_['keys_reverse_'] = keys_reverse_

    output = open(PATH_2_KEYS_AND_TAGS, 'wb')
    pickle.dump(keys_and_tags_, output)
    output.close()


def update_keys_and_tags_if_needed():
    # If either the file keys_and_tags does not exists
    # or if filtertags has been updated, create new keys and tags
    if not PATH_2_KEYS_AND_TAGS.is_file():
        create_keys_and_tags_file()
    else:
        last_modified_date_filtertag = PATH_2_FILTERTAGS.stat().st_mtime
        last_modified_date_keys_tags = PATH_2_KEYS_AND_TAGS.stat().st_mtime
        if last_modified_date_filtertag > last_modified_date_keys_tags:
            create_keys_and_tags_file()


def update_file_info_if_needed():
    if not PATH_2_FILE_INFO.is_file():
        file_info_ = dict()
        for name in ['move', 'md', 'auto_md', 'yml', 'auto_yml']:
            file_info_[name] = dict()
        output = open(PATH_2_FILE_INFO, 'wb')
        pickle.dump(file_info_, output)
        output.close()

update_keys_and_tags_if_needed()
update_file_info_if_needed()
