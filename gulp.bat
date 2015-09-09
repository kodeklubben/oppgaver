@echo off
set CWD=codeclub_lesson_builder
set MODULES=%CWD%/node_modules

if not "%1"=="" goto task

:: no args, run forever
:gulp
node %MODULES%/gulp/bin/gulp.js --cwd %CWD%
if errorlevel 1 goto gulp
goto done

:task
:: arg supplied, do not run forever
node %MODULES%/gulp/bin/gulp.js --cwd %CWD% %*

:done
set CWD=
set MODULES=
