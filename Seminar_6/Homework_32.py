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

# для автотеста 

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

for i in range(len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
         print(i)

# решение из автотеста

for i in range(len(list_1)):
  if min_number <= list_1[i] <= max_number:
    print(i)
