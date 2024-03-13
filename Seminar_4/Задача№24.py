# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


import random
from random import  randint
print(list := [random.randint(2, 100) for _ in range(int(input("Введите размер списка: ")))])

sum = 0
index = 0
for i in range(len(list)):
    if (list[i - 1] + list[i] + list[(i + 1) % len(list)]) > sum:
        sum = list[i - 1] + list[i] + list[(i + 1) % len(list)]
        index = i
print(f"Максимум ягод за один заход: {sum}")
print("Куст № {} со значением {}".format(index, list[index]))

# решение для автотеста

#arr = [5, 8, 6, 4, 9, 2, 7, 3]

sum = 0
index = 0
for i in range(len(arr)):
    if (arr[i - 1] + arr[i] + arr[(i + 1) % len(arr)]) > sum:
        sum = arr[i - 1] + arr[i] + arr[(i + 1) % len(arr)]
        index = i
print(sum)

# предлагаемое автотестом решение

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
print(max(arr_count))



