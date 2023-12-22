'''
Escreva um módulo chamado validador que inclua funções para verificar se
um número é primo e se uma string contém apenas letras. Importe essas
funções em um programa principal e utilize-as para realizar verificações.
'''
from validador__init__ import validador_letras, validador_primo
print('VERIFICADOR DE STRING E NUMEROS PRIMOS')
resp = input('Deseja verificar se sao strings[S] ou primo[P]: ').upper()
if resp == 'S':
    print(validador_letras(resp))
elif resp == 'P':
    print(validador_primo())


