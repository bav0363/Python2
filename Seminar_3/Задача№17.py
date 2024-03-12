# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# print(list := [random.randint(0, 5) for _ in range(int(input("Введите размер списка: ")))])
# print(list)
# print(set(list))
# print(len(set(list)))

from random import  randint

list = []
res = []
size = int(input("Какой будет размер списка? "))
for i in range(size):
    list.append(randint(0, 5))
print(*list)

for i in range(len(list)):
    if res.count(list[i]) < 1:
        res.append(list[i])
print(*res)
print(len(res))



