'''
Escreva uma função em um módulo chamado utils que recebe uma string e
remove os espaços em branco no início e no final. Importe essa função
em um programa principal e teste-a com várias strings.
'''
from utils__init__ import remove_espaco
frase = input('Escreva uma frase: ')
remove_espaco(frase)