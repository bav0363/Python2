# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
from random import  randint

# def replace(list_1):
#     for i in range(len(list_1)):
#         if list_1[i] > 3:
#             list_1[i] = 1
#     return list_1

# def replace(list_1):
#     list_2 = []
#     max_num = list_1[0]
#     min_num = list_1[0]
#     for i in range(1, len(list_1)):
#         if max_num < list_1[i]:
#             max_num = list_1[i]
#         elif min_num > list_1[i]:
#             min_num = list_1[i]
#     for i in range(len(list_1)):
#         if list_1[i] == max_num:
#             list_2.append(min_num)
#         elif list_1[i] == min_num:
#             list_2.append(max_num)
#         else:
#             list_2.append(list_1[i])
#     return list_2

def replace(list_1):
    max_oc = max(list_1)
    min_oc = min(list_1)
    for i in range(len(list_1)):
        if list_1[i] == max_oc:
            list_1[i] = min_oc
    return list_1

print(list_1 := [random.randint(1, 5) for _ in range(int(input("Введите размер списка: ")))])
list_2 = replace(list_1)
print(list_2)
