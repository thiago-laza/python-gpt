'''
Ordenação de Lista:

Crie uma função para ordenar uma lista de números em ordem crescente.
Permita que o usuário forneça uma lista e use a função para ordená-la.
'''
def ordena_lista():
    lista_elementos = []
    for l in range(numero_elementos):
        valor = int(input(f'{l+1}⁰ valor: '))
        lista_elementos.append(valor)
        lista_ordenada = sorted(lista_elementos)
    return lista_ordenada


numero_elementos = int(input('Informe o numero de elementos da lista: '))
resultado = ordena_lista()
print(resultado)


