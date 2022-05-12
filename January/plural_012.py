#!/usr/bin/env python3

import sys

for line in sys.stdin:
   line = line.strip()
   if line[-1] == 'x' or line[-2:] == 'sh' or line[-1] == 'z' or line[-1] == 's' or line[-2:] == 'ch':
      print(line + 'es')
   elif line[-1] == 'y':
      ch = line[-2].lower()
      if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
         print(line + 's')
      else:
         print(line[:-1] + 'ies')
   elif line[-1] == 'o':
      print(line + 'es')
   elif line[-1] == 'f':
      print(line[:-1] + 'ves')
   elif line[-2:] == 'fe':
      print(line[:-2] + 'ves')
   else:
      print(line + 's')
