import csv


with open('prices.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

    products = [prod for prod in reader.fieldnames[1:]]

    prod_dc = {}
    for el in reader:
        for num, good in enumerate(products):
            prod_dc.setdefault(products[num], []).append(el[good])

    print(prod_dc)