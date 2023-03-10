from datetime import datetime

pattern = '%d.%m.%Y'
number = int(input())
dates = {}

for member in range(number):
    first_name, second_name, day = input().split()
    dates[datetime.strptime(day, pattern).toordinal()] = \
        dates.get(datetime.strptime(day, pattern).toordinal(), 0) + 1

maximum = max([v for k, v in dates.items()])
[print(datetime.fromordinal(k).strftime(pattern), sep='\n') for k, v in sorted(dates.items()) if v == maximum]





# if len(oldests) == 1:
#     [print(datetime.fromordinal(v).strftime(pattern), k) for k, v in dates.items() if v == oldest]
# else:
#     print(datetime.fromordinal(oldest).strftime(pattern), len(oldests))