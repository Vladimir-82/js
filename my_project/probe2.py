def is_power(n):
    def rec(pow=0):
        res = 2 ** pow
        if res > n:
            return False
        if res == n:
            return True
        else:
            return rec(pow + 1)

    return rec()

print(is_power(1111111))







