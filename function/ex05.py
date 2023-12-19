'''
Conversor de Temperatura:

Escreva funções para converter de Celsius para Fahrenheit e vice-versa.
Peça ao usuário para fornecer uma temperatura e a unidade desejada.
'''
def conversao_temperatura(t,u):
    global unidade_convertida
    if u == 'C':
        unidade_convertida = 'F'
        return 1.8*t + 32
    elif u == 'F':
        unidade_convertida = 'C'
        return (t-32)/1.8




temperatura = float(input('Informe a temperatura: '))
unidade = input('Informe a unidade (Celsius - C) ou (Fahrenheit - F): ').upper()

print(f'A temperatura de {temperatura}⁰{unidade} e equvalente a {conversao_temperatura(temperatura, unidade)}⁰{unidade_convertida}')