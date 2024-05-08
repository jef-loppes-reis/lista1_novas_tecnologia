# Use um dicionário para armazenar informações sobre uma pessoa que
# você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
# cidade em que ela vive. Você deverá ter chaves como first_name , last_name ,
# age e city . Mostre cada informação armazenada em seu dicionário.


class Ex4:

    def __init__(self, first_name:str, last_name:str, age:int, city:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    

    def pessoa(self) -> dict[str,int]:
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'city': self.city
        }


if __name__ == '__main__':

    pessoa = Ex4('Jeferson', 'Lopes', 30, 'Ceilandia').pessoa()

    print("Primeiro nome:", pessoa["first_name"])
    print("Sobrenome:", pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])
