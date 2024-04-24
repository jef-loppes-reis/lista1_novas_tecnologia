"""Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção saída seja escolhida."""

from os import system


def soma(n1:int, n2:int) -> int:
    """Soma

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    return n1 + n2


def subtracao(n1:int,  n2:int) -> int:
    """Subtração

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    return n1 - n2


def mult(n1:int, n2:int) -> int:
    """Multiplicação

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    return n1*n2


def div(n1:int, n2:int) -> int:
    """Divisão

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    return n1/n2


def menu() -> None:
    """_summary_
    """
    print('''
    [1] - Adição
    [2] - Subtração
    [3] - Divisão
    [4] - Multiplicação''')


if __name__ == '__main__':
    while True:
        system('cls')
        menu()
        op = input('\nDigite o numero da opção do menu: ')
        if op.isnumeric() and op in ['1','2','3','4']:

            n1_ = input('Digite o primeiro numero: ')
            n2_ = input('Digite o segundo numero: ')

            if not n1_.isnumeric() and not n2_.isnumeric():
                continue

            n1_, n2_ = int(n1_), int(n2_)

            match int(op):
                case 1:
                    print(f'\nSoma: {soma(n1_, n2_)}')
                case 2:
                    print(f'\nSubtração: {subtracao(n1_, n2_)}')
                case 3:
                    print(f'\nDivisão: {div(n1_, n2_)}')
                case 4:
                    print(f'\nMultiplicação: {mult(n1_, n2_)}')
                case _:
                    print()
            break
