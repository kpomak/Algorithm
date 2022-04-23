"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def satan_sum(num):
    if num == 1:
        return 1
    return 1 - 0.5 * satan_sum(num - 1)


number = int(input('Ведите число элементов ряда '))
result = satan_sum(number)
print(result)
