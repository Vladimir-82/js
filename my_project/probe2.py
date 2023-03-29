import csv


with open('prices.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))

    # products = [prod for prod in reader.fieldnames[1:]]


    lowest_price = []
    for row in rows[1:]:
        for price in row:
            if price.isdigit():
                lowest_price.append(int(price))
    lp = min(lowest_price)


    products = {}
    for row in rows[1:]:
        for el in row:
            if el == str(lp):
                products.setdefault(rows[0][int(row.index(el))], row[0])
    low = min(products.items(), key=lambda shop: shop[0])
    print(*low, sep=': ')







    # prod_dc = {}
    # for el in reader:
    #     for num, good in enumerate(products):
    #         prod_dc.setdefault(products[num], []).append(el[good])
    #
    # print(prod_dc)