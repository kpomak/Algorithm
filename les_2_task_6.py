"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
 Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
from random import randint


def game(num, turn=1):
    if turn < 11:
        attempt = int(input(f'Попытка № {turn}\nВаше число '))
        if attempt == num:
            return f'Победа!'
        if num > attempt:
            print('Ваше число меньше')
        else:
            print('Ваше число больше')
        return game(num, turn + 1)
    return f'Это число {num}'


print('Отгадайте число от 1 до 100')
number = randint(0, 100)
result = game(number)
print(result)
