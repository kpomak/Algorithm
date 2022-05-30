"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""


from random import randint, shuffle


LOW = -100
HIGH = 100


def dwarf_median_sort(array):
    i = 1
    while i < len(array):
        if array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
            if i == 0:
                i += 1
        else:
            i += 1
    return array[len(array) // 2]


def quick_median_find(array):
    found_idx = len(array) // 2

    def max_recursion_depth_emergency_exit_with_dwarfs_help(start, stop):
        print(f'Здесь были гномы!!!')
        i = start + 1
        while i <= stop:
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                i -= 1
                if i == start:
                    i += 1
            else:
                i += 1
        return array[found_idx]

    def quick_find_like_tony_hoare(start=0, stop=None, flag=False):
        if start == stop:
            return array[found_idx]
        if flag and array[start] == array[stop]:
            return max_recursion_depth_emergency_exit_with_dwarfs_help(start, stop)

        pivot = array[randint(start, stop)]
        i, j = start, stop
        while i <= j:
            while array[i] <= pivot:
                if i == stop:
                    break
                i += 1
            while array[j] > pivot:
                j -= 1
            if i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
            if i == stop:
                break

        if i == j == stop:
            flag = True
            return quick_find_like_tony_hoare(start, stop, flag)
        if found_idx > j:
            return quick_find_like_tony_hoare(i, stop, flag)
        elif found_idx <= j:
            return quick_find_like_tony_hoare(start, j, flag)

    return quick_find_like_tony_hoare(stop=len(array) - 1)


m = int(input('Введите натуральное число: '))
data = [randint(LOW, HIGH) for _ in range(2 * m + 1)]
print('Исходный массив:\n', data)
print('Медиана:', quick_median_find(data))
print(f'Массив после нахождения {m + 1}-го минимального элемента, спасибо Хоару:\n', data)
shuffle(data)
print('Медиана гномов:', dwarf_median_sort(data))
print('Отсортированный гномами массив:\n', data)


