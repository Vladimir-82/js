import time
def timetrack(func):
    def surogate(*args):
        start = time.time()
        result = func(*args)
        stop = time.time()
        print(f'Функция отработала - {stop-start} секунды')
        return result
    return surogate

@timetrack
def counter(*args):

    res = 1
    for i in args:
        res *= i ** 5000
    return len(str(res))

print(counter(100054, 500045, 533436, 534327))



