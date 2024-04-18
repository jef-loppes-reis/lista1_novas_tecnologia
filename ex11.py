# Coloque um número bem grande para ser executado no exemplo anterior,
# você perceberá que demora bastante, consegue pensar num solução na
# lógica para reduzir o tempo de procura?

from os import system
from concurrent.futures import ProcessPoolExecutor


def check_num_primo(num:int) -> None:
    if num % num == 0:
        return f'O numero {num} nao e primo!'
    return f'O numero {num} e primo!'


if __name__ == '__main__':

    while True:
        system('cls')
        n = input('Digite o numero: ')
        if n.isnumeric():
            break

    lista = range(2, int(n))

    result = []
    with ProcessPoolExecutor() as executor:
        for future in executor.map(check_num_primo, lista):
            result.append(future)
    
    print(list(dict.fromkeys(result)))
