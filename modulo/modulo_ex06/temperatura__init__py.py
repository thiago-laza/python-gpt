def temperatura():
    unidade = input('Qual unidade deseja conveter:\n⁰K-> ⁰C[1]'
                    '\n⁰C-> ⁰K[2]\n⁰C->⁰F[3]\n⁰F->⁰C[4]'
                    '\n⁰F-> ⁰K[5]\n⁰K-> ⁰F[6]\nUNIDADE: ')
    if unidade == '1':
        valor = float(input('Informe a temperatura em K: '))
        resultado = valor - 273
        print(f'{valor}⁰K -> {resultado}⁰C')
    elif unidade == '2':
        valor = float(input('Informe a temperatura em ⁰C: '))
        resultado = valor + 273
        print(f'{valor}⁰C -> {resultado}⁰K')
    elif unidade == '3':
        valor = float(input('Informe a temperatura em ⁰C: '))
        resultado = valor * 1.8 + 32
        print(f'{valor}⁰C -> {resultado}⁰F')
    elif unidade == '4':
        valor = float(input('Informe a temperatura em ⁰F: '))
        resultado = (valor - 32) / 1.8
        print(f'{valor}⁰F -> {resultado}⁰C')
    elif unidade == '5':
        valor = float(input('Informe a temperatura em ⁰F: '))
        resultado = (valor - 32) * 5/9 + 1.8
        print(f'{valor}⁰F -> {resultado}⁰K')
    elif unidade == '6':
        valor = float(input('Informe a temperatura em ⁰K: '))
        resultado = (valor - 32) * 1.8 + 32
        print(f'{valor}⁰K -> {resultado}⁰F')





