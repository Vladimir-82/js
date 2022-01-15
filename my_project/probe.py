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


def func():
    field = [8 * ['.'] for _ in range(8)]
    row = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
    col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    horse = input()
    field[row[int(horse[1])]][col[horse[0]]] = 'N'

    for i in [-2, 2]:
        for j in [-1, 1]:
            if 0 <= row[int(horse[1]) + i] <= 7 or 0 <= col[horse[0]] + j <= 7:
                field[row[int(horse[1]) + i]][col[horse[0]]+j] = '*'
    # for i in [-1, 1]:
    #     for j in [-2, 2]:
    #         if 0 <= row[int(horse[1]) + i] <= 7 or 0 <= col[horse[0]] + j <= 7:
    #             field[row[int(horse[1]) + i]][col[horse[0]]+j] = '*'


    for i in field:
        print(*i)


func()
