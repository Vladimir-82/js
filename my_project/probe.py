# n = int(input())
# [print(*[input() for i in range(m)]) for i in range(n)]

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
print(matrix)