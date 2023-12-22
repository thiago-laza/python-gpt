def adivinha():
    from random import randint
    num_aleatorio = randint(1, 10)
    palpite = int(input('Palpite: '))
    if palpite == num_aleatorio:
        print('Acertou')
    else:
        print(f'Errou, seu palpite foi {palpite} e o numero sorteado foi {num_aleatorio}')







