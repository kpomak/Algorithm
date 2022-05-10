"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
# постановка задачи
from random import randint

SIZE = 15
LOW = -150
HIGH = 3550
array = [randint(LOW, HIGH) for i in range(SIZE)]

# решение
fst_min, snd_min = array[1], array[0]
for num in array:
    if num <= fst_min:
        fst_min = num
        if snd_min > fst_min:
            fst_min, snd_min = snd_min, fst_min

print(f'Исходный массив:\n{array}\nНаименьшее число {snd_min}\nВторое наименьшее {fst_min}')
