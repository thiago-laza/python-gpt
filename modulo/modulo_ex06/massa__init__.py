def massa():
    unidade = input('Qual unidade deseja conveter:\nKg-> g[1]'
                    '\ng-> Kg[2]\nUNIDADE: ')
    if unidade == '1':
        valor = float(input('Informe o valor (Kg): '))
        resultado = valor * 1000
        print(f'{valor} Kg -> {resultado} g')
    elif unidade == '2':
        valor = float(input('Informe o valor (g): '))
        resultado = valor / 1000
        print(f'{valor} g -> {resultado} Kg')


