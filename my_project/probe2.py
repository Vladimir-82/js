def transpose(matrix):
    l = len(matrix[0])
    s = len(matrix)
    res = []
    for row in matrix:
        for i in range(l):
            res.append(matrix[s])
    print(res)

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

transpose(matrix)
