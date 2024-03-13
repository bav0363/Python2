# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.


import random
from random import  randint


print(list_1 := set([random.randint(0, 10) for _ in range(int(input("Введите размер первого списка: ")))]))
print(list_2 := set([random.randint(0, 10) for _ in range(int(input("Введите размер второго списка: ")))]))

result_list = sorted(list_1.intersection(list_2))
print(f"Пересекающиеся числа без повторений в порядке возрастания: {result_list}")

# решение для автотеста

var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 

var21 = set([int(i) for i in var2.split()])
var31 = set([int(i) for i in var3.split()])

result_list = sorted(var21.intersection(var31))
print(*result_list)

