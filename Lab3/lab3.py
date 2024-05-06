import math


first_katet = int(input(" Длина первого катета: "))
second_katet = int(input(" Длина второго катета: "))


gipotenusa = math.sqrt(first_katet**2 + second_katet**2)
perimeter = first_katet + second_katet + gipotenusa
area = 0.5 * first_katet * second_katet

print("\n Введенные значения:")
print("Длина первого катета:", first_katet)
print("Длина второго катета:", second_katet)

print("\n Результаты:")
print("Длина гипотенузы:", round(gipotenusa, 2))
print("Периметр:", round(perimeter, 2))
print("Площадь:", round(area, 2))