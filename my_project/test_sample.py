def gen(lst1, lst2):
    for i in lst1:
        for j in lst2:
            yield i, j, i * j


lst1 = [4, 5, 6, 7]
lst2 = [8, 9, 10, 11]
generator = gen(lst1=lst1, lst2=lst2)

for a, b, res in generator:
    if res == 45:
        print(a, b, res)
        break
print(next(generator))
