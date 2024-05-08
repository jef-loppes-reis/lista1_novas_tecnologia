# Comece com o programa que você escreveu no Exercício 4. Crie dois
# novos dicionários que representem pessoas diferentes e armazene os três
# Exercícios da Aula 2
# dicionários em uma lista chamada people . Percorra sua lista de pessoas
# com um laço. À medida que percorrer a lista, apresente tudo que você sabe
# sobre cada pessoa.

from ex4 import Ex4


if __name__ == '__main__':
    pessoas = [
        Ex4('Jeferson', 'Lopes', 30, 'Ceilandia').pessoa(),
        Ex4('Ana', 'Reis', 25, 'Guara').pessoa()
    ]

    for i, pessoa in enumerate(pessoas, start=1):
        print(f"Informações da pessoa {i}:")
        print("Primeiro nome:", pessoa["first_name"])
        print("Sobrenome:", pessoa["last_name"])
        print("Idade:", pessoa["age"])
        print("Cidade:", pessoa["city"])
        print()
