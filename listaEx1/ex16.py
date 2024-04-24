"""A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … 
Os dois primeiros termos são iguais a 1, e a partir do terceiro,
o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3,
exiba o n-ésimo termo da série de Fibonacci."""


from os import system


def fibonacci(n:int) -> int:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    if n in [1,2]:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    NUM_NEGATIVO = ''
    while True:
        system('cls')
        print(NUM_NEGATIVO)
        num = input('Digite o numero: ')
        if '-' in num:
            NUM_NEGATIVO = 'O numero digitado era negativo\n'
            continue
        if num.isnumeric():
            N_ESIMO_FIBONACCI = fibonacci(int(num))
            print(f"O {num}-ésimo termo da série de Fibonacci é {N_ESIMO_FIBONACCI}")
            break
