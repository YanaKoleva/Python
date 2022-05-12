#!/usr/bin/env python3

import sys

import string

def unique(file):
   a = []
   lines = file.readlines()
   for line in lines:
      tokens = line.strip().split()
      for words in tokens:
         words = words.lower()
         for punct in words:
            if punct in string.punctuation:
               words = words.replace(punct, '')
         if words not in a and len(words) > 0:
            a.append(words)
   return len(a)


line = unique(sys.stdin)
print(line)
