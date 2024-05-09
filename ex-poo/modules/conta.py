from datetime import datetime

from modules.historico import Historico


class Conta:

    _num_contas = 0

    def __init__(self, num_conta: str, tipo_conta: str,
                 cliente: str, saldo: float, limit: float) -> None:

        self._num_conta = num_conta
        self._tipo_conta = tipo_conta
        self._cliente = cliente
        self._saldo = saldo
        self._limit = limit
        self._historico = Historico()
        Conta._num_contas += 1

    @property
    def numero_conta(self) -> str:
        self._historico.transacoes.append(f'\n[{datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S")}] -> Consulta da conta de numero {self._num_conta}')
        return self._num_conta

    @property
    def numero_conta(self, novo_numero: str) -> str:
        self._historico.transacoes.append(f"\n[{datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S")}] -> Alterou o número da conta {self._num_conta} para {novo_numero}.")
        self._num_conta = novo_numero

    @property
    def saldo(self) -> float:
        self._historico.transacoes.append(f"\n[{datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S")}] -> Consulta de saldo {self._saldo}.")
        return self._saldo

    @saldo.setter
    def saldo(self, novo_valor: float) -> None:
        self._historico.transacoes.append(f"\n[{datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S")}] -> Alterou o saldo {self._saldo} para {novo_valor}.")
        self._saldo = novo_valor

    @property
    def titular(self) -> str:
        self._historico.transacoes.append(f"\n[{datetime.now().strftime(
            "%d-%m-%Y | %H:%M:%S")}] -> Consulta do titular da conta {self._cliente.nome}.")
        return self._cliente

    def extrato(self) -> str:
        self._historico.transacoes.append(
            f"\n[{datetime.now().strftime("%d-%m-%Y | %H:%M:%S")}] -> Consultou o extrato.")
        return f"Cliente: {self._cliente.nome} \nConta: {self._num_conta} \nSaldo: {self.saldo}"

    @staticmethod
    def get_total_contas() -> int:
        return Conta._num_contas

    def __str__(self):
        return "Este objeto é uma Conta"
