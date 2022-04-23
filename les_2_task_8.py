"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
8. Посчитать, сколько раз встречается определенная цифра во введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def check(num, row, value=0):
    if not row:
        return value
    if row % 10 == num:
        value += 1
    return check(num, row // 10, value)


def counter(n, num, match=0):
    if n == 0:
        return match
    target = int(input())
    match += check(num, target)
    return counter(n - 1, num, match)


count, number = int(input('Введите количество чисел и цифру, которую будем в них искать ')), int(input())
print('Вводите числа')
result = counter(count, number)
print(f'Цифра {number} встретилась {result} раз')
