import math
print('========================================')
print('Лабораторна робота №1')
print('Програмування лінійних алгоритмів')
print('Автор: Олійник Артем, КМ-91 (16 варіант)')
print('========================================')
print("Обчислити тривалість року на двох планетах по введеним їх радіусів орбіт і швидкості руху по орбітах.")
print("З'ясувати, чи правда, що рік на першій планеті довший, ніж на другий.")
print("Тривалість року обчислюється за формулою: 2 * радіус_орбіти * ¶ / орбітальна_швидкість.")
while True:
    while True:
        try:
            r1 = float(input("Введіть значення для r1="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            v1 = float(input("Введіть значення для v1="))
            if v1 != 0:
                break
            else:
                print("Введіть число яке не дорівнює 0")
        except ValueError:
            print("Введіть число яке не дорівнює 0")
    while True:
        try:
            r2 = float(input("Введіть значення для r2="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            v2 = float(input("Введіть значення для v2="))
            if v2 != 0:
                break
            else:
                print("Введіть число яке не дорівнює 0")
        except ValueError:
            print("Введіть число яке не дорівнює 0")
    f1=2*r1*math.pi/v1
    f2=2*r2*math.pi/v2
    if f1 > f2:
        print("Рік на першій планеті довший")
    if f2 > f1:
        print("Рік на другій планеті довший")
    if f2 == f1:
        print("Роки будуть однакові")
    print("========================================")