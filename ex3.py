"""
Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar
ou par.
"""

from os import system

def impar_par(n:int) -> str:
    """Impar ou Par.

    Args:
        n (int): _description_

    Returns:
        str: _description_
    """
    return 'O numero e IMPAR' if n%2 == 1 else 'O numero e PAR'


if __name__ == '__main__':
    while True:
        system('cls')
        _n = input('Digite o numero: ')
        if _n.isnumeric():
            print(impar_par(int(_n)))
            break
