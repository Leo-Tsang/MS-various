#!/usr/bin/python
#Reducer.py
import sys

word_count = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')

    if word in word_count:
        word_count[word].append(int(count))
    else:
        word_count[word] = []
        word_count[word].append(int(count))

#Reducer
for word in word_count.keys():
        max_count = max(word_count[word])
        print'%s\t%s' % (word, max_count)
