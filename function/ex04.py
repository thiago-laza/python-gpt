'''
Contador de Palavras:

Crie uma função que conte o número de palavras em uma string.
Permita que o usuário forneça uma frase e use a função para contar as palavras.
'''
def conta_palavras():
    numero_espacos = frase.count(' ')
    return numero_espacos + 1



frase = input('Digite uma frase: ')
print(f'A frase {(frase.upper())} tem {conta_palavras()} palavras.')