import math


class1 = int(input("Кол-во учеников в первом классе: "))
class2 = int(input("Кол-во учеников во втором классе: "))
class3 = int(input("Кол-во учеников в третьем классе: "))
print(f"Необходимое кол-во парт: {math.ceil(class1/2) + math.ceil(class2/2) + math.ceil(class3/2)} ед.")