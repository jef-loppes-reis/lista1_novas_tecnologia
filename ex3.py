# Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar
# ou par.

from os import system

def impar_par(n:int) -> str:
    return 'O numero e IMPAR' if n%2 == 1 else 'O numero e PAR'


if __name__ == '__main__':
    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            print(impar_par(int(n)))
            break
