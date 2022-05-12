#!/usr/bin/env python3

import sys

def min_words(words):
   m = min([len(w) for w in words])
   return [w for w in words if len(w) == m]


def with_vowels(s):
   vowels = 'aeoiu'
   for c in s:
      if c.lower() in vowels:
         vowels = vowels.replace(c, '')
   if len(vowels) == 0:
      return s


def end(words):
   list = [w for w in words if w[-4:] == 'iary']
   return len(list)

def most_es(words):
   max = 0
   for word in words:
      number = word.count('e') + word.count('E')
      if number > max:
         max = number
   return max


words = [words for words in sys.stdin]
print('Shortest word containing all vowels:', min_words([with_vowels(w) for w in words if with_vowels(w) is not None])[0].strip())
print("Words ending in iary:", end(words))
print("Words with most e's:", [w.strip() for w in words if w.count("e") + w.count("E") == most_es(words)])
