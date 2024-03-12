# Задача №37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
import random


# def reverse(count):
#     if count > 0:
#         el = input("Введите элемент: ")
#         reverse(count - 1)
#         print(el, end=" ")
#
# count = int(input("Какое кол-во элементов? "))
# reverse(count)

def reverse(count: int) -> str:
    if count == 0:
        return " "
    char = input("Введите элемент: ")
    return reverse(count - 1) + char
print(reverse(4))