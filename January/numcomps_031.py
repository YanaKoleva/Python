#!/usr/bin/env python3

import sys

for line in sys.stdin:
   numbers = range(1, int(line.strip()) + 1)
   print('Multiples of 3:', [n for n in numbers if n % 3 == 0])
   print('Multiples of 3 squared:', [n * n for n in numbers if n % 3 == 0])
   print('Multiples of 4 doubled:', [n * 2 for n in numbers if n % 4 == 0])
   print('Multiples of 3 or 4:', [n for n in numbers if n % 3 == 0 or n % 4 == 0])
   print('Multiples of 3 and 4:', [n for n in numbers if n % 3 == 0 and n % 4 == 0])
