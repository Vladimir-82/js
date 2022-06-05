def parts_sums(ls):
    # Sums of Parts
    if not ls:
        return [0]
    res = []
    ls.reverse()
    res.append(ls[-1])
    for i in ls:
        res.append(i + res[-1])
    res.reverse()
    return res



ls = [0, 1, 3, 6, 10]
print(parts_sums(ls))

# [20, 20, 19, 16, 10, 0]
