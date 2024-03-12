num_rows = 6  # int(input("Введите число строк: "))
num_columns = 6  # int(input("Введите число столбцов: "))

operation = lambda x, y: x * y


def print_operation_table(operation, num_rows, num_columns):
    table = []
    for i in range(1, num_rows + 1):
        print()
        for j in range(1, num_columns + 1):
            table.append(operation)
            print("{:3d}".format(i * j), end=" ")
    return table



print_operation_table(operation, num_rows, num_columns)
