"""
2) Закодируйте любую строку по алгоритму Хаффмана.
Превратите строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
"""
from collections import Counter
from operator import attrgetter


class MyNode:
    def __init__(self, weight=None, symbol=None, left=None, right=None):
        self.weight = weight
        self.symbol = symbol
        self.left = left
        self.right = right

    @staticmethod
    def create_tree(text):
        text_count = Counter(text)
        nodes = []
        for character, frequency in text_count.items():
            nodes.append(MyNode(weight=frequency, symbol=character))

        while len(nodes) > 1:
            nodes.sort(key=attrgetter('weight'), reverse=True)
            fst = nodes.pop()
            snd = nodes.pop()
            nodes.append(MyNode(weight=(fst.weight + snd.weight), left=fst, right=snd))
        return nodes[0]


def get_code(tree, text):
    crypto_table = {}

    def find_letter_code(sub_tree, char, sym_code=''):
        if char == sub_tree.symbol:
            crypto_table[char] = f'{sym_code}'
            return crypto_table[char]
        if sub_tree.left is not None:
            return f'{find_letter_code(sub_tree.left, char, sym_code=f"{sym_code}0")}' \
                   f'{find_letter_code(sub_tree.right, char, sym_code=f"{sym_code}1")}'
        else:
            return f''

    code = []
    for i in range(len(text)):
        character = text[i]
        code.append(crypto_table[character] if character in crypto_table else find_letter_code(tree, character))
    return crypto_table, code


def decode(crypto_table, code):
    binary_input = ''.join(code)
    decode_table = {number: letter for letter, number in crypto_table.items()}
    text = []
    number = ''
    for i in range(len(binary_input)):
        number = f'{number}{binary_input[i]}'
        if number in decode_table:
            text.append(decode_table[number])
            number = ''
    return ''.join(text)


message = input('Введите строку для кодирования ')
huffman_tree = MyNode.create_tree(message)
table, binary_output = get_code(huffman_tree, message)
print('Таблица кодирования:')
for key, value in table.items():
    print(f"'{key}': {value}")
print(f'Закодированная строка:', *binary_output)
print(f'Декодированная строка: {decode(table, binary_output)}')
