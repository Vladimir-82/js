def dict_travel(nested_dicts, new_str=''):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel(v, new_str + f'{k}.')
        else:
            print(f'{new_str}{k}: {v}')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)






