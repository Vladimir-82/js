import csv


def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        rows = list(csv.reader(file, quotechar='"'))
        for row in rows:
            print(row)


    # with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([line for line in rows[0]])
    #     for key, values in sorted(changes.items()):
    #     writer.writerow(values)


print(condense_csv('1.csv', 'ID'))