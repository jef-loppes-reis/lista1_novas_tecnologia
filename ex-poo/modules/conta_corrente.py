from datetime import datetime

from modules.conta import Conta


class ContaCorrente(Conta):

    def __init__(self, numero: str, cliente: str, saldo: float, limite: float, aniversario_conta: datetime):
        super().__init__(numero,  "Corrente", cliente, saldo, limite)
        self._aniversario_conta = aniversario_conta
