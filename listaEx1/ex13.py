"""O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n
fatorialˮ) e é definido como segue:
n! = n * (n - 1) * (n - 2) * ... * 1 (para valores de n maiores ou iguais a 1) e n! = 1 (para n = 0)
Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120."""

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
    while True:
        system('cls')
        num = input("Fatorial de: ")
        if num.isnumeric():
            fat = fatorial(int(num))
            print(f'{fat[1]}, que dá {fat[0]}')
            break
