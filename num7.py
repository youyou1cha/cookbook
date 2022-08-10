#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 这个是专门讨论 collections.Counter
# Counter是一个字典，记录元素出现的次数

# Counter 还能做运算

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

more_words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes']

a = Counter(words)
b = Counter(more_words)

print(a+b)
print(a-b)