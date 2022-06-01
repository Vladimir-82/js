from operator import add
from functools import reduce




def divisible_count(x, y, k):
    # return len(list(filter(lambda x: not x % k, tuple(range(x, y + 1)))))
    # return sum([1 for i in range(x, y + 1) if not i % k])
    # return sum([1 for i in range(x, y + 1) if not i % k])
    return reduce(add, [1 for i in range(x, y + 1) if not i % k], 0)

print(divisible_count(6, 11, 2))