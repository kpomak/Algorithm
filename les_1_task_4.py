"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
Написать программу, которая генерирует в указанных пользователем границах:
● случайное целое число,
● случайное вещественное число,
● случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import randint, uniform

print('Введите начало и конец диапазона')
start, stop = input(), input()
if start.isdigit():
    num = randint(int(start), int(stop))
elif start.isalpha():
    num = chr(randint(ord(start), ord(stop)))
else:
    num = uniform(float(start), float(stop))
print(num)
