a = float(input('Введите коэффициент a: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))


if a != 0:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('Корней нет!')
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        if x1==x2:
            print('Уравнение имеет только один корень х = ', x1)
        else:
            print(f'У уравнения 2 корня:\n х1 = {x1}\n и х2 = {x2}')

else:
    x = -c / b
    print('Уравнение имеет только один корень х = ', x)