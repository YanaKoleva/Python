#!/usr/bin/env python3

import sys


def score(file):
   try:
      with open(file, 'r') as f:
         best = -1
         for line in f:
            m, name = line.strip().split(maxsplit=1)
            m = int(m)
            if m > best:
               best, s = m, [name]
            elif m == best:
               s.append(name)
         print(f'Best student(s): {", ".join(s)}')
         print(f'Best mark: {best}')
   except FileNotFoundError:
      print(f'The file {file} could not be opened')


score(sys.argv[1])
