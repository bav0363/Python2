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

