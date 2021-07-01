import mysql.connector

def conecta_ao_banco(banco):
    conexao = mysql.connector.connect(
        host='localhost',
        user='syscad',
        passwd='syscad',
        db = banco
    )

    return conexao

def insere_dados(conexao, nome, endereco, cpf):
    sql = 'INSERT INTO clientes(nome, endereco, cpf) VALUE (%s, %s, %s)'
    val = (nome, endereco, cpf)

    try:
        cursor = conexao.cursor()
        cursor.execute(sql, val)
        conexao.commit()

        cursor.close()
        conexao.close()

    except mysql.connector.Error as erro:
        if erro.errno == 1062: #Já existe CPF
            print('CPF já cadastrado!')

def exibir_relatorio(conexao):
    sql = 'SELECT * FROM clientes'

    cursor = conexao.cursor()
    cursor.execute(sql)

    resultados = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultados

def excluir_dados(conexao, id):
    sql = f"DELETE FROM clientes WHERE id={id}"

    cursor = conexao.cursor()
    cursor.execute(sql)

    conexao.commit()

    cursor.close()
    conexao.close()

def pesquisar_cliente(conexao, cpf=None, nome=None):
    sql = f"SELECT * FROM clientes WHERE cpf LIKE '%{cpf}%'"

    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado
