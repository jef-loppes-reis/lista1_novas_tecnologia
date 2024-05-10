from datetime import datetime
from csv import reader


class Agenda:

    _agenda = {}
    _columns = ['nome', 'telefone', 'email', 'data_nascimento']
    _hoje = datetime.today()

    def __init__(self, nome:str, tel:str, email:str, dia:int, mes:int, ano:int) -> None:
        self.nome = nome
        self.tel = tel
        self.email = email
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def salvar_contato():
        ...

    def buscar_contato():
        ...

    def apagar_contato():
        ...

    def listar_contatos():
        ...

    def alterar_contato():
        ...

    def salvar_agenda():
        ...

    def listar_ani():
        ...

    def carregar_agenda(path_agenda:str='./agenda.csv'):
        with open(path_agenda, 'r', encoding='utf-8') as fp:
            df_agenda = reader(fp.read())
        for contato in df_agenda:
            print(contato)
