#!/bin/bash

find ../src -name '*.md' -type f -exec ./LKK_auto_linter.sh {} \;
