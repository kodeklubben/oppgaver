#!/bin/sh
# Set CWD to the location of this file
cd ${0%/*}
git pull && \
cd codeclub_lesson_builder && \
git fetch origin nb-NO && \
git merge --no-edit FETCH_HEAD && \
npm install && \
cd .. && \
./gulp dist && \
./gulp links && \
cd dist && \
if [ -e README.md ]
then
    find * ! -name README.md -delete
else
    rm -r *
fi
cp -r ../build/* . && \
git add --all . && \
git commit -m "build $(date)" && \
git push
