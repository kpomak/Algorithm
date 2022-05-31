"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""


def sub_string(phrase):
    checked = set()
    for i in range(1, len(phrase)):
        for j in range(len(phrase) - i + 1):
            checked.add(hash(phrase[j:j + i]))
    return f'{len(checked)}'


print(sub_string('papa'))
print(sub_string('sova'))
