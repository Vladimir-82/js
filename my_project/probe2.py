# def cubes_of_odds(iterable):
#     for number in iterable:
#         if number % 2:
#             yield number ** 3
def is_prime(number):
    return all(1 for i in range(2, number) if not number % i)


print(is_prime(7))