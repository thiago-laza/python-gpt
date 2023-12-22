'''
Crie um módulo chamado calculadora que contenha funções básicas de operações
matemáticas (soma, subtração, multiplicação e divisão). Importe e use essas
funções em um programa principal.
'''
from calculadora__init__ import adicao, subtracao, multiplicacao, divisao
print('Informe dois valores e escolha uma operacao.')
num_1 = int(input('Informe o primeiro valor: '))
num_2 = int(input('Informe o segundo valor: '))
print('Escolha a operacao: \nAdicao[A]\nSubtracao[S]\nMultiplicacao[M]\nDivisao[D]')
operacao = input('Operacao: ').upper()
print('='*33)
if operacao == 'A':
    print(f'A adicao de {num_1} com {num_2} e igual a {adicao(num_1, num_2)}.')
elif operacao == 'S':
    print(f'A subtracao de {num_1} com {num_2} e igual a {subtracao(num_1, num_2)}')
elif operacao == 'M':
    print(f'A multiplicacao de {num_1} com {num_2} e igual a {multiplicacao(num_1, num_2)}')
elif operacao == 'D':
    print(f'A divisao de {num_2} com {num_2} e igual a {divisao(num_1, num_2)}')
