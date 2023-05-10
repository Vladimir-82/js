def takes_positive(func):
    def sur(*args, **kwargs):
        try:
            if not all(isinstance(arg, int) for arg in args):
                raise ValueError
            if all(arg > 0 for arg in args):
                raise TypeError
            else:
                res = func(*args, **kwargs)
                return res
        except:
            print('dsws')
    return sur


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))