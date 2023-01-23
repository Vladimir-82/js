from re import findall as f
from functools import reduce

# 1. Сначала вывести все bee
#
# 2. Затем все beegeek
#
# 3. Затем все beegeekgeek
#
# 4. Затем все beegeekbeegeek


s = 'Correct name is beegeekgeek'


regex = r'((bee)(geek){1,}){1,}'

result = f(regex, s)

print(result)


