from datetime import datetime, timedelta, date

pattern = '%d.%m.%Y'
start, stop = datetime.strptime('01.01.0001', pattern), \
    datetime.strptime('31.12.9999', pattern)


counter = {}
for i in range(start.toordinal(), stop.toordinal()):
    if date.fromordinal(i).day == 13:
        d = date.fromordinal(i).isoweekday()
        counter[d] = counter.get(d, 0) + 1

[print(v) for k, v in sorted(counter.items())]