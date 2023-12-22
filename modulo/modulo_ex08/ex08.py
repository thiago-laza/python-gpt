'''
Crie um módulo chamado analisador_texto que contenha funções para contar
o número de palavras e calcular a média de caracteres por palavra em uma
string. Importe essas funções em um programa principal e teste-as com diferentes textos.
'''
from analisador_texto__init__ import contador_palavras, media_palavras
texto = input('Digite um texto: ')
print(contador_palavras(texto))
print(media_palavras(texto))
