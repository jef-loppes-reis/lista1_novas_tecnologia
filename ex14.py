"""Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
fatorial."""


from os import system


def fatorial(n:int):
    """_summary_

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    string_aux = f'{n}! ='
    res=1
    count=1
    while count <= n:
        string_aux += f' * {count}' if count > 1 else f' {count}'
        res *= count
        count += 1
    return res, string_aux


if __name__ == '__main__':
    NUM_NEGATIVO = ''
    while True:
        system('cls')
        print(NUM_NEGATIVO)
        num = input("Fatorial de: ")
        if '-' in num:
            NUM_NEGATIVO = 'O numero digitado era negativo\n'
            continue
        if not num.isnumeric():
            continue
        fat = fatorial(int(num))
        print(f'\n{fat[1]}, que dá {fat[0]}')
        break
