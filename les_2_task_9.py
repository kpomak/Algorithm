"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def check(num, value=0):
    if not num:
        return value
    value += num % 10
    return check(num // 10, value)


def counter(biggest=0, row_sum=0):
    target = int(input())
    if target == 0:
        return biggest, row_sum
    attempt = check(target)
    if attempt > row_sum:
        row_sum, biggest = attempt, target
    return counter(biggest, row_sum)


print('Вводите натуральные числа, чтобы выйти — 0')
number, count = counter()
print(f'Число {number} с наибольшей суммой цифр {count}')
