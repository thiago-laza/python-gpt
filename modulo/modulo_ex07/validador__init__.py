def validador_letras(letras):
    letras = input('Digite: ')
    if letras.isalpha():
        return f'{letras} contem apenas letras.'
    else:
        return f'{letras} nao contem apenas letras ou esta vazia.'


def validador_primo():
    numero = int(input('Digite um numero: '))
    cont = 1
    cont_primo = 0
    while cont <= numero:
        if numero % cont == 0:
            cont_primo += 1
        cont += 1
    if cont_primo == 2:
        return f'{numero} e primo.'
    else:
        return f'{numero} nao e primo.'