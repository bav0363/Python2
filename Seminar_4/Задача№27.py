import re

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea " \
#        "shells on the sea shore I'm sure that the shells are sea shore shell"
# text = text.upper()
# my_list = re.split("[ .]", text) # Разбивает text по заданному условию
# print(my_list)
# print(set(my_list))
# print(len(set(my_list)))

from string import punctuation

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea " \
       "shells on the sea shore I'm sure that the shells are sea shore shell"
for ch in punctuation:
       text = text.replace(ch, " ")
print(text)
my_list = text.lower().split() # Разбиваем текст на слова (по пробелам) и переводим все в нижний регистр
print(my_list)
print(set(my_list))
print(len(set(my_list)))