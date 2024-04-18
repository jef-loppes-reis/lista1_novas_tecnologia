# Escreva um aplicativo que insere um número consistindo em cinco dígitos
# do usuário, separa o número em seus dígitos individuais e imprime os
# dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
# usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.

from re import sub
from os import system


def split_list_num(num:str) -> str:
    return sub(r"\[|\]|\'|\,",'', str([x for x in num]))


if __name__ == '__main__':
    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            print(f'Separação dos numeros: {split_list_num(n)}')
            break
