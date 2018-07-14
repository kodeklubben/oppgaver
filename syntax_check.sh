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

# Finds images without ALT tags, Markdown syntax ![]()
# if grep -rniP --color=auto --include=\*.md '\!\[\]\(.*\)$' ./src; then
#     printf "\nFound missing ALT: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Finds images without ALT tags, HTML syntax ![]()
# if grep -rniP --color=auto --include=\*.md '<img(?![^>]*\balt=)[^>]*?>' ./src; then
#     printf "\nFound missing ALT: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Finds every title with an incorrect title, it should be # WORD {.WORD}.
# if (grep -r --include=\*.md '^##* ' ./src | grep -v '{.*}$'); then
#     printf "\nIncorrect title, should be # WORD {.TYPE}: ${red_bold}\$\$${nc}.\n\n"
#     found=true
# fi

# Main titles # need to have exactly ONE empty line beneath and TWO above
if pcregrep -rLiM --include='.*\*.md' '(\S(\n{1,2}|\n{4,})^# .*)|(^# .*(\n|\n{3,})\S)' ./src; then
    printf "\nTitles needs exactly two blank lines below and one above: ${red_bold}\$\$${nc}.\n\n"
    found=true
fi



# Exit with error status (1) if there was a match
if [ "${found}" = true ]; then
    exit 1
fi
