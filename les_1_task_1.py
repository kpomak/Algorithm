"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

x = int(input('введите число от 100 до 999'))
a = x // 100
b = x % 100 // 10
c = x % 10
plus = a + b + c
comp = a * b * c
print(f'cумма цифр = {plus}\nпроизведение цифр = {comp}')
