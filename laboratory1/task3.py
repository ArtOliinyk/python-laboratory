print('========================================')
print('Лабораторна робота №1')
print('Програмування лінійних алгоритмів')
print('Автор: Олійник Артем, КМ-91 (16 варіант)')
print('========================================')
print('Обчислити функцію')
while True:
    while True:
        try:
            x = float(input("Введіть значення для x="))
            break
        except ValueError:
            print("Введіть число")
    if x<3.2:
        y=pow(x,4) + 9
    else:
        if (-5*pow(x,2)+7)!=0:
            y=round((54*pow(x,4))/(-5*pow(x,2)+7), 3)
        else:
            print("Помилка: Діленння на 0")
    print(y)
    print("========================================")