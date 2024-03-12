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
vowels_in_word(number_vowels)
print(result(number_vowels))
