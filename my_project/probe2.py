from re import fullmatch

match1 = fullmatch(r'(-)?(\d+)', '2077')
match2 = fullmatch(r'(-)?(\d+)', '-1337')

print(match1.group(1))
print(match1.group(2))
print(match2.group(1, 2))