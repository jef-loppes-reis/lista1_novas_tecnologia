"""O quadrado de um número natural n é dado pela soma dos n primeiros
números ímpares consecutivos. Por exemplo, 1^2 = 1, 2^2 = 1+3 etc. Dado
um número n, calcule seu quadrado usando a soma de ímpares ao invés de
produto."""

from os import system


def quadrado_por_soma_impares(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    primeiro_impar = 2 * n - 1
    soma_impares = primeiro_impar
    proximo_impar = primeiro_impar

    for _ in range(n - 1):
        proximo_impar += 2
        soma_impares += proximo_impar

    return soma_impares


if __name__ == '__main__':
    while True:
        system('cls')
        num = input('Digite o numero: ')
        if num.isnumeric():
            quadrado = quadrado_por_soma_impares(int(num))
            print(f"O quadrado de {num} é {quadrado}")
            break
