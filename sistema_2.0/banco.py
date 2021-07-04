import mysql.connector

def consulta():
    conexao = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin',
    db='db_teste'
    )
    cursor = conexao.cursor()

    sql='SELECT * FROM clientes'

    cursor.execute(sql)
    resultados = cursor.fetchall()

    num_colunas = len(cursor.description)
    nome_colunas = [i[0] for i in cursor.description]

    dados = (resultados, nome_colunas)
    
    return dados
