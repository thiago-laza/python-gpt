def comprimento():
    unidade = input('Qual unidade deseja conveter:\nKm-> m[1]'
                    '\nm-> Km[2]\nKm->cm[3]\ncm->Km[4]'
                    '\nm-> cm[5]\ncm-> m[6]\nUNIDADE: ')
    if unidade == '1':
        valor = float(input('Informe o valor(Km): '))
        resultado = valor * 1000
        print(f'{valor} Km -> {resultado} m')
    elif unidade == '2':
        valor = float(input('Informe o valor(m): '))
        resultado = valor / 1000
        print(f'{valor} m -> {resultado} Km.')
    elif unidade == '3':
        valor = float(input('Informe o valor(cm): '))
        resultado = valor * 100000
        print(f'{valor} Km -> {resultado} cm')
    elif unidade == '4':
        valor = float(input('Informe o valor (cm): '))
        resultado = valor / 100000
        print(f'{valor} cm -> {resultado} Km')
    elif unidade == '5':
        valor = float(input('Informe o valor (m): '))
        resultado = valor * 100
        print(f'{valor} m -> {resultado} cm')
    elif unidade == '6':
        valor = float(input('Informe o valor (cm): '))
        resultado = valor / 100
        print(f'{valor} cm -> {resultado} m')








