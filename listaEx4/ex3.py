# Escreva um programa que compare duas listas. Considere a primeira lista
# como a versão inicial e a segunda como a versão após alterações.
# Utilizando operações com conjuntos, seu programa deverá imprimir a lista
# de modificações entre essas duas versões, listando:
#  ◦ os elementos que não mudaram
#  ◦ os novos elementos
#  ◦ os elementos que foram removidos

class Ex3:

    def __init__(self, lista_inicial:list, lista_modificada:list) -> None:
        self.lista_inicial = lista_inicial
        self.lista_modificada = lista_modificada


    def comparar_listas(self) -> tuple[dict]:
        _set_inicial = set(self.lista_inicial)
        _set_modificada = set(self.lista_modificada)

        _nao_mudaram = _set_inicial.intersection(_set_modificada)
        _novos_elementos = _set_modificada - _set_inicial
        _removidos = _set_inicial - _set_modificada

        return _nao_mudaram, _novos_elementos, _removidos


if __name__ == '__main__':
    lista_ini = [1, 2, 3, 4, 5]
    lista_mod = [3, 4, 5, 6, 7]

    nao_mudaram, novos_elementos, removidos = Ex3(lista_ini, lista_mod).comparar_listas()

    print("Elementos que não mudaram:", nao_mudaram)
    print("Novos elementos:", novos_elementos)
    print("Elementos removidos:", removidos)
