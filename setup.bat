@echo off
git submodule init
git submodule update --depth 1
cd codeclub_lesson_builder
npm install
cd ..
pause
