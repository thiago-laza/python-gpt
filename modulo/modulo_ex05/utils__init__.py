def remove_espaco(f):
    tamanho = len(f)
    nova_palavra = ''
    if f[0] == ' ':
        for n in range(1, tamanho):
            nova_palavra += f[n]
        print(nova_palavra)
    elif f[tamanho - 1] == ' ':
        for n in range(0, tamanho):
            nova_palavra += f[n]
        print(nova_palavra)
    else:
        print(f)







