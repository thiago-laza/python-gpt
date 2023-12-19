'''
Validador de Senha:

Crie uma função que verifica se uma senha atende a critérios mínimos (comprimento, presença de letras e números, etc.).
Permita que o usuário insira uma senha e use a função para validar.
'''
def verifica_senha(s):
    tamanho = len(senha)
    if tamanho < 8:
        print('A senha precisa ter no minimo 8 caracteres.')
    else:
        print('A senha tem 8 ou mais caracteres. OK!')


    tem_letra = any(char.isalpha() for char in senha)
    if tem_letra:
        print('A senha contem letra. OK!')
    else:
        print('A senha nao tem letra.')

    tem_numero = any(char.isdigit() for char in senha)
    if tem_numero:
        print('A senha tem numero. OK!')
    else:
        print('A senha nao tem numero.')

    if tamanho and tem_letra and tem_numero:
        print('Senha valida.')
    else:
        print('Senha invalida.')


senha = input('Senha: ')
verifica_senha(senha)


