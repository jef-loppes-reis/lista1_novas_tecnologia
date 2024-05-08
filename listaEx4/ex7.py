# Crie uma lista chamada sandwich_orders e a preencha com os nomes de
# vários sanduíches. Em seguida, crie uma lista vazia chamada
# finished_sandwiches . Percorra a lista de pedidos de sanduíches com um laço
# e mostre uma mensagem para cada pedido, por exemplo, Preparei seu
# sanduíche de atum. À medida que cada sanduíche for preparado, transfirao para a lista de sanduíches prontos. Depois que todos os sanduíches
# estiverem prontos, mostre uma mensagem que liste cada sanduíche
# preparado.

class Ex7:
    def __init__(self, lista_elementos:list[str]=["Atum", "Frango", "Queijo", "Presunto e queijo", "Vegetariano"]) -> None:
        self.sandwich_orders = lista_elementos

    def burger(self):
        finished_sandwiches = []
        print("Preparando os sanduíches:")
        while self.sandwich_orders:
            pedido = self.sandwich_orders.pop(0)
            print(f"Preparei seu sanduíche de {pedido}.")
            finished_sandwiches.append(pedido)

        print("\nSanduíches preparados:")
        for sanduiche in finished_sandwiches:
            print(sanduiche)


if __name__ == '__main__':
    Ex7().burger()
