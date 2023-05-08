def sort_priority(values, group):
    first = list(sorted(set(values).intersection(set(group))))
    second = list(sorted(set(values).difference(set(first))))
    values[:] = first + second
    return values


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

# [2, 3, 5, 7, 1, 4, 6, 8]