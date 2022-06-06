def matrix_addition(a, b):

    n = len(a)
    m = len(a[0])
    res = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            res[i][j] = a[i][j] + b[i][j]

    return res

A = [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ]

B = [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]

print(matrix_addition(A, B))