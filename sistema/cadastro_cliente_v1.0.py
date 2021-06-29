import os


def limpar_tela():
    os.system('clear')


def cadastrar_cliente(nome, endereco, cpf):
    global Nomes, Enderecos, Cpfs
    limpar_tela()
    print('CADASTRANDO >>>>>>\n')

    Nomes.append(nome)
    Enderecos.append(endereco)
    Cpfs.append(cpf)

    print(f'Cliente {nome} cadastrado com sucesso!')
    input('[ENTER] para continuar...')


def exibir_clientes():
    global Nomes, Enderecos, Cpfs
    limpar_tela()
    print('RELATÓRIO >>>>>\n')

    for p in range(len(Nomes)):
        print(f'Nome     : {Nomes[p]}')
        print(f'Endereços: {Enderecos[p]}')
        print(f'CPF      : {Cpfs[p]}')
        print('________________________________________')

    input('[ENTER] para continuar...')


def pesquisar_cliente(cpf=None, nome=None):
    global Cpfs
    limpar_tela()
    print('PESQUISANDO >>>>>\n')

    if cpf in Cpfs:
        return Cpfs.index(cpf)
    return -1     # não encontrou o cpf


def excluir_cliente(cpf):
    limpar_tela()
    print('EXCLUIDO >>>>>>\n')

    c = pesquisar_cliente(cpf)
    if c != -1:
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


def editar_cliente(cpf):
    limpar_tela()
    print('EDITANDO >>>>>>\n')
    global Nomes, Enderecos, Cpfs
    c = pesquisar_cliente(cpf)

    if c != -1:
        print(f'Nome    : {Nomes[c]}')
        print(f'Endereço: {Enderecos[c]}')
        print(f'CPF     : {Cpfs[c]}')
        print('____________________________')
        print('Digite um novo valor ou [ENTER] para permanecer o atual')
        novo_n = input('Novo Nome: ')
        novo_e = input('Novo Endereço: ')
        novo_c = input('Novo CPF: ')

        if novo_n != '':
            Nomes[c] = novo_n
        if novo_e != '':
            Enderecos[c] = novo_e
        if novo_c != '':
            Cpfs[c] = novo_c

    print('Dados alterados com sucesso.')
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
login = input('Usuário: ')
senha = input('Senha: ')

if validar_usuario(login, senha):
    while True:
        limpar_tela()
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
            cpf = input('CPF do Cliente: ')
            editar_cliente(cpf)

        else:
            print('Opção inválida!')
            input('[ENTER] para continuar...')
