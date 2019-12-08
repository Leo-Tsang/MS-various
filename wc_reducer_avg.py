#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
current_number_dept_occurances = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue


    if current_word == word:
        current_count += count
        current_number_dept_occurances += 1
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count / (1.0 * current_number_dept_occurances))
        current_count = count
        current_word = word
        current_number_dept_occurances = 1

if current_word == word:
    print '%s\t%s' % (current_word, current_count / (1.0 * current_number_dept_occurances))