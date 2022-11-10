n, m = map(int, input().split())
mas = [input().split() for j in range(n)]
ln = len(mas[0])
[print(*i[-1:ln//2:-1] + i[:ln//2+1]) for i in mas]



