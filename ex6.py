# Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do
# segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.

from math import sqrt
from os import system


def eq_segundo_grau(a:int, b:int, c:int):
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_
        c (int): _description_
    """

    delta = b**2 - 4*a*c

    if delta == 0:
        raiz = ((-1*b) + sqrt(delta))/2*a
        raiz2 = ((-1*b)- sqrt(delta))/2*a
        print ("O valor da raiz é:" + str(raiz) )

    elif delta>0:
        raiz = ((-1*b) + sqrt(delta))/2*a
        raiz2 = ((-1*b)- sqrt(delta))/2*a
        print ("O valor das raizes é: " + str(raiz) + " e " + str(raiz2) )

    else:
        print ("Essa equação não possui raizes reais" )


if __name__ == '__main__':
    while True:
        system('cls')

        a_ = input ("Qual o valor de a: " )
        b_ = input ("Qual o valor de b: " )
        c_ = input ("Qual o valor de c: " )

        print([x.isnumeric() for x in [a_, b_, c_]])

        if False in [x.isnumeric() for x in [a_, b_, c_]]:
            continue

        a_, b_, c_ = int(a_), int(b_), int(c_)
        eq_segundo_grau(a_, b_, c_)
