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

# предлагаемое решение из автотеста 

mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

