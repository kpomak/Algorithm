"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти (укажите какую задачу вы взяли в комментарии);
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный по суммарной затраченной памяти;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.

Python 3.10.2 x64
Windows 10 Pro 20H2 x64

Задача 3.7:
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import sys
import collections as cs
import numpy as np
from random import randint


def size(**kwargs):
    checked_id = []

    def catch_if_not_already_checked(element):
        element_id = id(element)
        if element_id in checked_id:
            return 0
        checked_id.append(element_id)
        return sys.getsizeof(element)

    def _size(*args):
        result = 0
        for data in args:
            if hasattr(data, '__iter__'):
                items_sum = 0
                if hasattr(data, 'items'):
                    items_sum = sum([_size(key, value) for key, value in data.items()])
                elif not isinstance(data, (range, enumerate, str)):
                    items_sum = sum([_size(item) for item in data])
                return catch_if_not_already_checked(data) + items_sum
            result += catch_if_not_already_checked(data)
        return result

    return sum([_size(data_item) for data_item in kwargs.values()])


# решение 1
def func_list(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 1:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 2
def func_tuple(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 2:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 3
def func_set(array):
    fst_min, snd_min = array.pop(), array.pop()
    array.add(fst_min)
    array.add(snd_min)
    for i in array:
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        min_values = fst_min, snd_min
        if i < fst_min and i not in min_values:
            fst_min = i
    # print(f'Решение 3:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 4
def func_frozenset(array):
    fst_min, snd_min = next(iter(array)), next(iter(array))
    for i in array:
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        min_values = fst_min, snd_min
        if i < fst_min and i not in min_values or fst_min == snd_min:
            fst_min = i
    # print(f'Решение 4:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 5
def func_deque(array):
    queue = array.copy()  # создаем копию, чтобы не обращаться по индексам, а делать pop()
    fst_min, snd_min = queue.pop(), queue.pop()
    for i in range(len(queue)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        num = queue.pop()
        if num <= fst_min:
            fst_min = num
    queue = array.copy()  # создаем копию для оценки использованной памяти
    # print(f'Решение 5:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 6
def func_dict(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 6:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


#  решение 7
def func_defaultdict(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 7:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 8
def func_counter(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 8:\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# решение 9
def func_numpy(array):
    fst_min, snd_min = array[0], array[1]
    for i in range(2, len(array)):
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min
        if array[i] <= fst_min:
            fst_min = array[i]
    # print(f'Решение 9 :\nмассив {array}')
    # print(f'наименьшие числа {snd_min} {fst_min}')
    variables = locals()
    return variables


# постановка задач
SIZE = 10_000
LOW = SIZE * -100_000  # изменяя значения LOW и HIGH помни про solution_3 (HIGH - LOW > SIZE)
HIGH = SIZE * 100_000
num_array = [randint(LOW, HIGH) for i in range(SIZE)]

solution_1 = num_array
solution_2 = tuple(num_array)
solution_3 = set(num_array)
while len(solution_3) < SIZE:
    solution_3.add(randint(LOW, HIGH))
solution_4 = frozenset(solution_3)
solution_5 = cs.deque(num_array)
solution_6 = {key: value for key, value in enumerate(num_array)}
solution_7 = cs.defaultdict(int, solution_6)
solution_8 = cs.Counter(solution_6)
solution_9 = np.array(num_array)

# решение
print('Использование памяти при решении задачи 3.7 в зависимости от типа данных: ')
print(f'{str(type(solution_1)):<40}{size(**func_list(solution_1))} байт')
print(f'{str(type(solution_2)):<40}{size(**func_tuple(solution_2))} байт')
print(f'{str(type(solution_3)):<40}{size(**func_set(solution_3))} байт')
print(f'{str(type(solution_4)):<40}{size(**func_frozenset(solution_4))} байт')
print(f'{str(type(solution_5)):<40}{size(**func_deque(solution_5))} байт')
print(f'{str(type(solution_6)):<40}{size(**func_dict(solution_6))} байт')
print(f'{str(type(solution_7)):<40}{size(**func_defaultdict(solution_7))} байт')
print(f'{str(type(solution_8)):<40}{size(**func_counter(solution_8))} байт')
print(f'{str(type(solution_9)):<40}{size(**func_numpy(solution_9))} байт')

"""
<class 'list'>                          365204 байт
<class 'tuple'>                         360068 байт
<class 'set'>                           804560 байт
<class 'frozenset'>                     804560 байт
<class 'collections.deque'>             363644 байт без создания копии объекта, а с копией - 446012 байт
<class 'dict'>                          855024 байт
<class 'collections.defaultdict'>       855032 байт
<class 'collections.Counter'>           855040 байт
<class 'numpy.ndarray'>                 320196 байт контейнер небольшой, но сохраняет одинаковые объекты под разными id


По результатам измерений c указанными исходными данными победил numpy.ndarray,
однако, возникают сомнения в достоверности расчета используемой им памяти.

Результаты в турнирной таблице представлены для массивов размером 10_000 элементов:

1. место - tuple
2. место - deque без создания копий
3. место - list
4. место - deque c созданием копии
5. место - {set, frozenset}
6. место - dict
7. место - defaultdict
8. место - Counter

numpy.ndarray - дисквалификация
"""
