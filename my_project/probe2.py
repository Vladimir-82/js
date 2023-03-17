import calendar
import datetime


def get_all_days(year):
    res = []
    for m in range(1, 13):
        c = calendar.monthcalendar(year, m)
        for week in c:
            if week[3]:
                res.append(datetime.date(day=week[3]+14, month=m, year=year).strftime("%d.%m.%Y"))
                break
    return res





print(*get_all_days(int(input())), sep='\n')
