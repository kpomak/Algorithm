"""
Комментарии по коду решета можно посмотреть по ссылке:
https://garnet-spot-1fd.notion.site/GU_1911-deb3ff67f9c24b5ba16e102abf3b64d0

2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

- Первый — с помощью алгоритма «Решето Эратосфена».

- Второй — без использования «Решета Эратосфена».
"""

import math
import timeit as it
import cProfile

NUMBER = 1000


def sieve(n):  # Решето Эратосфена
    primes = {}

    def _sieve(start, stop):
        guesses = [i for i in range(start, stop + 1)]

        def __sieve(number, array):
            for element in array:
                guesses[element - start] = 0

            if array:
                primes[number] = array[-1]
            else:
                primes[number] = number * 2
            return

        for prime_num, last_comp in primes.items():
            if last_comp < start:
                composite = [i for i in range(last_comp + prime_num, stop + 1, prime_num)]
            else:
                composite = [i for i in range(prime_num * 2, stop + 1, prime_num)]
            __sieve(prime_num, composite)

        for guess in guesses:
            if guess:
                composite = [i for i in range(guess * 2, stop + 1, guess)]
                __sieve(guess, composite)

        start, stop = stop + 1, stop * 2
        return start, stop

    start_num, stop_num = 2, n * 2
    result = 'something went wrong'

    while len(primes) < n:
        start_num, stop_num = _sieve(start_num, stop_num)

    for idx, key in enumerate(primes.keys()):
        if idx == n - 1:
            result = key
    return result


def prime(n):  # Классический способ проверки числа на простоту
    prime_numbers = [2]

    def _prime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    guess = 3

    while len(prime_numbers) < n:
        if _prime(guess):
            prime_numbers.append(guess)
        guess += 1

    return prime_numbers[-1]


if __name__ == '__main__':
    # print(it.timeit('prime(10)', number=NUMBER, globals=globals()))  # 0.022297800052911043
    # print(it.timeit('prime(100)', number=NUMBER, globals=globals()))  # 0.5361093999817967
    # print(it.timeit('prime(1000)', number=NUMBER, globals=globals()))  # 11.625638600438833
    # print(it.timeit('prime(10_000)', number=NUMBER, globals=globals()))  # 272.549905099906
    # print(it.timeit('prime(100_000)', number=NUMBER, globals=globals()))  # 6109.297534400132

    # cProfile.run('prime(100_000)')

    """
    3999125 function calls in 5.713 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    5.713    5.713 <string>:1(<module>)
        1    0.456    0.456    5.712    5.712 les_4_task_2.py:64(prime)
  1299707    4.958    0.000    5.139    0.000 les_4_task_2.py:67(_prime)
        1    0.000    0.000    5.713    5.713 {built-in method builtins.exec}
  1299708    0.108    0.000    0.108    0.000 {built-in method builtins.len}
  1299707    0.181    0.000    0.181    0.000 {built-in method math.sqrt}
    99999    0.010    0.000    0.010    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """

    # print(it.timeit('sieve(10)', number=NUMBER, globals=globals()))  # 0.016346300020813942
    # print(it.timeit('sieve(100)', number=NUMBER, globals=globals()))  # 0.27287570014595985
    # print(it.timeit('sieve(1000)', number=NUMBER, globals=globals()))  # 2.5736964996904135
    # print(it.timeit('sieve(10_000)', number=NUMBER, globals=globals()))  # 53.67269179970026
    # print(it.timeit('sieve(100_000)', number=NUMBER, globals=globals()))  # 674.4045149995945

    # cProfile.run('sieve(100_000)')

    """
             473866 function calls in 0.836 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.836    0.836 <string>:1(<module>)
        1    0.018    0.018    0.830    0.830 les_4_task_2.py:21(sieve)
        4    0.212    0.053    0.812    0.203 les_4_task_2.py:24(_sieve)
        4    0.062    0.015    0.062    0.015 les_4_task_2.py:25(<listcomp>)
   236922    0.383    0.000    0.383    0.000 les_4_task_2.py:27(__sieve)
    61436    0.122    0.000    0.122    0.000 les_4_task_2.py:39(<listcomp>)
    54359    0.007    0.000    0.007    0.000 les_4_task_2.py:41(<listcomp>)
   121127    0.026    0.000    0.026    0.000 les_4_task_2.py:46(<listcomp>)
        1    0.000    0.000    0.836    0.836 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
    """

"""
Вывод: Эратосфен побеждает! Вычеркиваний надо меньше, чем проверок на простоту.

>>> from les_4_task_2 import prime, sieve
>>> sieve(2)
3
>>> prime(4)
7
"""
