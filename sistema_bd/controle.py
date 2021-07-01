import modelo as db


DB_CLIENTES = 'syscad'


def cadastrar_cliente(nome, endereco, cpf):
    con = db.conecta_ao_banco(DB_CLIENTES)
    db.insere_dados(con, nome, endereco, cpf)


def exibir_clientes():
    con = db.conecta_ao_banco(DB_CLIENTES)
    res = db.exibir_relatorio(con)
    return res


def pesquisar_cliente(cpf=None, nome=None):
    con = db.conecta_ao_banco(DB_CLIENTES)
    res = db.pesquisar_cliente(con, cpf)

    return res


def excluir_clientes(cpf):
    res = pesquisar_cliente(cpf)

    if res != None:
        linha = 0
        if len(res) > 1:
            print('Foi encontrado mais de um valor')
            id = int(input('Digite um ID: '))

            while linha < len(res):
                if res[linha][0] == id:
                    break
                linha += 1

        print('Tem certeza que deseja excluir?')
        print(f'Nome: {res[linha][1]} :: CPF: {res[linha][3]}')
        i = input('[S] Sim >  ')
        if i.lower() == 's':
            con = db.conecta_ao_banco(DB_CLIENTES)
            db.excluir_dados(con, res[linha][0])
            print('Dados excluidos com sucesso!')
