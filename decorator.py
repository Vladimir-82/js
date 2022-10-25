def gen(lst1, lst2):
    for i in lst1:
        for j in lst2:
            yield i, j, i * j


lst1 = [4, 5, 6]
lst2 = [3, 7, 8]
generator = gen(lst1, lst2)

for a, b, mul in generator:
    if mul == 35:
        print(a, b, mul)
        break

print(next(generator))


