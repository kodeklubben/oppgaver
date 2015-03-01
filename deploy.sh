#!/bin/sh
#Set CWD to the location of this file
cd ${0%/*}
./gulp links && \
cd kwrl.github.io && \
if [ -e README.md ]
then
    find * ! -name README.md -delete 
else
    rm -rf *
fi
cp -r ../build/* . && \
git add --all . && \
git commit -m "build $(date)" && \
git push
