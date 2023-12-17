'''
Verificador de Números Primos:

Escreva uma função que verifica se um número é primo ou não.
Peça ao usuário para fornecer um número e use a função para verificar se é primo.
'''
def primo(n):
    contador = 1
    contador_primo = 0
    while contador <= n:
        if n % contador == 0:
            contador_primo+=1
        contador+=1
    if contador_primo == 2:
        print(f'{num} e primo.')
    else:
        print(f'{num} nao e primo')




num = int(input('Digite um numero para verificar se ele e primo: '))
primo(num)
