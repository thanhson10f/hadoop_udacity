#!/usr/bin/python

import sys

old_word = None
word_count = 0
node_set = set()

for line in sys.stdin:
    info = line.strip().split('\t')
    
    if not info[1].isdigit():
        continue

    word = str(info[0])
    node_id = int(info[1])

    if old_word and word != old_word:
        node_set_sorted = sorted(node_set)      
        print '{0}\t{1}\t{2}'.format(old_word,word_count, ','.join(map(str, node_set_sorted)))
        word_count = 0
        node_set.clear()
    
    old_word = word
    word_count = word_count + 1
    node_set.add(node_id)

if old_word:
    node_set_sorted = sorted(node_set)
    print '{0}\t{1}\t{2}'.format(old_word, word_count, ','.join(map(str, node_set_sorted)))

