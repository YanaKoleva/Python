#!/usr/bin/env python3

import sys

def seen(word):
   a = "angel"
   if word != "angle":
      for w in word:
         if w.lower() not in a:
            return False
         elif w.lower() in a:
            a = a.replace(w.lower(), "", 1)
      if len(a) == 0:
         return True
      else:
         return False
   return False


for line in sys.stdin:
   lenght = len(line.strip())
   words = [line.strip() for line in sys.stdin]
   print("Words containing 17 letters:", [w for w in words if len(w) == 17])
   print("Words containing 18+ letters:", [w for w in words if len(w) >= 18])
   print("Words with 4 a's:", [w for w in words if w.lower().count("a") == 4])
   print("Words with 2+ q's:", [w for w in words if (w.lower()).count("q") > 1])
   print("Words containing cie:", [w for w in words if len(w.lower().split("cie")) > 1])
   print("Anagrams of angle:", [w for w in words if seen(w)])
