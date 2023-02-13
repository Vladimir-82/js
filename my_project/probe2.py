numbers = input().split()
print(*sorted(set(filter(lambda x: numbers.count(x) > 1, numbers)), key=int))
