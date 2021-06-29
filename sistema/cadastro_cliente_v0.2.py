def limpar_tela():
    print('')


def cadastrar_cliente():
    limpar_tela()
    print('Cadastrando....')
    input('[ENTER] para continuar...')


def exibir_cliente():
    limpar_tela()
    print('Relatório....')
    input('[ENTER] para continuar...')


def pesquisar_cliente():
    limpar_tela()
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
            cadastrar_cliente()
        elif op == '2':
            exibir_cliente()
        elif op == '3':
            pesquisar_cliente()
        elif op == '4':
            excluir_cliente()
        elif op == '5':
            editar_cliente()
        else:
            print('Opção inválida!')
            input('[ENTER] para continuar...')
