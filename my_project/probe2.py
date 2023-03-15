import calendar
import datetime

dt = datetime.datetime.strptime(input(), '%Y %m')
year, month = dt.year, dt.month

print(calendar.monthrange(year=year, month=month)[1])
