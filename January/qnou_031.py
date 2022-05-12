#!/usr/bin/env python3

import sys

#all = [line.strip() if len(line.lower().split('qu')) == 1 else '' if line.isalpha() is False else '' for line in sys.stdin]
#print('Words with q but no u:', [a for a in all if len(a) > 0])

def qnou(s):
   s = s.replace('qu', '-')
   return 'q' in s


qnous = [w.strip() for w in sys.stdin if qnou(w.lower())]
print(f'Words with q but no u: {qnous}')
