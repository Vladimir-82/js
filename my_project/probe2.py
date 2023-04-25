from collections import defaultdict

size_file = {"GB": 1073741824, "MB": 1048576, "KB": 1024, "B": 1}


def format_size(size):
    if size < 1024:
        return f'Summary: {round(size)} B'
    size /= 1024
    if size < 1024:
        return f'Summary: {round(size)} KB'
    size /= 1024
    if size < 1024:
        return f'Summary: {round(size)} MB'
    size /= 1024
    if size < 1024:
        return f'Summary: {round(size)} GB'


with open('files.txt',  encoding='utf-8') as file:
    files_list = defaultdict(list)
    files_size = defaultdict(int)
    for f in file.readlines():
        files_list[f.strip().split()[0].split('.')[-1]].append(f.strip().split()[0])
        files_size[f.strip().split()[0].split('.')[-1]] += int(f.strip().split()[1]) * size_file[f.strip().split()[2]]
counter = 0
for key, val in sorted(files_list.items(), key=lambda x: x[0]):

    for el in sorted(val):
        print(el)
    print('-' * 10)
    print(format_size(files_size[key]))
    counter += 1
    if counter < len(files_list):
        print()