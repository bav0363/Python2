# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть

# quantity = int(input("Сколько монеток лежит на столе? "))
# count = 1
# num_0 = 0
# num_1 = 0
# while count <= quantity:
#     num = int(input(f"Какое положение у {count} монетки? "))
#     if num == 0:
#         num_0 += 1
#         count += 1
#     else:
#         num_1 += 1
#         count += 1
# if num_1 >= num_0:
#     print(f"Нужно перевернуть {num_0} монетки со значением 0")
# else:
#     print(f"Нужно перевернуть {num_1} монетки со значением 1")



coins = [0, 1, 0, 0, 1, 0]

num_0 = 0
num_1 = 0

for i in coins:
    if i == 0:
        num_0 += 1
    else:
        num_1 += 1
print(min(num_0,num_1))






