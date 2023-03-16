import time

def timetreak(f):
    def surogate(*args):
        start = time.time()
        res = f(*args)
        stop = time.time()
        print(stop - start)
        return res
    return surogate




# @timetreak
def func(*args):
    res = 1
    for i in args:
        res *= i ** 10000
    return len(str(res))

# print(func(123347, 54334, 54645))

print(timetreak(func)(123347, 54334, 54645))
