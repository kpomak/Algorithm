"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

# постановка задачи
from random import randint

SIZE = 15
LOW = -20
HIGH = 20
array = [randint(LOW, HIGH) for i in range(SIZE)]

# решение
flag, idx = False, 0
for i, value in enumerate(array):
    if value < 0 and not flag:
        idx = i
        flag = True
    elif array[idx] < value < 0:
        idx = i

# вывод
print(f'Исходный массив:\n{array}')
if not flag:
    print(f'В массиве нет отрицательных чисел')
else:
    print(f'Mаксимальный отрицательный элемент {array[idx]} на {idx} месте')

