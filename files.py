def counter(lst: list):

    res = 1
    for i in lst:
        res *= i ** 5000
    return len(str(res))

print(counter(30))