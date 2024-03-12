# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# import random
# from random import  randint
# print(list := [random.randint(0, 20) for _ in range(int(input("Введите размер списка: ")))])
#
# number = int(input("Введите число для проверки: "))
# check = float('inf')
# result = 0
# for i in range(len(list)):
#     if abs(list[i] - number) < check:
#         check = abs(list[i] - number)
#         result = list[i]
# print(check)
# print(result)

list_1 = [1, 2, 3, 4, 5]
k = 6

k = int(input("Введите число для проверки: "))
check = float('inf')
result = 0
for i in range(len(list_1)):
    if abs(list_1[i] - k) < check:
        check = abs(list_1[i] - k)
        result = list_1[i]
print(result)

