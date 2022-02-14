# n = int(input())
# d = {}
# for i in range(n):
#     words = input().split(':')
#     d.setdefault(words[0].lower(), words[1].strip())
#
# m = int(input())
# for i in range(m):
#     search = input().lower()
#     print(d.get(search, 'Не найдено'))



# n = int(input())
#
# d = {}
# for el in range(n):
#     word = input().split()
#     d.setdefault(word[0], word[1])
#
# search = input()
# for k, v in d.items():
#     if search == k:
#         print(v)
#     if search == v:
#         print(k)


n = int(input())
d = {}
for el in range(n):
    word = input().split()
    d.setdefault(word[0], [*word[1:]])

m = int(input())

for i in range(m):
    search = input()
    for k, v in d.items():
        if search in v:
            print(k)


# 2
# Германия Берлин Мюнхен Гамбург Дортмунд
# Нидерланды Амстердам Гаага Роттердам Алкмар
# 4
# Амстердам
# Алкмар
# Гамбург
# Гаага