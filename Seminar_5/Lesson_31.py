# Задача №31. Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fibonacci(index):
#     number = 0
#     num_0 = 1
#     num_1 = 1
#     i = 2
#     if index == 0:
#         return num_0
#     elif index == 1:
#         return num_1
#     else:
#         while i < index + 1:
#             number = num_1 + num_0
#             num_1, num_0 = number, num_1
#             i += 1
#         return number

# def fibonacci(index):  # Ряд начинается с 1. т.е. первый элемент = 1
#     if index in [1, 2]:
#         return 1
#     return fibonacci(index - 1) + fibonacci(index - 2)
#
# index = int(input("Введите порядковый номер ряда Фибоначчи: "))
# number = fibonacci(index)
# print(number)
