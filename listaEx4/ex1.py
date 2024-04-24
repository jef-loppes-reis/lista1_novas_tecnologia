# Escreva um programa que gere um dicionário, em que cada chave seja um
# caractere, e seu valor seja o número desse caractere encontrado em uma
# frase lida.
# Exemplo:O rato ->
# {"O":1,"r":1,"a":1,"t":1,"o":1}

def slice_frase(frase:str) -> dict[str]:
    return dict(enumerate([x for x in frase]))

if __name__ == "__main__":
    print(slice_frase('Jeferson Lopes'))