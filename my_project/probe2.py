from itertools import permutations


res = list(input())
r = sorted(set(permutations(res, len(res))))
[print(*i, sep='') for i in r]
