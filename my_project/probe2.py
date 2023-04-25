from collections import defaultdict

size_file = {'GB': 1073741824, 'MB': 1048576 , 'KB': 1024, 'B': 1}

with open('files.txt',  encoding='utf-8') as file:
    files_list = defaultdict(list)
    files_size = defaultdict(int)
    files_format = defaultdict(set)

    for f in file.readlines():
        files_list[f.strip().split()[0].split('.')[-1]].append(f.strip().split()[0])
        files_size[f.strip().split()[0].split('.')[-1]] += int(f.strip().split()[1]) * size_file[f.strip().split()[2]]
        files_format[f.strip().split()[0].split('.')[-1]].add(f.strip().split()[2])
print(files_format)
for key, val in sorted(files_list.items(), key=lambda x: x[0]):
    for el in sorted(val):
        print(el)
    print('------')









