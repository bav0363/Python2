# Задача №39. Общее обсуждение
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random

print(list_1 := [random.randint(0, 10) for _ in range(6)])  # range(int(input("Введите размер первого списка: ")))])
print(list_2 := [random.randint(0, 10) for _ in range(6)])  # range(int(input("Введите размер второго списка: ")))])

# Способ от преподавателя (эталонный) - использование List Comprehension

result = [i for i in list_1 if i not in list_2] # Эталон
# result = [list_1[i] for i in range(len(list_1)) if list_2.count(list_1[i]) == 0] # Мой List Comprehension

print(result)

# Способ на семинаре
# result = []
# for i in range(len(list_1)):
#     print(list_1[i], end=" ")
#     print(list_2.count(list_1[i]))
#     if list_2.count(list_1[i]) == 0:
#         result.append(list_1[i])
# print(result)

# Мой способ
# list_3 = []
# for i in range(len(list_1)):
#     count = 0
#     for j in range(len(list_2)):
#         if list_1[i] == list_2[j]:
#             count += 1
#             break
#     if count == 0:
#         list_3.append(list_1[i])
#         print(list_1[i], end=" ")
# print()
# print(list_3)
