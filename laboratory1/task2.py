print('========================================')
print('Лабораторна робота №1')
print('Програмування лінійних алгоритмів')
print('Автор: Олійник Артем, КМ-91 (16 варіант)')
print('========================================')
print("Скласти програму, що визначає, чи пройде графік функції у = ах2 + b х + с")
print("через задану з клавіатури точку з координатами (t, n).")
while True:
    while True:
        try:
            a = float(input("Введіть значення для a="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            b = float(input("Введіть значення для b="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            c = float(input("Введіть значення для c="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            t = float(input("Введіть значення для t="))
            break
        except ValueError:
            print("Введіть число")
    while True:
        try:
            n = float(input("Введіть значення для n="))
            break
        except ValueError:
            print("Введіть число")
    y=float(a*n*n+b*n+c)
    if y==t:
        print("Графік перетинає точку")
    else: print("Графік не перетинає точку")
    print("========================================")