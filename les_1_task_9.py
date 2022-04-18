"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a, b, c = int(input('Ведите три числа')), int(input()), int(input())
if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
elif a > c:
    print(a)
elif b > c:
    print(c)
else:
    print(b)
