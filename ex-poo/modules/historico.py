from datetime import datetime


class Historico:

    def __init__(self):
        self._data_de_abertura = datetime.now().strftime("%d-%m-%Y | %H:%M:%S")
        self._transacoes = []

    def imprime(self):
        print(f"A data de abertura: {self._data_de_abertura}")
        print("Transações:")
        for _ in self._transacoes:
            print(_)

    @property
    def transacoes(self):
        return self._transacoes
