"""
https://drive.google.com/file/d/1-GlcAj_5ueNNvRu9LU5NQFE294QR-3Ix/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
fst, snd = input('введите две буквы '), input()
fst_place = ord(fst) - 96
snd_place = ord(snd) - 96
symbol_space = abs(fst_place - snd_place) - 1
print(f'номер в алфавите первого символа - {fst_place},'
      f'второго - {snd_place},количество букв между ними - {symbol_space}')
