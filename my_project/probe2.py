from collections import Counter


counter = Counter(input().split(','))
max_key = max(counter.keys(), key=len)
for key, val in sorted(counter.items(), key=lambda x: x[0]):
    cost = sum(map(lambda x: ord(x), [el for el in key if el != ' ']))
    print(f'{key.ljust(len(max_key))}: {cost} UC x {val} = {cost * val} UC')
