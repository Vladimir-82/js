import json


with open('food_services.json') as file1:
    data1 = json.load(file1)
    districts = {}
    for cort in data1:
        districts.setdefault(cort["TypeObject"], []).append([cort["Name"], cort["SeatsCount"]])
    for key, val in sorted(districts.items(), key=lambda y: y[0]):
        mx = max(val, key=lambda x: int(x[1]))
        print(key, ', '.join((mx[0], str(mx[1]))), sep=': ')