import re

current_numbers = int(input())

current_members_list = []
for i in range(current_numbers):
    name = input().split('@')[0]
    current_members_list.append(name)

new_numbers = int(input())
for j in range(new_numbers):
    new_name = input()

    namesakes = []
    for name in current_members_list:
        match = re.search(new_name, name)
        if match:
            namesakes.append(name)

        num = 0
        while True:
            if f'{name}'


