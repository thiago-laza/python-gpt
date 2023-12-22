'''
Crie um pacote chamado geometria que inclua módulos para cálculos de áreas e perímetros
de formas geométricas simples, como quadrado, retângulo e círculo. Utilize esses
módulos em um programa principal.
'''
from geometria__init__ import quadrado, retangulo, circunferencia
print('CALCULADORA DE AREA E PERIMETRO')
print('Informe a regiao que deseja determinar a area e o perimetro:\nQuadrado[Q]\nRetangulo[R]\nCircunferencia[C]')
print('-' * 40)
regiao = input('Regiao: ').upper()
if regiao == 'Q':
    lado = float(input('Informe a medida do lado: '))
    print(quadrado(lado))
elif regiao == 'R':
    largura = float(input('Informe a medida da largura: '))
    comprimento = float(input('Informe a medida do comprimento: '))
    print(retangulo(largura, comprimento))
elif regiao == 'C':
    raio = float(input('Informe a medida do raio: '))
    print(circunferencia(raio))

