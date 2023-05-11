def takes_positive(func):
    def sur(*args, **kwargs):
        lst = [*args, *kwargs.values()]
        if not all(map(lambda x: isinstance(x, int), lst)):
            raise TypeError
        elif not all(map(lambda x: x > 0, lst)):
            raise ValueError
        res = func(*args, **kwargs)
        return res
    return sur


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(4, 2, 5, 4, 1, 2, 3))
except Exception as err:
    print(type(err))