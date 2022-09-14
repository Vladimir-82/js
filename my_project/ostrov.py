def sqInRect(lng, wdth):
    res = []
    if lng == wdth:
        return None
    massive = [lng, wdth]
    while massive.count(massive[0]) != len(massive):
        var = sorted(massive)
        res.append(var[0])
        massive = [var[0], var[1] - var[0]]
    return res + res[-1:]

print(sqInRect(37, 14))
