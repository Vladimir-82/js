import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    res = {}

    for row in rows:
        res.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

with open('addresses.json', 'w') as file:
    json.dump(res, file)