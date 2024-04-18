"""Modifique o programa anterior de forma a ler um número n. Imprima os n
primeiros números primos."""


from os import system
from concurrent.futures import ProcessPoolExecutor


def check_num_primo(num:int) -> None:
    """_summary_

    Args:
        num (int): _description_

    Returns:
        _type_: _description_
    """
    if num % num == 0:
        return f'O numero {num} nao e primo!'
    return f'O numero {num} e primo!'


if __name__ == '__main__':

    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            break

    lista = range(2, int(n)+1)

    result = []
    with ProcessPoolExecutor() as executor:
        for future in executor.map(check_num_primo, lista):
            print(future)
            result.append(future)

    # print(list(dict.fromkeys(result)))
