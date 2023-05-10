def takes_positive(func):
    def sur(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            len(arg for arg in args if arg > 0) == len(args)
            return res
        except Exception(TypeError) as err1:
            return err1
        except Exception(ValueError) as err2:
            return err2
    return sur


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))