import re

string = 'beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik'


def func(obj):
    if obj.group(1) == obj.group(2):
        return obj.group(1)



regex = r'\b(\w+)\b[^\w]?[\s]?\b(\1)\b'


while True:

    match = re.search(regex, string)
    print(match)
    if match:
        string = re.sub(regex, r'\2', string)

    print(string)






