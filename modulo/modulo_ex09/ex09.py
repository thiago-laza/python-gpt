'''
Desenvolva um pacote chamado cadastro que inclua módulos para cadastrar
e buscar informações de usuários. O pacote deve conter subpacotes para
categorias diferentes de usuários, como clientes e funcionários.
'''
print('CADASTRO - CLIENTES E FUNCIONARIOS')
tipo = input('Cliente[1]\nFuncionario[2]\nOpcao: ')
if tipo == '1':
    opcao_cliente = input('Cadastrar cliente[1]\Buscar cliente[2]\nOpcao: ')
    if opcao_cliente == '1':
        cadastro_cliente()
    elif opcao_cliente == '2':
        busca_cliente()
elif  == '2':
    opcao_funcionario = input('Cadastrar funcionario[1]\Buscar funcionario[2]\Opcao: ')
    if opcao_funcionario == '1':
        cadastro_funcionario()
    elif opcao_funcionario == '2':
        busca_funcionario()
