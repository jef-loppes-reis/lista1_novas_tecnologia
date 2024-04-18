# Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do
# usuário esses números e imprime sua soma, produto, diferença e divisão.

from os import system

def soma(n1:int, n2:int) -> int:
    return n1 + n2


def subtracao(n1:int,  n2:int) -> int:
    return n1 - n2


def mult(n1:int, n2:int) -> int:
    return n1*n2


def div(n1:int, n2:int) -> int:
    return n1/n2


if __name__ == "__main__":
    while True:
        system('cls')
        n1 = input('Digite o primeiro numero: ')
        n2 = input('Digite o segundo numero: ')
        if n1.isnumeric() and n2.isnumeric():
            n1, n2 = int(n1), int(n2)
            print(f'''
                    Soma: {soma(n1,n2)}\n\
                    Produto: {mult(n1,n2)}\n\
                    Diferença: {subtracao(n1,n2)}\n\
                    Divisão: {div(n1,n2)}
                    ''')
            break
