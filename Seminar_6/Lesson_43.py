# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random

print(list_1 := [random.randint(0, 10) for _ in range(6)])  # range(int(input("Введите размер первого списка: ")))])

# Эталонное решение 1

# result = 0
# for item in set(list_1):
#     result += list_1.count(item) // 2
# print(result)

# Эталонное решение 2. Через List Comprehension

print(sum([list_1.count(item) // 2 for item in set(list_1)]))

# Мое решение
# my_list = list(set(list_1))
# result = 0
# for i in range(len(my_list)):
#     result += list_1.count(my_list[i]) // 2
# print(result)




#print(result)


# for i in range(len(list_1) - 1):
#     count = 1
#     for j in range(len(list_1) - 1):
#         if list_1[i] == list_1[j + 1]:
#             count += 1
#         result += count // 2
# print(result)
