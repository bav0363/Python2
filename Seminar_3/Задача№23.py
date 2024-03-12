# import random
# from random import  randint
#
# print(list := [random.randint(0, 10) for _ in range(int(input("Введите размер списка: ")))])
# count = 0
# list_2 = []
# print(len([i for i in range(1, len(list)) if list[i-1] < list[i]]))

count = 0
i = 1
while i < len(list):
    if list[i] > list[i-1]:
        count += 1
    i += 1
print((count))

# for i in range(1, len(list)):
#      if list[i-1] < list[i]:
#          count += 1
# print(count)


