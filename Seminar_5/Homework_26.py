# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.

def exponentiate_1(a):
    if a < 1:
        return 1
    return a * exponentiate_1(a - 1)


a = int(input("Введите число: "))
# b = int(input("Введите степень числа: "))
# print(f"Число {a} в степени {b} равно {exponentiate_1(a, b)}")
print(exponentiate_1(a))