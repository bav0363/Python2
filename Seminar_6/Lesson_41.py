# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.


import random

print(list_1 := [random.randint(0, 10) for _ in range(6)])  # range(int(input("Введите размер первого списка: ")))])

# Способ от преподавателя (эталонный) - использование List Comprehension

print(len([i for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[(i + 1)]]))

# result = [list_1[i] for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[(i + 1)]]
# print(result)
# print(len(result))

# Мой вариант
# count = 0
# for i in range(len(list_1)):
#     if list_1[i - 1] < list_1[i] > list_1[(i + 1) % len(list_1)]:
#         count += 1
# print(count)
