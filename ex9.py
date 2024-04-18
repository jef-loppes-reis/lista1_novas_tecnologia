# Escreva um programa que exiba uma lista de opções (menu): adição,
# subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
# escolhida. Repita até que a opção saída seja escolhida.

from os import system


def soma(n1:int, n2:int) -> int:
    return n1 + n2


def subtracao(n1:int,  n2:int) -> int:
    return n1 - n2


def mult(n1:int, n2:int) -> int:
    return n1*n2


def div(n1:int, n2:int) -> int:
    return n1/n2


def menu() -> None:
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

            n1 = input('Digite o primeiro numero: ')
            n2 = input('Digite o segundo numero: ')

            if not n1.isnumeric() and not n2.isnumeric():
                continue

            n1, n2 = int(n1), int(n2)

            match int(op):
                case 1:
                    print(f'\nSoma: {soma(n1, n2)}')
                case 2:
                    print(f'\nSubtração: {subtracao(n1, n2)}')
                case 3:
                    print(f'\nDivisão: {div(n1, n2)}')
                case 4:
                    print(f'\nMultiplicação: {mult(n1, n2)}')
                case _:
                    print()
            break
