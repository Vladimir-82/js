import csv
from datetime import datetime


with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))

    changes = {}
    for row in rows[1:]:
        print(row[2])
        day_change = datetime.strptime(row[2], '%d/%m/%Y %H:%M')
        changes.setdefault(row[1], []).append(day_change)


with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([line for line in rows[0]])
    for row in data:
        writer.writerow(row)



