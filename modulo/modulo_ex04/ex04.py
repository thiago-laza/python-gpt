'''
Crie um pacote chamado jogos que inclua módulos para jogos simples, como
adivinhação de números e jogo da forca. Utilize esses módulos em um
programa principal que permita ao usuário escolher qual jogo jogar.
'''
print('ESCOLHA QUAL JOGO PRETENDE JOGAR')
jogo = input('Adivinhacao[A]\nForca[F]\nEscolha: ').upper()
if jogo == 'A':
    from adivinha__init__ import adivinha
    adivinha()
elif jogo == 'F':
    from foca__init__ import forca
    forca()

