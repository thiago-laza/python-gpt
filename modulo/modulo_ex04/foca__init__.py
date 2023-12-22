def forca():
    palavra = 'python'

    cont = 0
    resp = []
    while cont < len(palavra):
        letra = input('Digite uma letra: ')
        resp.append(letra)
        if letra in palavra:
            cont += 1
            print('ok')
        else:
            resp.clear()
            print(f'A palavra nao tem a letra {letra}')
        if cont == len(palavra):
            print('fim')



