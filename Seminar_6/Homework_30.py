# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element = int(input("Введите первый элемент массива: "))
step = int(input("Введите шаг последовательности: "))
amount_elements = int(input("Введите кол-во элементов в последовательности: "))


def progressive(first_element, step, amount_elements):
    if amount_elements < 2:
        return first_element
    print(first_element, end=" ")
    return progressive(first_element + step, step, amount_elements - 1)


print(progressive(first_element, step, amount_elements))
