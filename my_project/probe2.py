import csv


def csv_columns(filename):
    dc = {}
    with open(filename, encoding='utf-8') as file:
        rows = csv.reader(file)

        print(list(rows)[0])


        # for row in list(rows)[1:]:
        #     for num, el in enumerate(row):
        #         print(num, el)

                # dc.setdefault(list(rows)[0][num], []).append(el)
                # dc[list(rows)[0][num]] = dc.get(list(rows)[0][num], []).append(el)


    return dc


print(csv_columns('1.csv'))

