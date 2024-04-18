# Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do
# segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.

from math import sqrt
from os import system


def eq_segundo_grau(a, b, c):

    Delta = b**2 - 4*a*c

    if Delta == 0:
        raiz = ((-1*b) + sqrt(Delta))/2*a
        raiz2 = ((-1*b)- sqrt(Delta))/2*a
        print ("O valor da raiz é:" + str(raiz) )

    elif Delta>0:
        raiz = ((-1*b) + sqrt(Delta))/2*a
        raiz2 = ((-1*b)- sqrt(Delta))/2*a
        print ("O valor das raizes é: " + str(raiz) + " e " + str(raiz2) )

    else:
        print ("Essa equação não possui raizes reais" )


if __name__ == '__main__':
    while True:
        system('cls')

        a = input ("Qual o valor de a: " )
        b = input ("Qual o valor de b: " )
        c = input ("Qual o valor de c: " )

        print([x.isnumeric() for x in [a,b,c]])

        if False in [x.isnumeric() for x in [a,b,c]]:
            continue

        a,b,c = int(a), int(b), int(c)
        eq_segundo_grau(a,b,c)
