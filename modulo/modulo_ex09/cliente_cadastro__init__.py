def cliente():
    global cliente
    opcao = input('Deseja cadastrar ou buscar cliente?\nCadastrar[1]\nBuscar[2]\nOpcao: ')
    if opcao == '1':
        clientes = []
        while True:
            cliente = {}
            cliente['nome'] = input('Nome: ')
            cliente['telefone'] = int(input('Telefone: '))
            cliente['email'] = input('Email: ')
            resp = input('Deseja cadastrar mais algum cliente? [s/n]: ')
            clientes.append(cliente)
            if resp in 'Nn':
                break




cliente()


