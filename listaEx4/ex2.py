# Escreva um programa que compare duas listas. Utilizando operações com
# conjuntos, imprima:
# a. os valores comuns às duas listas
# b. os valores que só existem na primeira
# c. os valores que existem apenas na segunda
# d. uma lista com os elementos não repetidos das duas listas.
# e. a primeira lista sem os elementos repetidos na segunda


def valores_comuns_entre_listas(lista1:list, lista2:list) -> list:
    valores_comuns = []
    for x in lista1:
        if x in lista2:
            valores_comuns.append(x)
    return valores_comuns


def valores_somente_lista1(lista1:list, lista2:list) -> list:
    valores_que_so_existe_lista1 = []
    for x in lista1:
        if not x in lista2:
            valores_que_so_existe_lista1.append(x)
    return valores_que_so_existe_lista1


def valores_somente_lista2(lista1:list, lista2:list) -> list:
    valores_que_so_existe_lista2 = []
    for x in lista2:
        if not x in lista1:
            valores_que_so_existe_lista2.append(x)
    return valores_que_so_existe_lista2


if __name__ == '__main__':
    LISTA1 = ['a', 'b', 'c']
    LISTA2 = ['a', 'b', 'c', 'd', 'e']
    a = valores_comuns_entre_listas(LISTA1, LISTA2)
    b = valores_somente_lista1(LISTA1, LISTA2)
    c = valores_somente_lista2(LISTA1, LISTA2)

    print(a, b, c)
