#!/bin/sh
git submodule init && \
git submodule update --depth 1 && \
cd codeclub_lesson_builder

# do not install browser sync
sed -i "/^.*\"browser-sync\".*$/d" package.json

# do not install phantomjs
sed -i "/^.*\"metalsmith-phantomjs-pdf\".*$/d" package.json

npm install
