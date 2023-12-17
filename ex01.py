'''
Calculadora Simples:

Crie uma função para adição, subtração, multiplicação e divisão de dois números.
Permita que o usuário escolha a operação desejada e forneça os números.
'''
def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


operacao = input('Escolha a operacao (adicao,subtracao,multiplicacao,divisao): ')
num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))

if operacao == 'adicao':
    resultado = adicao(num_1, num_2)
    print(f'A adicao entre {num_1} e {num_2} e igual a {resultado}.')
elif operacao == 'subtracao':
    resultado = subtracao(num_1, num_2)
    print(f'A subtracao entre {num_1} e {num_2} e igual a {resultado}.')
elif operacao == 'multiplicacao':
    resultado = multiplicacao(num_1, num_2)
    print(f'A multiplicacao entre {num_1} e {num_2} e igual a {resultado}.')
elif operacao == 'divisao':
    resultado = divisao(num_1, num_2)
    print(f'A divisao entre {num_1} e {num_2} e igual a {resultado}.')


