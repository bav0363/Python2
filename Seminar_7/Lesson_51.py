import random

print(my_list := [str(random.randint(10, 15)) for _ in range(15)])

func = lambda i: len(i) == len(my_list[0])
def some_by(func, my_list):
    if len(list(filter(func, my_list))) == len(my_list):
        return True
    return False

print(some_by(func, my_list))
