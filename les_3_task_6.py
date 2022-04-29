"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

# постановка задачи
from random import randint

SIZE = 10
LOW = -5
HIGH = 5
array = [randint(LOW, HIGH) for i in range(SIZE)]


# решение
max_idx, min_idx, result = 0, 0, 0

for idx, num in enumerate(array):
    if array[max_idx] < num:
        max_idx = idx
    if array[min_idx] > num:
        min_idx = idx

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

for num in array[min_idx + 1: max_idx]:
    result += num

# вывод
print(f'В исходном массиве:\n{array}\nсумма чисел между элементами '
      f'{array[min_idx]} и {array[max_idx]} равна {result}')