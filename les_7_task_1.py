"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""


from random import randint


SIZE = 10
LOW = -100
HIGH = 99


def bubble_reverse_sort(array):
    i = 1
    while True:
        flag = False
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break
        i += 1
    return i


data = [randint(LOW, HIGH) for _ in range(SIZE)]
print(f'Исходный массив:\n{data}')
print(f'Отсортированный за {bubble_reverse_sort(data)} пузырьков массив:\n{data}')
