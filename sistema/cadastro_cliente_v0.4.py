def limpar_tela():
    print("\n" * 130)


def cadastrar_cliente(nome, endereco, cpf):
    global Nomes, Enderecos, Cpfs
    print('CADASTRANDO >>>>>>\n')

    Nomes.append(nome)
    Enderecos.append(endereco)
    Cpfs.append(cpf)

    print(f'Cliente {nome} cadastrado com sucesso!')
    input('[ENTER] para continuar...')


def exibir_clientes():
    global Nomes, Enderecos, Cpfs
    print('RELATÓRIO >>>>>\n')

    for p in range(len(Nomes)):
        print(f'Nome     : {Nomes[p]}')
        print(f'Endereços: {Enderecos[p]}')
        print(f'CPF      : {Cpfs[p]}')
        print('________________________________________')

    input('[ENTER] para continuar...')


def pesquisar_cliente():
    print('Pesquisando....')
    input('[ENTER] para continuar...')


def excluir_cliente():
    limpar_tela()
    print('Excluindo....')
    input('[ENTER] para continuar...')


def editar_cliente():
    limpar_tela()
    print('Editando....')
    input('[ENTER] para continuar...')


def validar_usuario(us, pw):
    if us == 'admin' and pw == 'admin':
        return True

    return False
# ====================================================


Nomes = []
Enderecos = []
Cpfs = []

print(f'{">> SYSCAD <<":=^40}')
# login = input('Usuário: ')
# senha = input('Senha: ')

if True: # validar_usuario(login, senha):
    while True:
        print('|================ MENU ================|')
        print('| [1] - CADASTRAR                      |')
        print('| [2] - RELATORIO                      |')
        print('| [3] - PESQUISAR                      |')
        print('| [4] - EXCLUIR                        |')
        print('| [5] - EDITAR                         |')
        print('| [0] - SAIR                           |')
        op = input('> ')

        if op == '0':
            print('Fim do sistema....')
            break

        elif op == '1':
            n = input('Nome do Cliente: ')
            e = input('Endereço do Cliente: ')
            c = input('CPF do Cliente: ')
            cadastrar_cliente(n, e, c)

        elif op == '2':
            exibir_clientes()
        elif op == '3':
            pesquisar_cliente()
        elif op == '4':
            excluir_cliente()
        elif op == '5':
            editar_cliente()
        else:
            print('Opção inválida!')
            input('[ENTER] para continuar...')
