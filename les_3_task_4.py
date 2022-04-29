"""
Определить, какое число в массиве встречается чаще всего.
"""

# постановка задачи
from random import randint

SIZE = 33
LOW = 1
HIGH = 19
array = [randint(LOW, HIGH) for i in range(SIZE)]

# решение
counter = {num: 0 for num in set(array)}

for num in array:
    counter[num] += 1

max_key = array[0]

for key, value in counter.items():
    if counter[max_key] < value:
        max_key = key

# вывод
print(f"Исходный список:\n{array}")
for key, value in counter.items():
    print(f'Число {key} встретилось {value} раз')
print(f"Чаще всего встречается число {max_key}")
