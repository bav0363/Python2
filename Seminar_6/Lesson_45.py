# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
import math

# Эталонное решение
k = 20000

# Эталонное решение
def sum_dev(number: int) -> int: # Функция возвращает сумму всех делителей числа number
    return sum([dev for dev in range(1, int(number / 2 + 1)) if not number % dev])

my_dict = {num: sum_dev(num) for num in range(1, k)} # Создаем словарь, где ключ порядковые число, а значение -
# сумма его делителей

for key, value in my_dict.items():
    if key == my_dict.get(value) and key < value:
            print(key, value)


# Мое в группе
#
# for i in range(1, k):
#     sum_1 = 0
#     sum_2 = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum_1 += j
#     for m in range(1, sum_1):
#         if sum_1 % m == 0:
#             sum_2 += m
#     if i == sum_2 and i < sum_1:
#         print(i, sum_1)

# Мое решение
# my_dict = {}
# for i in range(1, k):
#     sum = 0
#     for j in range(1, int(i / 2 + 1)):
#         if i % j == 0:
#             sum += j
#         my_dict[i] = sum
#
# for key, value in my_dict.items():
#     if key == my_dict.get(value) and key != value:
#         if key < value:
#             print(key, value)
