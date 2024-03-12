# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
from random import  randint
print(list := [random.randint(0, 5) for _ in range(int(input("Введите размер списка: ")))])

number = int(input("Введите число для проверки: "))
count = 0
for i in range(len(list)):
    if list[i] == number:
        count += 1
print(f"Число {number} встречается {count} раз(а)")
