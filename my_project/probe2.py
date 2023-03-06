from datetime import date, timedelta


def num_of_sundays(y):
    date1 = date(year=y, month=1, day=1)
    print(date1)
    sundays = 0
    while True:
        if date1.year == y + 1:
            break
        if date1.weekday() == 0:
            sundays += 1
        date1 = date1 + timedelta(days=1)

    return sundays






print(num_of_sundays(768))


