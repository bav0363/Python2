# text = "aaabcaadcdd"
# print(text)
#
# print(list := [ text[i] for i in range(len(text))])
# for i in range(len(list)):
#     count = 0
#     for j in range(i + 1, len(list)):
#         if list[j] == list[i]:
#             count += 1
#             list[j] = "{}{}{}".format(list[j], "_", count)
# print(list)
# text ="".join(list)
# print(text)

# from string import ascii_uppercase
# from random import choice
#
# new_str = "".join([choice(ascii_uppercase + "123456789") for _ in range(10)])
# print(new_str)
#
# dict_count = {}
# new_list = []
# for i in new_str:
#     dict_count[i] = dict_count.get(i, 0) + 1  # Если ключ не найден, то 0, если найден, то увеличиваем на 1 значение
#     if dict_count.get(i) > 1:
#         new_list.append(f"{i}_{dict_count.get(i) - 1}") # Если такой ключ ранее уже был, то присваиваем запись
#     else:
#         new_list.append(i)
# print(dict_count)
# print(new_list)

from string import ascii_uppercase
from random import choice

new_str = "".join([choice(ascii_uppercase + "123456789") for _ in range(10)])
print(new_str)

dict_count = {}
for i in new_str:
    dict_count[i] = dict_count.get(i, 0) + 1  # Если ключ не найден, то 0, если найден, то увеличиваем на 1 значение
    if dict_count.get(i) > 1:
        print(f"{i}_{dict_count.get(i) - 1}", end=" ")  # Если такой ключ ранее уже был, то присваиваем запись
    else:
        print(i, end=" ")

print("F", "S", "D", "I", 7, "B", "M", "E", "E_1", "C", sep="!\n\n ", end="!")
