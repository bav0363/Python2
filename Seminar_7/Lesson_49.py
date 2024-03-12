import math
import random
from random import randint

# Решение преподавателя - эталон
print(my_list := [(random.randint(2,15), random.randint(2,15)) for _ in range(15)])
my_list = list(filter(lambda i: i[0] != i[1], my_list))
print(max(my_list, key=lambda i: i[0] * i[1]))


# Мое решение
# print(my_list := [(tuple(random.randint(2, 15) for _ in range(2))) for _ in range(15)])
# print(my_list1 := list(filter(lambda i: i[0] != i[1], my_list)))
# print(my_list2 :=sorted(list(map(lambda i: int(math.pi * i[0] * i[1]), my_list1))))
# print(my_list3 := [item for item in my_list1 if int(item[0] * item[1] * math.pi) == my_list2[-1]])

# Решение в группе
# print(my_list := [(tuple(random.randint(2, 15) for _ in range(2))) for _ in range(15)])
# print(my_list1 := sorted(list(filter(lambda i: i[0] != i[1], my_list)), key=lambda i: int(math.pi * i[0] * i[1])))
# print(my_list1[-1])