import os

from termcolor import colored
from prettytable import PrettyTable
from progressbar import ProgressBar
from time import sleep
from getpass import getpass

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

    t = PrettyTable(['NOME', 'ENDEREÇO', 'CPF'])
    for p in range(len(Nomes)):
        t.add_row([Nomes[p], Enderecos[p], Cpfs[p]])

    print(t)

    input('[ENTER] para continuar...')

def pesquisar_cliente(cpf=None, nome=None):
    global Cpfs
    limpar_tela()
    print('PESQUISANDO >>>>>\n')

    if cpf in Cpfs:
        return Cpfs.index(cpf)
    return -1     # não encontrou o cpf

def excluir_cliente(cpf):
    c = pesquisar_cliente(cpf)
    print(colored('EXCLUIDO >>>>>>\n', 'red'))

    if c != -1:
        print(colored('Tem certeza que deseja excluir?', 'yellow', 'on_red'))
        print(f'Nome: {Nomes[c]} :: CPF: {Cpfs[c]}')
        i = input('[S/N]: ')
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

def exibir_menu():
    print('|================ MENU ================|')
    menu_principal = PrettyTable(['OPÇÃO', 'ITEM'])
    menu_principal.align['ITEM'] = 'l' # L de Left
    menu_principal.add_row(['1', 'CADASTRAR                   '])
    menu_principal.add_row(['2', 'RELATÓRIO'])
    menu_principal.add_row(['3', 'PESQUISAR'])
    menu_principal.add_row(['4', 'EXCLUIR'])
    menu_principal.add_row(['5', 'EDITAR'])



    menu_principal.add_row(['0', 'SAIR'])

    print(menu_principal)

def loading():
    print('Carregando módulos\nPor favor, agurde!\n')
    barra = ProgressBar()
    for i in barra(range(25)):
        sleep(0.1)
# ====================================================


Nomes = []
Enderecos = []
Cpfs = []

loading()

print(colored(f'{">> SYSCAD <<":=^40}', "green"))
login = input('Usuário: ')
senha = getpass('Senha: ')

if validar_usuario(login, senha):
    while True:
        limpar_tela()
        exibir_menu()

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
