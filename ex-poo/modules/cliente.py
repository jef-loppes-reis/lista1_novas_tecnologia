class Cliente:

    def __init__(self,  nome: str, sobrenome: str, cpf: str):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome) -> None:
        self._nome = nome
