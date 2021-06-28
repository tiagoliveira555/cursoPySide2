from datetime import datetime


def cumprimentar(usuario):
    date = datetime.now()
    hora = int(date.strftime('%H'))

    if hora < 12:
        print(f'Bom dia, {usuario}!')
    elif hora < 18:
        print(f'Boa tarde, {usuario}!')
    else:
        print(f'Boa noite, {usuario}!')


def validar_usuario(usuario, senha):
    if usuario == 'admin' and senha == 'admin':
        print('Acesso permitido')
        return True
    else:
        print('Acesso não permitido')
        return False


print(f'{"SIS TEMA":_^40}\n')
us = input('Usuário: ')
pw = input('Senha: ')


if validar_usuario(us, pw) == True:
    cumprimentar(us)
