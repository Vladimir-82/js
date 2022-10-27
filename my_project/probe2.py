def key_difference(dc1, dc2):
    result = {}
    dc3 = dc1 | dc2
    for i, j in dc3.items():
        if i not in dc1.keys() and i in dc2.keys():
            result.setdefault(i, 'added')
        elif i in dc1.keys() and not i in dc2.keys():
            result.setdefault(i, 'deleted')
        elif i in dc1.keys() and i in dc2.keys() and dc1.get(i) != dc2.get(i):
            result.setdefault(i, 'changed')
        elif i in dc1.keys() and i in dc2.keys() and dc1.get(i) == dc2.get(i):
            result.setdefault(i, 'equal')
    return result







dict1 = {'one': 'eon', 'two': 'two', 'four': 'True'}
dict2 = {'two': 'own', 'zero': '4', 'four': 'True'}
print(key_difference(dict1, dict2))

