from collections import namedtuple
import csv
import datetime

with open('meetings.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    for row in sorted(rows, key=lambda x:
    (datetime.datetime.strptime(x['meeting_date'], '%d.%m.%Y'),
     datetime.datetime.strptime(x['meeting_time'], '%H:%M').time())):
        print(f"{row['surname']} {row['name']}")