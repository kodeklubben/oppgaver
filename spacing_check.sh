
#!/usr/bin/env bash

found=false

#Color and bold
red_bold='\033[1;31m'
green_bold='\033[1;32m'
nc='\033[0m' # No color

# Explanation of options given to grep:
# -r                                    recursive
# -i                                    ignore case
# -q                                    quitet, do not print
# -P                                    use Perl syntax (not that many backslashes needed)
# --include=\*.tex                      only search in texfiles (the * is a wildcard)
# --exclude-dir={Utkommentert,Meta}     do not search in (any) directory called "Utkommentert" or "Meta"

# Main titles # need to have exactly ONE empty line beneath and TWO above
# if pcregrep -rniM --include='.*\*.md' '(\S(\n{1,2}|\n{4,})^# .*)|(^# .*(\n|\n{3,})\S)' ./src; then
#     printf "\nTitles needs exactly two blank lines below and one above: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Subtitles ##, ###, etc need to have ONE empty line beneath and above
# if pcregrep -rniM --include='.*\.md' '\S\n##|\n{3,}##+|##+.*\n\S|##+.*\n{3,}\S' ./src; then
#     printf "\nSubtitles needs exactly one blank line below and one above: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# # Check that all lists *, +, -. - [ ], 1. 2.  etc have a blank line above
# if pcregrep -nHorM --include='.*\.md' '([^\n]\n|.*\n{3,})^ *(-|\+|\*|([0-9]+.)+) ' ./src; then
#     printf "\nLists need to have a blank line above: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Check that you use SPACE instead of TAB
# if pcregrep -nHorM --include='.*\.md' '\t' ./src; then
#     printf "\nPlease use SPACE instead of TAB: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Check that every file ends with a blank line
if pcregrep -nHorML --include='.*\.md' '\n\Z' ./src; then
    printf "\nThe file must end with a blank line: ${red_bold}\$\$${nc}.\n\n"
    found=true
fi

# Finds every line longer than 100 characters
# if grep -rn --color=auto --include=\*.md '.\{158,\}' ./src |cut -f1,2 -d:; then
#     printf "\nThe recommended line length is 79 characters: ${red_bold}\$\$${nc}.\n\n"
# fi







# Exit with error status (1) if there was a match
if [ "${found}" = true ]; then
    exit 1
fi
