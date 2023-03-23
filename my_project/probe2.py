import csv

with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    salary = {}
    count = {}
    for row in rows:
        salary[row['company_name']] = salary.get(row['company_name'], 0) + int(row['salary'])
        count[row['company_name']] = count.get(row['company_name'], 0) + 1

    result = {}
    for key, val in salary.items():
        result[key] = val / count[key]

    [print(i[0]) for i in sorted(result.items(), key=lambda x: x[1])]


