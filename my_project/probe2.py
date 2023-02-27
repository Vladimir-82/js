from datetime import date


def saturdays_between_two_dates(start: date, end: date):

    dates = [start, end]
    d1, d2 = min(dates).toordinal(), max(dates).toordinal()
    return len(list(filter(lambda x: date.fromordinal(x).weekday() == 5, range(d1, d2 + 1))))


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))






