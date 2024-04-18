# Escreva um programa que converta uma temperatura digitada em "C” em
# “F”. A fórmula para essa conversão é:

#      9    
# F =  - C + 32
#      5

from os import system


def convert_celsius_to_fahrenheit(temp:int) -> float:
    return ((9/5) * temp) + 32


if __name__ == '__main__':
    while True:
        temp_celsius = input('Digite a temperatura em Celsius: ')
        if temp_celsius.isnumeric():
            print(f'Temperatura em Fahrenheit: {convert_celsius_to_fahrenheit(int(temp_celsius))}')
            break
