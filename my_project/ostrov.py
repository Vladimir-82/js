def divisible_count(x,y,k):
    arr = list(filter(lambda x: not x % k, list(range(x, y + 1))))
    counter = 0
    for i in arr:
        counter += 1
    return counter
    # return len([i for i in range(x, y + 1) if not i % k])

print(divisible_count(6, 11, 2))