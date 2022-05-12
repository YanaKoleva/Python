#!/usr/bin/env python3

import sys

for line in sys.stdin:
   options = range(2, int(line.strip()))
   numbers = range(1, int(line.strip()) + 1)
   list = []
   for n in numbers:
      all = [n for o in options if (n % o) == 0]
      if len(all) == 1:
         list.append(int(all[0]))
   print('Primes:', list)
