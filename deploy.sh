#!/bin/sh

./gulp links && \
cd kodeklubben.github.io && \
find * ! -name README.md -delete && \
cp -r ../build/* . && \
git add --all . && \
git commit -m "build $(date)" && \
git push
