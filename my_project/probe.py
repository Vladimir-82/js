from random import randint
# n = int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# print(matrix)

# n = int(input())
# matrix = [[randint(1, 9) for i in range(n)] for _ in range(n)]
#
# print(matrix)


# n = int(input())
# m = int(input())
# matrix = [print(*[str(i * j).ljust(3) for i in range(m)]) for j in range(n)]


n = int(input())
m = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

k, v = int(input().split()[0]), int(input().split()[1])

for i in range(n):
    for j in range(m):
        if j == k:
            matrix[i][k], matrix[i][v] = matrix[i][v], matrix[i][k]
print(matrix)


