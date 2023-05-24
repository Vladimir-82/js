from datetime import timedelta, date


def dates(start, count=None):
    counter = 0
    while True:
        yield start
        counter += 1
        start += timedelta(days=1)
        if count is not None:
            if counter == count:
                return

generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))




