# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.


import random
from random import  randint


print(list_1 := set([random.randint(0, 10) for _ in range(int(input("Введите размер первого списка: ")))]))
print(list_2 := set([random.randint(0, 10) for _ in range(int(input("Введите размер второго списка: ")))]))

result_list = sorted(list_1.intersection(list_2))
print(f"Пересекающиеся числа без повторений в порядке возрастания: {result_list}")

