import csv


def condense_csv():
    with open('student_counts.csv', encoding='utf-8') as file, \
            open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as f:
        rows = list(csv.reader(file))

        writer = csv.writer(f)
        classes = rows[0][1:]

        years = [row[0] for row in rows[1:]]
        print(years)


        count = {}
        for clas in range(len(classes)):
            for row in rows[1:]:
                count.setdefault(classes[clas], []).append(row[clas+1])

        print(sorted(count.items()))




        # for key, values in count.items():
        #     writer.writerow([key, *values])








        # writer = csv.writer(f)
        # writer.writerow(titles)
        # for key, values in dc.items():
        #     writer.writerow([key, *values])


print(condense_csv())