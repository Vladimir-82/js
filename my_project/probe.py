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


def func(n):
    matrix = [[int(i) for i in input().split()] for _ in range(n)]
    summ = sum(matrix[0])
    allnum = []
    summ_gd = []
    summ_vd = []
    for i in range(n):
        summ_col = []
        sum_row = []
        for j in range(n):
            allnum.append(matrix[i][j])
            summ_col.append(matrix[j][i])
            sum_row.append(matrix[i][j])

            if i == j:
                summ_gd.append(matrix[i][j])

            if i + j + 1 == n:
                summ_vd.append(matrix[i][j])

        if sum(sum_row) != summ:
            return 'NO'
        if sum(summ_col) != summ:
            return 'NO'
    if sorted(allnum) != list(range(1, n**2 + 1)):
        return 'NO'
    if sum(summ_gd) != summ:
        return 'NO'
    if sum(summ_vd) != summ:
        return 'NO'


    return 'YES'


n = int(input())
print(func(n))
