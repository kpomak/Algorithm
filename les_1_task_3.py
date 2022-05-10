"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
По введенным пользователем координатам двух точек вывести уравнение прямой
вида y = kx + b, проходящей через эти точки.
"""
print('Введите координаты двух точек x1, y1, x2, y2')
x1 = float(input('x1 '))
y1 = float(input('y1 '))
x2 = float(input('x2 '))
y2 = float(input('y2 '))
if x1 == x2:
    print(f'x = {x1:g}')
elif y1 == y2:
    print(f'y = {y1:g}')
else:
    k = (y2-y1)/(x2 - x1)
    b = y1 - k * x1
    print(f'y = {k:.2g}x {b:=+{len(str(abs(b // 1)))}.2g}')

