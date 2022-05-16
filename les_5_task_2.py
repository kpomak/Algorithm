"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


import collections as cs

BASE = 16


def hex_sum(first_num, second_num, from_dec, to_dec):
    fst = first_num.copy()
    snd = second_num.copy()
    sum_hex = cs.deque(['0'])

    diff = len(fst) - len(snd)

    if diff < 0:
        fst, snd = snd, fst

    snd.extendleft(['0'] * abs(diff))

    for rank in range(len(snd)):
        rank_sum = to_dec[fst.pop()] + to_dec[snd.pop()] + to_dec[sum_hex[0]]
        sum_hex[0] = from_dec[rank_sum % BASE]
        sum_hex.appendleft('1' if rank_sum // BASE else '0')

    if sum_hex[0] == '0':
        sum_hex.popleft()

    return sum_hex


def hex_mult(first_num, second_num, from_dec, to_dec):
    if first_num == cs.deque('0') or second_num == cs.deque('0'):
        return cs.deque('0')  # исключает ответы ['0', '0', '0']

    fst = first_num.copy()
    mult_hex = cs.deque(['0'])

    for spam in range(len(fst)):
        buffer = 0
        operand = cs.deque('0' for _ in range(spam + 1))
        first_number = fst.pop()
        snd = second_num.copy()

        for egg in range(len(snd)):
            rank_mult = to_dec[first_number] * to_dec[snd.pop()] + buffer
            operand[0] = from_dec[rank_mult % BASE]
            buffer = rank_mult // BASE
            operand.appendleft('0')

        if buffer == 0:
            operand.popleft()
        else:
            operand[0] = from_dec[buffer]

        mult_hex = hex_sum(mult_hex, operand, from_dec, to_dec)

    return mult_hex


def hex_sum_mult_counter(first_num, second_num, from_dec, to_dec):

    def hex_counter(counter):
        result_queue = cs.deque()

        for shrubbery in range(len(counter) + 1):
            counter[shrubbery + 1] += counter[shrubbery] // BASE
            result_queue.appendleft(from_dec[counter[shrubbery] % BASE])

        if result_queue[0] == '0':
            result_queue.popleft()

        return result_queue

    first_queue, second_queue = first_num.copy(), second_num.copy()

    fst = cs.Counter()

    for spam in range(len(first_queue)):
        fst[spam] = to_dec[first_queue.pop()]

    snd = cs.Counter()

    for egg in range(len(second_queue)):
        snd[egg] = to_dec[second_queue.pop()]

    length_fst, length_snd = len(fst), len(snd)
    length = length_fst if length_fst >= length_snd else length_snd

    plus = cs.Counter()

    for rank in range(length):
        plus[rank] = fst[rank] + snd[rank]

    result_sum = hex_counter(plus)

    if first_num == cs.deque('0') or second_num == cs.deque('0'):
        result_mult = cs.deque('0')
    else:
        mult = cs.Counter()
        for rank_fst, number_fst in fst.items():
            for rank_snd, number_snd in snd.items():
                mult[rank_fst + rank_snd] += number_fst * number_snd

        result_mult = hex_counter(mult)

    result = (result_sum, result_mult)

    return result


dec_to_hex = cs.defaultdict(str)
for i in range(BASE):
    dec_to_hex[i] = f'{i:X}'

hex_to_dec = cs.defaultdict(int)  # Although this way may not be obvious at first unless you're Dutch. # tuple :-)
for key, value in dec_to_hex.items():
    hex_to_dec[value] = key

first = cs.deque(input('Введите первое число в шестнадцатиричном формате ').upper())
second = cs.deque(input('Введите второе число в шестнадцатиричном формате ').upper())

print('Cумма =', *hex_sum(first, second, dec_to_hex, hex_to_dec))
print('Произведение =', *hex_mult(first, second, dec_to_hex, hex_to_dec))

hex_sum_counter, hex_mult_counter = hex_sum_mult_counter(first, second, dec_to_hex, hex_to_dec)

print('Cумма =', *hex_sum_counter)
print('Произведение =', *hex_mult_counter)

"""
По результатам испытаний timeit и cProfile установлено, что независимо от длины перемножаемых чисел,
алгоритм с использованием словаря Counter выполняется примерно в три раза быстрее алгоритма, использующего только
очередь, за счет отсутствия многочисленных pop и appendleft'ов, создания копий объектов, а также нескончаемого перевода
из шестнадцатиричной в десятичную систему счисления и обратно.
"""