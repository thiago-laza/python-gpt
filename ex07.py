'''
Soma de Elementos em Listas:

Escreva uma função que soma todos os elementos em uma lista.
Permita que o usuário forneça uma lista de números.
'''
def soma_valores(l):
    soma = 0
    for n in lista_valores:
        soma += n
        #return soma
    print(soma)


lista_valores = []
while True:
    valor = int(input('Digite um valor para a lista: '))
    lista_valores.append(valor)
    resp = input('Deseja inseris mais algum valor a lista? [s/n]: ')
    if resp in 'n':
        break
#print(soma_valores(lista_valores))
soma_valores(lista_valores)