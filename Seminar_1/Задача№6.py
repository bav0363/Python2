# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

number_of_ticket = int(input("Введите 6-ти значный номер билета: "))
first_half = number_of_ticket // 1000
second_half = number_of_ticket % 1000
sum_first_half = 0
sum_second_half = 0
if number_of_ticket>999999 or number_of_ticket<100000:
    print("Некорректный ввод! Билет должен состоять из 6-ти цифр. Попробуйте снова.")
else:
    while first_half != 0:
        sum_first_half += first_half % 10
        first_half //= 10
    while second_half != 0:
        sum_second_half += second_half % 10
        second_half //= 10
    if sum_first_half == sum_second_half:
        print("Ура! Вам попался счастливый билет!")
    else:
        print("Вам выпал несчастливый билет! В следующий раз повезет!")
