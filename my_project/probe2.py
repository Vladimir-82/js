from collections import Counter


books = Counter(input().split())
n = int(input())

res = 0
for costumer in range(n):
    book, cost = input().split()
    if books[book] >= 1:

        books.subtract({book: 1})
        res += int(cost)

print(res)

