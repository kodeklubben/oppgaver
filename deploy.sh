#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDER="$DIR/codeclub_lesson_builder"

echo "cleaning dist"
# Set CWD to the location of this file
cd $DIR/dist && \
if [ -e README.md ]
then
    find * ! -name README.md -delete
else
    rm -r *
fi

echo "pulling changes"
# do not pull changes while in dir
cd $DIR/.. && \
git -C $DIR pull && \
git -C $BUILDER fetch origin master && \
git -C $BUILDER merge --no-edit FETCH_HEAD && \
cd $BUILDER && \
npm install

echo "build and push"
cd $DIR && \
./gulp dist && \
cp -r build/* dist && \
cd dist && \
git add --all . && \
git commit -m "build $(date)" && \
git push
