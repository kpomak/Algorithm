"""
https://drive.google.com/file/d/1o-V4GKe6fFn1TsYXTVORh3x-jHYjcgIE/view?usp=sharing
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def unicode(start, stop, turn=0):
    if start == stop:
        return f'{stop}: {chr(stop)}'
    if turn < 9:
        return f'{start}: {" " if len(str(start)) < 3 else ""}{chr(start)} | {unicode(start + 1, stop, turn + 1)}'
    return f'{start}: {chr(start)}\n{unicode(start + 1, stop)}'


begin, end = 32, 127
print(unicode(begin, end))

