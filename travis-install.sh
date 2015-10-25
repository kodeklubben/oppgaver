#!/bin/sh
git submodule init && \
git submodule update --depth 1 && \
cd codeclub_lesson_builder && \
sed -i "/^.*\"browser-sync\".*$/d" package.json && \
npm install
