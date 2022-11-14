# def func(n, m):
#     mas = [[input() for i in range(m)] for j in range(n)]
#     [print(*i[::-1]) for i in mas]
#
#
#
#
# n, m = map(int, input().split())
# func(n, m)









n, m = map(int, input().split())
mas = [[input() for i in range(m)] for j in range(n)]
[print(*i[::-1]) for i in mas]





