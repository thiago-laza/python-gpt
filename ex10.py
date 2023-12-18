'''
Verificador de Ano Bissexto:

Implemente uma função que verifica se um ano é bissexto.
Solicite ao usuário um ano e use a função para verificar.
'''
def ano_bissexto(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        print('E bissexto.')
    else:
        print('Nao e bissexto.')




ano = int(input('Informe um ano para saber se ele e ou nao bissexto: '))
ano_bissexto(ano)