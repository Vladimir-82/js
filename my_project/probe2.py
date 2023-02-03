import re

string = 'hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!'


def func(obj):
    print(obj.group(1))
    print(obj.group(2))
    if obj.group(1) == obj.group(2):
        return obj.group(1)



while True:
    regex = r'(\w+)[^\w]?\s?(\w+)'
    match = re.search(regex, string)
    if match:
        string = re.sub(regex, func, string)
    else:
        print(string)
        break


string = re.sub(regex, func, string)









