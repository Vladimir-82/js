def my_generator(list_1, list_2):
    for i in list_1:
        for j in list_2:
            yield i, j, i * j


lst1 = [3, 4, 5, 6, 7]
lst2 = [1, 88, 3, 6, 7]


gen = my_generator(lst1, lst2)
for i, j, res in gen:
    if res == 36:
        print(i, j, res)
        break
print(next(gen))