# Crie vários dicionários, em que o nome de cada dicionário seja o nome de
# um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
# nome do dono. Armazene esses dicionários em uma lista chamada pets .
# Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
# apresente tudo que você sabe sobre cada animal de estimação.


class Ex6:
    def __init__(self, nome:str, tipo:str, dono:str) -> None:
        self.nome = nome
        self.tipo = tipo
        self.dono = dono


    def pet(self) -> dict:
        return {
            'nome': self.nome,
            'tipo': self.tipo,
            'dono': self.dono
        }


if __name__ == '__main__':
    pets = [
        Ex6('Rex', 'Cachorro', 'Pedro').pet(),
        Ex6('Billy', 'Gato', 'Ana').pet(),
        Ex6('Zafira', 'Passaro', 'Joao').pet()
    ]

    for pet in pets:
        print(f"Informações sobre {pet['nome']}:")
        print("Tipo:", pet["tipo"])
        print("Dono:", pet["dono"])
        print()
