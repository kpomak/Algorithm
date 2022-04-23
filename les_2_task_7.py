"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def count(num):
    if num == 1:
        return num
    return num + count(num - 1)


number = int(input('Введите число элементов ряда '))
row_sum = count(number)
comp = number * (number + 1) / 2
if row_sum == comp:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')
