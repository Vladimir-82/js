import sys
from re import search


res = 0
counter = 0
for line in sys.stdin:
    try:
        if search('\.', line):
            res += float(line)
        else:
            res += int(line)
    except:
        counter += 1
print(res)
print(counter)


