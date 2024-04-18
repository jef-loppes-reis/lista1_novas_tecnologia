# Escreva um programa que leia a quantidade em segundos e imprima o
# resultado em dias, horas, minutos e segundos.

from datetime import datetime
from os import system

def convert_seconds(seconds:int) -> None:
    dias = seconds // 86400
    seconds_rest = seconds % 86400
    horas = seconds_rest // 3600
    seconds_rest = seconds_rest % 3600
    minutos = seconds_rest // 60
    seconds_rest = seconds_rest % 60

    print(f'''
    Dias: {dias}
    Horas: {horas}
    Minutos: {minutos}
    Segundos: {seconds_rest}
    
    {dias} Dias, {horas} horas {minutos} minutos e {seconds_rest} segundos.
    ''')

if __name__ == '__main__':
    while True:
        system('cls')
        sec = input('Digite os segundos: ')
        if sec.isnumeric():
            convert_seconds(int(sec))
            break
