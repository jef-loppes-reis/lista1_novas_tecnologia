import csv
import os
import datetime

agenda = {}
campos= ["nome", "telefone", "email", "datanasc"]
datahoje = datetime.date.today()

def salva_contato(contato):
    agenda[contato[0]] = contato
    print(f"O contato de {contato[0]} foi salvo com sucesso!")

def busca_contato(nome):
    return agenda[nome]

def apaga_contato(nome):
    del agenda[nome]
    print(f"O contato de {nome} foi apagado com sucesso!")
    
def lista_contatos(agenda):
    for contato in agenda.values():
        print(contato)

def altera_contato(nome):
    contato=agenda[nome]
   
    for i,campo in enumerate(campos):
        if("Y"==input(f"Você quer alterar o {campo}? Y ou N. ").upper()):
            contato[i] = input(f"Qual será o novo {campo}? ")

    apaga_contato(nome)
    salva_contato(contato)
    print(f"O contato {contato[0]} foi alterado com os dados {contato} !")

def salva_agenda(agenda):
    with open("agenda.csv","w",newline="") as arquivo_csv:
        saida = csv.writer(arquivo_csv)
        saida.writerows(agenda.values())

def lista_aniversariantes():
    aniversariantes=[]
    for contato in agenda.values():
        datanasc = datetime.datetime.strptime(contato[3],"%Y-%m-%d")
        if(datahoje.month == datanasc.month and datahoje.day == datanasc.day):
            idade = datahoje.year - datanasc.year
            aniversariantes.append([contato[0],idade])
    return aniversariantes

def abre_agenda():
    with open("agenda.csv") as arquivo_csv:
        entrada = csv.reader(arquivo_csv)

        for contato in entrada:
            agenda[contato[0]]=contato

    for pessoa in lista_aniversariantes():
        print(f"{pessoa[0]} faz {pessoa[1]} anos hoje. Dê parabéns!")



if os.path.isdir('/Users/adamsmith/Documents/py_sexta_noite/Agenda'):
    os.chdir('/Users/adamsmith/Documents/py_sexta_noite/Agenda')
    abre_agenda()
else:
    os.mkdir('/Users/adamsmith/Documents/py_sexta_noite/Agenda')
    os.chdir('/Users/adamsmith/Documents/py_sexta_noite/Agenda')



while 1:
    
    ope = int(input("""
                    Agenda Pessoal
                    
                1 - Salvar Contato
                2 - Alterar Contato
                3 - Buscar Contato
                4 - Apagar Contato
                5 - Listar Contatos



        pressione 0 para sair.

    """))

    if ope == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        print("Qual sua Data de Nascimento: ")
        ano = int(input("Ano: "))
        mes = int(input("Mês: "))
        dia = int(input("Dia: "))
        datanasc = datetime.date(year=ano, month=mes, day=dia)
        dataregis = datetime.datetime.today()
        salva_contato([nome, telefone,email,datanasc,dataregis])
    elif ope == 2:
        nome = input("Qual contato você quer alterar:")
        if (nome in agenda.keys()):
             altera_contato(nome)
        else:
            print(f"Não existe o contato {nome}!")
    elif ope == 3:
        nome = input("Qual contato quer buscar: ")
        print(busca_contato(nome))
    elif ope == 4:
        nome = input("Qual contato: ")
        apaga_contato(nome)
    elif ope == 5:
        lista_contatos(agenda)
    elif ope == 0:
        salva_agenda(agenda)
        break
    else:
        print("Opção inválida!")
