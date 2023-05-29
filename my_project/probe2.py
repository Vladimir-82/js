def is_prime(number):
    if number == 1:
        return False
    return all(bool(number % i) for i in range(2, number))


print(is_prime(114))