#!/usr/bin/env python3

import sys

name = []
list = []
file = sys.argv[1]

def score():
   try:
      with open(file, 'r') as f:
         f = f.readlines()
         score = 0
         try:
            for line in f:
               line = line.strip().split()
               names = name.append(' '.join(line[1:]))
               if score < int(line[0]):
                  score = int(line[0])
            i = 0
            while i < len(f):
               f[i] = f[i].split()
               if int(f[i][0]) == score:
                  list.append(f[i])
               i += 1

         except ValueError:
            return print('Invalid mark ' + line[0] + ' encountered. Exiting.')

   except FileNotFoundError:
      print('The file ' + file + ' could not be opened')


score()
