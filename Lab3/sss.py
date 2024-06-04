import math

while True:
    try:
        katet1 = int(input("Введите длину первого катета: "))
        katet2 = int(input("Введите длину второго катета: "))
        
        if katet1 <= 0 or katet2 <= 0:
            print("Ошибка! Введите положительные значения.")
            continue
    except ValueError:
        print("Ошибка! Введите целое число.")
        continue

    # Расчет гипотенузы, периметра и площади
    hypotenuse = math.sqrt(katet1**2 + katet2**2)
    perimeter = katet1 + katet2 + hypotenuse
    area = 0.5 * katet1 * katet2

    # Вывод результатов с округлением до 2 знаков после запятой
    print(f"Длина первого катета: {katet1}")
    print(f"Длина второго катета: {katet2}")
    print(f"Длина гипотенузы: {hypotenuse:.2f}")
    print(f"Периметр треугольника: {perimeter:.2f}")
    print(f"Площадь треугольника: {area:.2f}")
    
    break