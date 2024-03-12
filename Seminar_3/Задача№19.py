# import random
# from random import  randint
#
# list = []
# size = int(input("Какой будет размер списка? "))
# for i in range(size):
#     list.append(randint(0, 5))
# print(list)
# shift = int(input("На сколько элементов нужно сдвинуть список вправо? "))
# list = list[-shift:] + list[:-shift]
# print(list)

# import random
# from random import  randint
#
# print(list := [random.randint(0, 5) for _ in range(int(input("Введите размер списка: ")))])
# shift = int(input("На сколько элементов нужно сдвинуть список вправо? "))
#
# for i in range(shift):
#     list.insert(0, list.pop())
# print(list)

import random
from random import  randint

print(list := [random.randint(0, 5) for _ in range(int(input("Введите размер списка: ")))])
shift = int(input("На сколько элементов нужно сдвинуть список вправо? "))

for i in range(len((list))):
    print(list[(i - shift) % len(list)], end=" ")