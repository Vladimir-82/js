from itertools import zip_longest


a = iter([1, 2, 3])
print(*zip_longest (a, a))