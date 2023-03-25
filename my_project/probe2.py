import csv



with open('data.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    rows = list(rows)
    del rows[0]
    domens = [row[2].split('@')[1] for row in rows]
    dc = {}
    for d in (domens):
        dc[d] = dc.get(d, 0) + 1
    data = [[key, value] for key, value in sorted(dc.items(), key=lambda x: (x[1], x[0]))]

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['domain', 'count',])
    for row in data:
        writer.writerow(row)


