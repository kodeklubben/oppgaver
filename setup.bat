@echo off
git submodule init
git submodule update --depth 1
pushd codeclub_lesson_builder
call npm install
popd
pause
