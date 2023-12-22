'''
Crie um módulo chamado conversor que contenha funções para converter unidades
de medida, como metros para quilômetros, quilogramas para gramas, etc.
Utilize essas funções em um programa principal que realiza diversas conversões.
'''
print('CONVERSOR DE UNIDADES')
grandeza = input('Qual grandeza deseja converter:\nComprimento[C]\nMassa[M]\nTemperatura[T]\nGRANDEZA: ').upper()
if grandeza == 'C':
    from comprimento__init__ import comprimento
    comprimento()
elif grandeza == 'M':
    from massa__init__ import massa
    massa()
elif grandeza == 'T':
    from temperatura__init__py import temperatura
    temperatura()


