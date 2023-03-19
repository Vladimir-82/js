import sys


data = [line.strip() for line in sys.stdin]

print('Анри' if (not data.index(data[-1]) % 2 and not int(data[-1]) % 2) or
      (data.index(data[-1]) % 2 and int(data[-1]) % 2) else 'Дима')







