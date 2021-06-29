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


def pesquisar_cliente(cpf=None, nome=None):
    global Cpfs
    print('PESQUISANDO >>>>>\n')

    if cpf in Cpfs:
        return Cpfs.index(cpf)
    return -1     # não encontrou o cpf


def excluir_cliente(cpf):

    print('EXCLUIDO >>>>>>\n')

    c = pesquisar_cliente(cpf)
    if c is not -1:
        print('Tem certeza que deseja excluir?')
        print(f'Nome: {Nomes[c]} :: CPF: {Cpfs[c]}')
        i = input('[S] Sim')
        if i.lower() == 's':
            del(Nomes[c])
            del(Enderecos[c])
            del(Cpfs[c])
            print('Cliente excuído com sucesso.')
        else:
            print('O usuário cancelou a exclusão')
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
            cpf = input('CPF: ')
            c = pesquisar_cliente(cpf)
            if c != -1:
                print(f'Nome: {Nomes[c]}')
                print(f'Endereço: {Enderecos[c]}')
                print(f'CPF: {Cpfs[c]}')
            else:
                print('Valor não encontrado!')
            input('[ENTER] para continuar...')

        elif op == '4':
            cpf = input('CPF do cliente: ')
            excluir_cliente(cpf)
        elif op == '5':
            editar_cliente()
        else:
            print('Opção inválida!')
            input('[ENTER] para continuar...')
