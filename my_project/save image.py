import time


def time_track(func):
    def surogate(*args):
        start = time.time()
        res = func(*args)
        stop = time.time()
        print(f'Функцыя адпрацавала {stop - start} секунд')
        return res
    return surogate


@time_track
def count(*args):
    res = 1
    for i in args:
        res *= i ** 6000
    return len(str(res))


print(count(50000, 60000, 70000))