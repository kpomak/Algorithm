"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


from random import random


SIZE = 10
HIGH = 50


def merge_sort(array):

    def extend(_result, pos, last):
        for i in range(pos, last + 1):
            _result.append(array[i])
            pos += 1
        return

    def _merge_sort(start=0, end=None):
        if end == start:
            return

        half_end = (end + start) // 2
        half_start = half_end + 1
        _merge_sort(start, half_end)
        _merge_sort(half_start, end)
        result = []
        i, j = start, half_start

        while i <= half_end and j <= end:
            if array[i] >= array[j]:
                result.append(array[j])
                j += 1
            else:
                result.append(array[i])
                i += 1

        extend(result, i, half_end)
        extend(result, j, end)

        for i in range(start, end + 1):
            array[i] = result[i - start]
        return

    _merge_sort(end=len(array) - 1)
    return


data = [HIGH * random() for _ in range(SIZE)]
print('Исходный массив:', *data, sep='\n')
print("(• )( •)  " * 2)
merge_sort(data)
print('Отсортированный массив:', *data, sep='\n')
