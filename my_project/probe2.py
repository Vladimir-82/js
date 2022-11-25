from fractions import Fraction
from functools import reduce
from math import factorial as f

a = int(input())


print(reduce(lambda x, y: x + y, map(lambda z: Fraction(1, f(z)), [*range(1, a + 1)])))