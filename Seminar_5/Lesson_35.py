# Задача №35. Решение в группах Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
import math
import random

n = random.randint(1, 1000)
print(n)
def is_simple(n):
    if n in [1, 2]:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n ** 0.5), 2): # Делим только на нечетные (шаг 2) и до значения корня проверяемого числа
        if n % i == 0:
            return False
    return True
print(is_simple(n))
