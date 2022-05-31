def divisible_count(x,y,k):
    return len(list(filter(lambda x: not x % k, list(range(x, y + 1)))))
    # return len([i for i in range(x, y + 1) if not i % k])

print(divisible_count(6, 11, 2))