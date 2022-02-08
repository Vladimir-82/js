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

# n = int(input())
# res = [[1 if i == j or i == n - j - 1 else 0 for j in range(n)] for i in range(n)]


# n = int(input())
#
# matrix = [[0] * n for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j + 1 == n:
#             matrix[j][i] = 1
# for i in matrix:
#     print(*i)

# n = int(input())
# matrix = [[1 if i <= j and i <= n - 1 - j or i >= j and i >= n - 1 - j else 0 for j in range(n)] for i in range(n)]
# for i in matrix:
#     print(*i)

n = int(input())
m = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

k, v = int(input().split()[0]), int(input().split()[1])

for i in range(n):
    for j in range(m):
        if j == k:
            matrix[i][k], matrix[i][v] = matrix[i][v], matrix[i][k]
print(matrix)


