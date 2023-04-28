def zip_longest(*args, fill=None):
    s = args
    if not s[0]:
        return []
    lenght = len(max(*args, key=len))
    res = []
    for el in args:
        res.append(el + (lenght - len(el)) * [fill])
    return list(zip(*res))




print(zip_longest([[]]))