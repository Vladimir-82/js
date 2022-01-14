# n = int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# print(matrix)


def my_generator(list_1, list_2):
    for i in list_1:
        for j in list_2:
            yield i, j, i * j


lst1 = [3, 4, 5, 6, 7]
lst2 = [1, 88, 3, 6, 7]


gen = my_generator(lst1, lst2)
for i, j, res in gen:
    print(i, j, res)
    if res == 36:
        print('found')
        break
print(next(gen))
