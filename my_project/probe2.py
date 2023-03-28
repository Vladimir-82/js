import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file, open('condensed.csv', 'w', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(file))
        titles = [id_name]
        dc = {}
        for row in rows:
            dc.setdefault(row[0], []).append(row[-1])
            if row[1] not in titles:
                titles.append(row[1])
        writer = csv.writer(f)
        writer.writerow(titles)
        for key, values in dc.items():
            writer.writerow([key, *values])


print(condense_csv('1.csv', 'Position'))