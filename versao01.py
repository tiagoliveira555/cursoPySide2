import os


def limpar_tela():
    os.system('cls')


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
    if us == 'Tiago' and pw == '123':
        return True

    return False


print(f'{" <<SYSCAD>> ":=^30} [V: 1.0]')
login = input('Usuário: ')
senha = input('Senha: ')

if validar_usuario(login, senha):
    print('MENU')
