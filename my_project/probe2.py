from re import search
import sys

# patt = r'\b(\w+)\1\b'
# [print(s, end='') for s in sys.stdin if search(patt, s)]

patt = r'\.*(bee)\.*{2,}'
[print(s, end='') for s in sys.stdin if search(patt, s)]
