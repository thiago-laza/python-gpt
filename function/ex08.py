'''
Fibonacci Recursivo:

Implemente uma função recursiva para gerar os primeiros N números da sequência de Fibonacci.
Solicite ao usuário o valor de N.
'''
def fatorial(n):
    global x1, x2, x
    x1 = 1
    x2 = 1
    print(f'{x1} {x2}',end=' ')
    for i in range(n-2):
        x = x1 + x2
        x1 = x2
        x2 = x
        print(x, end=' ')




numero = int(input('Gerar n numeros da sequencia de Fibonacci: '))
fatorial(numero)

