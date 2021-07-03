def validar_usuario(login, senha):
    if login == 'admin' and senha == 'admin':
        return True
    return False
