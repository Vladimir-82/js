import calendar
import datetime

def get_days_in_month(year, month):

    dt = datetime.datetime.strptime(str(year)+str(list(calendar.month_name).index(month)), '%Y%m')
    print(dt)


print(get_days_in_month(2021, 'December'))
