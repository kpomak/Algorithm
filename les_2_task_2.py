"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
и 2 нечетные (3 и 5).
"""


def odd_even(num, odd=0, even=0):
    if not num:
        return odd, even
    if num % 10 % 2 == 0:
        return odd_even(num // 10, odd, even + 1)
    else:
        return odd_even(num // 10, odd + 1, even)


number = int(input('Введите натуральное число '))
odd_count, even_count = odd_even(number)
print(f'нечетных {odd_count}\nчетных {even_count}')
