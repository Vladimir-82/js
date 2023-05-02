def func(x):
    return x ** 2


def dec(f):
    def surogate(arg):
        print('some text')
        res = f(arg)
        return res
    return surogate


print(dec(func)(4))
