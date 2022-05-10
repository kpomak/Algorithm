"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

# постановка задачи
M, N = 5, 4
SPACER = 4
matrix = [[0 for j in range(N)] for i in range(M)]

# решение
row = len(matrix)
column = len(matrix[0]) - 1

for i in range(row):
    row_sum = 0
    for j in range(column):
        matrix[i][j] = int(input(f'Введите элемент {i + 1} строки {j + 1} столбца '))
        row_sum += matrix[i][j]
    matrix[i][column] = row_sum

# вывод
print('Полученная матрица:')
for i in matrix:
    for j in i:
        print(f'{j:>{SPACER}}', end='')
    print()



