import csv

with open('agenda.csv', 'r') as fp:
    arquivo = csv.reader(fp)
    for x in arquivo:
        print(x)
