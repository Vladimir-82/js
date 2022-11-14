import time
def time_track(func):
    def surogate(*args):
        start = time.time()
        res = func(*args)
        stop = time.time()
        print(f'функция отработала - {stop - start} сек')
        return res
    return surogate


@time_track
def counter(*args):
    res = 1
    for i in args:
        res *= i**5000
    return len(str(res))


print(counter(40006565, 60006, 545465, 656444))