'''
Escreva uma função em um módulo separado que receba uma lista de números e retorne
a média aritmética. Importe essa função em um programa principal e teste-a
com diferentes conjuntos de números.
'''
from media__init__ import media
lista = []
while True:
    valor = int(input('Informe um valor para ser colocado na lista: '))
    lista.append(valor)
    resp = input('Deseja acrescenta mais algum valor?[s/n]: ')
    if resp in 'Nn':
        break
print(media(lista))
