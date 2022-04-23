"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def invert(num, start=True):
    if not num:
        return f''
    if num % 10 == 0 and start:
        return invert(num // 10)
    return f'{num % 10}{invert(num // 10, False)}'


number = int(input('Введите натуральное число '))
result = invert(number)
print(result)

