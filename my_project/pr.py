# n = int(input())
# d = {}
# for i in range(n):
#     words = input().split(':')
#     d.setdefault(words[0].lower(), words[1].strip())
#
# m = int(input())
# for i in range(m):
#     search = input().lower()
#     print(d.get(search, 'Не найдено'))


# n = int(input())
#
# d = {}
# for el in range(n):
#     word = input().split()
#     d.setdefault(word[0], word[1])
#
# search = input()
# for k, v in d.items():
#     if search == k:
#         print(v)
#     if search == v:
#         print(k)


# n = int(input())
# d = {}
# for el in range(n):
#     word = input().split()
#     d.setdefault(word[0], [*word[1:]])
#
# m = int(input())
#
# for i in range(m):
#     search = input()
#     for k, v in d.items():
#         if search in v:
#             print(k)


# fuctorial
# def func(n):
#     if n != 0:
#         return n * func(n - 1)
#     else:
#         return 1
#
#
# print(func(5))


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: j ** 2 for i, j in enumerate(numbers)}
#
#
# print(result)

# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {i: j for i, j in colors.items() if j != None}
# print(result)


# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
#
# result = {k: v for k, v in favorite_numbers.items() if len(str(v)) == 2}
# print(result)

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(k.split(':')[0]): k.split(':')[1] for k in s.split()}
# print(result)


# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {k: [v for v in list(range(1, k + 1)) if not k % v] for k in numbers}
#
# print(result)
# result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}



# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {k: v for k, v in letters.items() if not k in remove_keys}
# print(result)




# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {k: [ord(el) for el in k] for k in words}
# print(result)



# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}
# print(result)




# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {tuples[k][0]: tuples[k][1:] for k in range(len(tuples))}
# print(result)



student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

result = [dict(zip(student_ids, dict(zip(student_names, student_grades))))]
print(result)

# [{'S001': {'Camila Rodriguez': 86}}, {'S002': {'Juan Cruz': 98}},...]