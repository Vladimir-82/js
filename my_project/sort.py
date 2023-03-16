lst = [4, 1, -56, 99, -100]


for _ in range(len(lst) - 1):
    for j in range(len(lst)-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
