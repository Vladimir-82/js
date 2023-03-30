import json
import sys

line = sys.stdin.read()
data = json.loads(line)
for key, value in data.items():
    if isinstance(value, list):
        print(key, end=': ')
        print(*value, sep=',')
    else:
        print(key, value, sep=': ')

