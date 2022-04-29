"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
from random import randint

# постановка задачи
M, N = 5, 4
LOW = -50
HIGH = 50
SPACER = 5

matrix = [[randint(LOW, HIGH) for j in range(N)] for i in range(M)]

# решение
min_array = matrix[0]
for row in matrix:  # проходим по первой строке только, чтобы не создавать в памяти новый объект через срез матрицы
    for column_idx, value in enumerate(row):
        if min_array[column_idx] > value:
            min_array[column_idx] = value

max_num = min_array[0]
for num in min_array[1:]:
    if max_num < num:
        max_num = num

# вывод
print('Исходная матрица:')
for i in matrix:
    for j in i:
        print(f'{j:>{SPACER}}', end='')
    print()
print(f'Минимальные элементы столбцов:\n{min_array}\n'
      f'максимальный из них {max_num}')



