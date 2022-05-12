#!/usr/bin/env python3

import sys

for line in sys.stdin:
   numbers = range(1, int(line.strip()) + 1)
   print('Multiples of 3 replaced:', [n if n % 3 != 0 else 'X' for n in numbers])
