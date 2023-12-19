'''
Calculadora de Fatorial:

Implemente uma função para calcular o fatorial de um número.
Solicite um número do usuário e imprima seu fatorial.
'''
def fatorial(n):
    f = 1
    for c in range(1,n):
        f*=n
        n-=1
    return f


n = int(input('Digite um numero para obter seu fatorial: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}.')






