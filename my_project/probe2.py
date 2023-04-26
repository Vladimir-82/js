def convert(n):
    z = '-' if n < 0 else ''
    return z + bin(n).split('b')[-1], z + oct(n).split('o')[-1], z + hex(n).split('x')[-1].upper()


print(convert(-24))
