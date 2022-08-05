import string


S = string.ascii_lowercase
DC = dict(zip(list(S), list(range(1, len(S) + 1))))

def high(x):
    DC.values()
    dc = {}
    lst = x.split()
    for word in lst:
        for letter in word:
            dc[word] = dc.get(word, 0) + DC[letter]
    print(dc)
    maximum = max(dc.values())
    for k, v in dc.items():
        if v == maximum:
            return k



    # max(map(lambda y: reduce(add, y, 0), x.split()))
    # res = map(lambda y: reduce(add, y, 0), x.split())

print(high('what time are we climbing up the volcano'))