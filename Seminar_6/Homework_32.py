# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random

print(lst := [random.randint(-10, 20) for _ in range(int(input("Введите размер списка: ")))])

min_limit = int(input("Введите минимальную границу: "))
max_limit = int(input("Введите максимальную границу: "))

print(my_list := [value for value in lst if value >= min_limit and value <= max_limit])


# for i in range(len(my_list)):
#     if my_list[i] >= min_limit and my_list[i] <= max_limit:
#         my_list_2.append(i)
# print(my_list_2)
