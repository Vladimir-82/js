# class Minus:
#
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def sum(self):
#         return self.num_1 - self.num_2
#
#
# operation = Minus(5, 2)
# print(operation.sum())



# import random
#
#
# class File():
#
#     def __init__(self):
#         self.name = 'file_name'
#         self.size = random.randint(1, 2)
#
#
# class Folder():
#
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
# folder = Folder('name_folder: ', 10)
#
# Folder_content = []
# Folder_list = []
# while sum(Folder_list) <= folder.size - 2:
#     file = File()
#     Folder_list.append(file.size)
#     Folder_content.append(file)
#
# print(f'В папке {folder.name} {len(Folder_content)} файлов суммарным размером {sum(Folder_list)}')
# for num, el in enumerate(Folder_content):
#     print(f'{el.name}_{num + 1}, размер файла - {el.size}')



def fibbonaci(n):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = b, a + b

fib = fibbonaci(10000)

to_find = 10

for el in fib:
    if el > to_find:
        break
    else:
        print(el, end=' ')



