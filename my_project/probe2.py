from random import choice


def random_numbers(left, right):
    values = list(range(left, right+1))[0]
    return iter(lambda: values, '')






iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))





