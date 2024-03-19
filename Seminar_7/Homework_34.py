# Функция для подсчета гласных в каждом слове
def vowels_in_word(my_list):
    for i in poem:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        number_vowels.append(count)
    return number_vowels


# Функция для проверки правила рифмы
def result(my_list):
    for i in range(1, len(my_list)):
        if my_list[0] != my_list[i]:
            return 'Пам парам'
    return 'Парам пам-пам'


vowels = 'ауоыэяюёие'  # Все гласные в алфавите
poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'  # Строка для проверки на рифму
list_poem = poem.split()
number_vowels = []
vowels_in_word(list_poem)
print(result(number_vowels))

# Для автотеста

def vowels_in_word(list_poem):
    for i in list_poem:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        number_vowels.append(count)
    return number_vowels

def result(my_list):
    if len(my_list) <= 1:
        return 'Количество фраз должно быть больше одной!'
    for i in range(1, len(my_list)):
        if my_list[0] != my_list[i]:
            return 'Пам парам'
    return 'Парам пам-пам'

vowels = 'ауоыэяюёие'  # Все гласные в алфавите
list_poem = stroka.split()
number_vowels = []
vowels_in_word(list_poem)
print(result(number_vowels))

Решение предлагаемое автотестом

vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))

 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')
