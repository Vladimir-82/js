

def print_operation_table(operation, rows, cols):
    [print(*[operation(rows, cols) for cols in range(1, cols+1)]) for rows in range(1, rows+1)]


print_operation_table(lambda a, b: a * b, 5, 5)