
import random
from random import  randint
print(list := [random.randint(0, 5) for _ in range(int(input("Введите размер списка: ")))])

res = float('-inf')
i = 0
while (i < (len(list)) and list[i] > 0):
    if list[i] > res:
        res = list[i]
    i += 1
print(res)