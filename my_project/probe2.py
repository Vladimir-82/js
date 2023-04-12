from collections import Counter
from string import ascii_lowercase as letters



with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    res = Counter()
    info = file.readlines()
    for el in info:
        res.update(el.lower())
    keys = filter(lambda x: x in letters, res.keys())
    for el in sorted(keys):
        print(f'{el}: {res[el]}')


