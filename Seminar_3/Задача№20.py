
my_list = [{1:"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"}, {2:"D, G, Д, К, Л, М, П, У"},
            {3:"B, C, M, P, Б, Г, Ё, Ь, Я"}, {4:"F, H, V, W, Y, Й, Ы"}, {5:"K, Ж, З, Х, Ц, Ч"}, {8:"J, X, Ш, Э, Ю"},
            {10:"Q, Z, Ф, Щ, Ъ"}]

word = input("Введите слово: ")
word = word.upper()
score = 0

for i in range(len(word)):
    for j in my_list:
        for k in j.values():
            for n in range(len(k)):
                if word[i] == k[n]:
                    for key, item in j.items():
                        score += key
print(score)