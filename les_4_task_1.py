"""
График зависимости времени выполнения кода от размера матрицы можно посмотреть по ссылке:
https://docs.google.com/spreadsheets/d/11nKoWc5kFYiHMqTYhY2rx-9_UOXpKQuontr07ljsxK0/edit?usp=sharing

1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Задача 3.9
Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Для удобства рассмотрим квадратную матрицу
"""
import numpy as np
import timeit as it
from random import randint
from cProfile import run


# постановка задачи

NUMBER = 1000
M = N = 5000
LOW = -50
HIGH = 50

matrix = [[randint(LOW, HIGH) for j in range(N)] for i in range(M)]

# решение 1

block_1 = """
min_array = matrix[0]
for row in matrix:
    for column_idx, value in enumerate(row):
        if min_array[column_idx] > value:
            min_array[column_idx] = value

max_num = min_array[0]
for num in min_array:
    if max_num < num:
        max_num = num
"""

# решение 2

block_2 = """
length_row, length_column = len(matrix[0]), len(matrix)
min_array = []
column = 0
while column < length_column:
    min_value = matrix[0][column]
    row = 1
    while row < length_row:
        if min_value > matrix[row][column]:
            min_value = matrix[row][column]
        row += 1
    min_array.append(min_value)
    column += 1

max_num = min_array[0]
_ = 1
while _ < length_column:
    if max_num < min_array[_]:
        max_num = min_array[_]
    _ += 1
"""

# решение 3

block_3 = """
max_num = max([min(row) for row in np.array(matrix).transpose()])
"""

# print(it.timeit(block_1, number=NUMBER, globals=globals()))  # M = N = 10           0.006044699810445309
# print(it.timeit(block_1, number=NUMBER, globals=globals()))  # M = N = 100          0.48360380018129945
# print(it.timeit(block_1, number=NUMBER, globals=globals()))  # M = N = 250          2.8275417000986636
# print(it.timeit(block_1, number=NUMBER, globals=globals()))  # M = N = 500          12.433946599718183
# print(it.timeit(block_1, number=NUMBER, globals=globals()))  # M = N = 1000         54.91858739964664

# print(it.timeit(block_2, number=NUMBER, globals=globals()))  # M = N = 10           0.00823769997805357
# print(it.timeit(block_2, number=NUMBER, globals=globals()))  # M = N = 100          0.7266612001694739
# print(it.timeit(block_2, number=NUMBER, globals=globals()))  # M = N = 250          4.998685299884528
# print(it.timeit(block_2, number=NUMBER, globals=globals()))  # M = N = 500          21.769094599876553
# print(it.timeit(block_2, number=NUMBER, globals=globals()))  # M = N = 1000         96.07811819994822

# print(it.timeit(block_3, number=NUMBER, globals=globals()))  # M = N = 10           0.020977700129151344
# print(it.timeit(block_3, number=NUMBER, globals=globals()))  # M = N = 100          1.0872033000923693
# print(it.timeit(block_3, number=NUMBER, globals=globals()))  # M = N = 250          6.473594699986279
# print(it.timeit(block_3, number=NUMBER, globals=globals()))  # M = N = 500          25.492315500043333
# print(it.timeit(block_3, number=NUMBER, globals=globals()))  # M = N = 1000         103.42736209975556

# run(block_1)  # M = N = 5000

"""
         3 function calls in 2.930 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    2.929    2.929    2.929    2.929 <string>:1(<module>)
        1    0.000    0.000    2.930    2.930 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# run(block_2)  # M = N = 5000

"""
         5005 function calls in 4.668 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    4.667    4.667    4.668    4.668 <string>:1(<module>)
        1    0.000    0.000    4.668    4.668 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     5000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# run(block_3)  # M = N = 5000

"""
         5007 function calls in 2.615 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    2.614    2.614 <string>:1(<module>)
        1    0.002    0.002    1.098    1.098 <string>:2(<listcomp>)
        1    0.000    0.000    2.615    2.615 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     5000    1.095    0.000    1.095    0.000 {built-in method builtins.min}
        1    1.510    1.510    1.510    1.510 {built-in method numpy.array}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}
"""

"""
Выводы:
В первом способе я использовал цикл for и функцию enumerate для прохода по столбцам матрицы,
во втором прошелся по матрице циклом while и обращался к элементам по индексам,
в третьем способе импортировал крутой модуль numpy для транспонирования матрицы и использовал функции min и max.

Из сProfile видно, что при третьем способе больше половины работы скрипта тратится на преобразование массива в матрицу,
в первых двух способах каких-то конкретных "узких" мест не обнаружено.

timeit свидетельствует от том, что все три функции на заданном участке входных данных имеют асимптотику О(N**2),
вероятно, из-за роста матрицы пропорционально N**2, при M = N. Цикл for работает очевидно быстрее цикла while.
В третьем способе долго реализуется транспонирование матрицы
"""
