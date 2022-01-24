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


# def func(n):
#     matrix = [[int(i) for i in input().split()] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 matrix[i][j], matrix[n-j-1][j] = matrix[n-j-1][j], matrix[i][j]
#     for i in matrix:
#         print(*i)
#
# func(int(input()))
# import numpy as np
# n = int(input())
# mat1 = [[int(i) for i in input().split()] for _ in range(n)]
# m = int(input())
#
#
# res = np.linalg.matrix_power(mat1, m)
# for i in range(n):
#     for j in range(n):
#         print(res[i][j], end=' ')
#     print()

# string = input().split()
# n = int(input())
# res = []
# for i in range(n):
#     res.append(string[i::n])
# print(res)


# ферзь
# value = input()
# x, y = value[0], value[1]
# slovarx = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# slovary = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
#
# x, y = slovarx[x], slovary[y]
# matrix = [['.'] * 8 for _ in range(8)]
#
# for x1 in slovarx.values():
#     for y1 in slovary.values():
#         if x1 == x or y1 == y:
#             matrix[y1][x1] = '*'
#
# for x1 in slovarx.values():
#     for y1 in slovary.values():
#         if abs(x - x1) == abs(y - y1):
#             matrix[y1][x1] = '*'
#
# matrix[y][x] = 'Q'
#
# for i in matrix:
#     print(*i)

