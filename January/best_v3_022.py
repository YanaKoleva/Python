#!/usr/bin/env python3

import sys


def score(file):
   try:
      with open(file, 'r') as f:
         best = -1
         for line in f:
            try:
               m, name = line.strip().split(maxsplit=1)
               m = int(m)

               if m > best:
                  best, s = m, name
            except ValueError:
               print(f'Invalid mark {m} encountered. Skipping.')
         print(f'Best student: {s}')
         print(f'Best mark: {best}')

   except IndexError:
      print('Index Error')


score(sys.argv[1])
