def is_hollow(x):
    # Hollow array
    if 0 in x and x[0] != 0 and x[-1] != 0:
        ind = x.index(0)
        if not all(x[ind:-ind]) and x[ind:-ind].count(0) > 2 and len(x[ind:-ind]) == x[ind:-ind].count(0):
            return True

    return False


print(is_hollow([-1,0,0,0,0]))