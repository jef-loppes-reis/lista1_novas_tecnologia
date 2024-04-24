"""Melhore o programa anterior, permitindo a entrada de números com
quaisquer dígitos."""


from re import sub
from os import system


def split_list_num(num:str) -> str:
    """Faz um slice em cima de um numero.

    Args:
        num (str): _description_

    Returns:
        str: _description_
    """
    return sub(r"\[|\]|\'|\,",'', str([x for x in num]))


if __name__ == '__main__':
    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            print(f'Separação dos numeros: {split_list_num(n)}')
            break
