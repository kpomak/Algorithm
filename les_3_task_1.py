"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

START_ARRAY = 2
STOP_ARRAY = 100
START_NUM = 2
STOP_NUM = 10

numbers = {}

for key in range(START_NUM, STOP_NUM):
    numbers[key] = 0

for num in range(START_ARRAY, STOP_ARRAY):
    for key in numbers:
        if num % key == 0:
            numbers[key] += 1

# второй вариант решения не самый точный

# array = [x for x in range(START_ARRAY, STOP_ARRAY)]
# length = len(array) + 1
# for key in range(START_NUM, STOP_NUM):
#     numbers[key] = length // key

# вывод результата
print(f'В диапазоне натуральных чисел от {START_ARRAY} до {STOP_ARRAY-1}')
for key, value in numbers.items():
    print(f'числу {key} кратно {value} из них')
