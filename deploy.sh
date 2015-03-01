#!/bin/sh
#Set CWD to the location of this file
cd ${0%/*}
./gulp links && \
cd kodeklubben.github.io && \
find * ! -name README.md -delete && \
cp -r ../build/* . && \
git add --all . && \
git commit -m "build $(date)" && \
git push
