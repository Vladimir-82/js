from fractions import Fraction

n = 10
z = n // 2

while True:
    if str(Fraction(z, (n - z))) == ''.join((str(z), '/', str(n - z))):
        print(Fraction(z, (n - z)))
        break
    else:
        z -= 1
