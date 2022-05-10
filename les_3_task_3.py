"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

# постановка задачи
from random import randint

SIZE = 20
LOW = 1
HIGH = 35
array = [randint(LOW, HIGH) for i in range(SIZE)]

# решение
max_idx, min_idx = 0, 0
for idx, num in enumerate(array):
    if array[max_idx] < num:
        max_idx = idx
    if array[min_idx] > num:
        min_idx = idx

# вывод
print(f'Исходный массив:\n{array}')
array[max_idx], array[min_idx] = array[min_idx], array[max_idx]
print(f'Максимальный и минимальный элементы на позициях {max_idx} и {min_idx} поменялись местами:\n{array}')
