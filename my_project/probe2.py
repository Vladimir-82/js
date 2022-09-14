import itertools

def next_bigger(n):
    nums = itertools.permutations(str(n))
    q = [int(''.join(i)) for i in nums]
    q = sorted(list(set(q)))
    try:
        nxt = q[q.index(n) + 1]
    except Exception:
        return -1

    return nxt if nxt > n else -1

print(next_bigger(9876543210))