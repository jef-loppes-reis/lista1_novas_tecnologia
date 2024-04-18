# Escreva um programa que leia um número e verifique se é ou não um
# número primo.


from os import system


def check_num_primo(num:int) -> None:
    if num == 1:
        print('\nNumero e 1')
        return None
    for x in range(2, num):
        if num % x == 0:
            print(f'\nO numero {num} nao e primo!')
            break
        print(f'\nO numero {num} e primo!')
        break


if __name__ == '__main__':
    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            check_num_primo(int(n))
            break
