poryad_nomer = int(input("Порядковый номер от головы поезда: "))
nomer_vagona = int(input("Номер вагона: "))
if poryad_nomer < nomer_vagona:
    print("Кол-во вагонов в электричке составляет: ", nomer_vagona + poryad_nomer - 1)
elif poryad_nomer > nomer_vagona:
    print("Кол-во вагонов в электричке составляет: ", poryad_nomer + nomer_vagona - 1)
else:
    print("Для решения недостаточно данных")


