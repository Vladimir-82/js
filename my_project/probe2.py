n, m = map(int, input().split())
mas = [input().split() for j in range(n)]
[print(*i[-1:n//2-1:-1] + i[:n//2]) for i in mas]



