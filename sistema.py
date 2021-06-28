from datetime import datetime


def cumprimentar():
    date = datetime.now()
    hora = int(date.strftime('%H'))

    if hora < 12:
        print('Bom dia!')
    elif hora < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')


def validar_usuario():
    pass


print(f'{"SIS TEMA":_^40}\n')
us = input('Usuário: ')
pw = input('Senha: ')

cumprimentar()
