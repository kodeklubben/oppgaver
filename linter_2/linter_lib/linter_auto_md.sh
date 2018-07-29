#!/usr/bin/env bash

# LKK_auto_linter
#
# Usage: First allow the script to be run
#
#   chmod +x ./LKK_auto_linter.sh
#
# Now you can run the script on any markdown (md) file
#
#   ./LKK_auto_linter.sh MARKDOWN.md
#

# Explanation of options given to perl:
#
# -i                                    Modifies your input file in-place (making a backup of
#                                       the original). Handy to modify files without the {copy,
#                                       delete-original, rename} process.
#
# -e                                    Allows you to provide the program as an argument rather
#                                       than in a file. You don't want to have to create a script
#                                       file for every little Perl one-liner.
#
#  0                                    Read the entire file (unlike line by line)
#
# -p                                    Places a printing loop around your command so
#                                       that it acts on each line of standard input.

if [ "$1" == "-h" ]; then
    echo "Usage: `LKK_auto_linter` name_of_md_file_you_want_to_edit.md"
    exit 0
fi

# Gives file input a better name and creates temp file
FILE1=$1
FILE2="${FILE1%.md}_temp.md"
cp "$FILE1" "$FILE2"

# Replace TAB with TWO SPACES
perl -i -0pe 's/\t/  /' $FILE2

# Make sure the file ends with a blank line
sed -i -e '$a\' $FILE2

# Remove trailing whitespace if it exists
sed -i -e 's/[[:space:]]*$//' $FILE2

# Fixes YAML header (turns -- or ---- into ---) removes spacing before, adds blank line under
perl -i -0pe 's/^\n*\h*---?-?((.|\n)*?)\h*---?-?\n*(.*)/---\1---\n\n\3/g' $FILE2

# Corrects all titles with punctuation
perl -i -pe 's/^(#+ .*)(\.|\:|\;)\h*$/\1/g' $FILE2

# Corrects all titles with incorrect brackets {}
# Titles should be formated: # Title {.word}
perl -i -pe 's/^ ?(#+ .*[^\{])((\.\w*)|(([^\{]|\{\{+)(\.\w*)\}*)|(\{*(\.\w*)([^\}]|\}\}+)))$/\1\{\8\6\3\}/g' $FILE2

# Autoformats main lists (- [ ]). Inserts space above
perl -i -0pe 's/(.)\n+(- ?\[ ?\] ?)(.)/\1\n\n- \[ \] \3/g' $FILE2

# Converts every line starting with `` or ```` to ``` (Some codeblocks use ````)
# perl -i -pe 's/^(\h*)(````|``)(\w*)$/\1```\3/g' $FILE2

# Insert blank space above and below code blocks
perl -i -0pe 's/\n*( *```\w*\n[\s\S]*?```)\n*/\n\n\1\n\n/g' $FILE2

# searches the line with "#" sign (all cases matches - Titles, SubTitles, etc),
# takes all its upper empty lines
# and converts them to the one empty line
perl -i -0pe 's/\n+(#[^\n]+)/\n\n\1/g' $FILE2

# again, searches the line with "#" sign, take all its bottom empty lines
# and converts them to the one empty line
perl -i -0pe 's/^(#[^\n]+)\n+/\1\n\n/g' $FILE2

# finds two blank lines or more replaces it with a single newline
perl -i -0pe 's/(?<!.)\n{2,}/\n/g' $FILE2

# searches the single "#" sign (Titles only),
# takes all its upper newlines (at this moment only two of them are there,
# because of previous substitutions)
# and converts them to three newlines
perl -i -0pe 's/\n+(#[^\n#]+)/\n\n\n\1/g' $FILE2

# This would overwrite the new file with the old if changes has been made
if cmp -s "$FILE1" "$FILE2"
then
    # echo "The files are the same"
    rm $FILE2
else
    echo "$FILE1"
    mv $FILE2 $FILE1
fi

# Explenation of some of the regex
#
# s/^(\h*)(````|``)(\w*)$/\1```\3/g
#
# s                                   start search
#   ^                                 start of the line
#    (\h*)                            any number of horisontal space (save this in \1)
#         (````|``)                   find 3 or 4 backticks
#                  (\w*)              any number of words ([a-z]) (save this in \2)
#                       $             end of the line
#                        /            start the replacement for the first part
#                         \1          insert content of capture group 1
#                            ```      insert the correct number of backticks
#                                \3   inserts the content of capture group 3
#
# \s                                  any number of whitespace
# \S                                  any number of NON whitespace
#  .                                  any character except linebreak
#
#
#  +                                  modifier. One or more of the preceeding token. a+ would find one a or more
#  ?                                  modifier. Zero or one of the preceeding token
#  *                                  modifier. Any number of the preceeding token
