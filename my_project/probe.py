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


# n, m = map(int, input().split())
# row = list(range(1, m + 1))
# for _ in range(n):
#     print(*row)
#     x = row.pop(0)
#     row.append(x)

# n, m = map(int, input().split())
# matrix = [[0] * m for i in range(n)]
# print(matrix)
# print(matrix * 2)


def func(**kwargs):
    for i in kwargs:
        print(kwargs[i])

func(a = 2, b = 3, c = 4)

