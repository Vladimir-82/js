new_print = print

def print(*args,**kwargs):
    res = []
    for el in args:
        if isinstance(el, str):
            res.append(el.upper())
        else:
            res.append(el)
    if kwargs:
        sep = kwargs['sep']
        end = kwargs['end']
    new_print(res)

print('bee', 'geek', sep=' and ', end=' wow')
