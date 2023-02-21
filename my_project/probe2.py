import re

current_numbers = int(input())

current_members_list = []
for i in range(current_numbers):
    name = input().split('@')[0]
    current_members_list.append(name)


new_numbers = int(input())
for j in range(new_numbers):
    new_name = input()

    for name in current_members_list:
        match = re.search(new_name, name)
        if match:

            n = 0
            while True:
                if re.fullmatch(new_name, name):
                    n += 1
                    new_name = new_name + str(n)
                else:

                    current_members_list.append(new_name)
                    print(new_name + '@beegeek.bzz')
                    break










