import sys


class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass



def is_good_password(s: str):
    if len(s) < 9:
        return "LengthError"
    if not any(c.islower() for c in s):
        return "LetterError"
    if not any(c.isupper() for c in s):
        return "LetterError"
    if not any(c.isdigit() for c in s):
        return "DigitError"
    return 'Success!'




for password in sys.stdin:
    print(is_good_password(password))
    if is_good_password(password) == 'Success!':
        break


# Short7
# Short71
# Short712
# Short7123
# Beegeek123456
# Stepik1111111111111
# Stepik22222222222222
# Short7
# Short7



