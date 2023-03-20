import sys
from re import fullmatch

pattern = ' *#.*'

data = [1 for line in sys.stdin if fullmatch(pattern, line.strip())]


print(data)
print(sum(data))




# from re import fullmatch
#
# pattern = ' *#.*'
# match1 = fullmatch(pattern, ' #123465465')
#
# print(match1)














