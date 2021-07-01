import mysql.connector

# host   => Onde está o banco de dados
# user   => O usuário que tem permissão de manipular o meu_banco
# passwd => Senha do user
# db     => Qual é o banco que vou acessar

conexao = mysql.connector.connect(
host = 'localhost',
user = 'admin',
passwd = 'admin',
db = 'meu_banco'
)

cursor = conexao.cursor()

# =================================== Inserindo dados no banco

nome = input('Nome do Cliente: ')
end = input('Endereço: ')
cpf = input('CPF: ')

sql = 'INSERT INTO clientes (nomes, enderecos, cpfs) VALUES (%s, %s, %s)'
val = (nome, end, cpf)

cursor.execute(sql, val)

conexao.commit()

print(f'{cursor.rowcount} dado inserido')
print(f'Dado inserido no id {cursor.lastrowid}')

# =================================== Exibir os Dados

sql = 'SELECT * FROM clientes'

cursor.execute(sql)

resultados = cursor.fetchall()

for r in resultados:
    print(r)


# ================================= Deletar dados do banco

apagar = input('Digite a ID a excuir: ')

sql = 'DELETE FROM clientes WHERE id = ' + apagar

cursor.execute(sql)

conexao.commit()

print(f'{cursor.rowcount} registro(s) apagado(s).')


# ========================== Editando valores do banco

novo_dado = '203.203.203-00'

quem_vai_mudar = input('Digite o ID do campo a ser alterado: ')

sql = f"UPDATE clientes SET cpfs= '{novo_dado}' WHERE id= '{quem_vai_mudar}'"

cursor.execute(sql)

conexao.commit()

print(f'{cursor.rowcount} linha(s) afetada(s).')
