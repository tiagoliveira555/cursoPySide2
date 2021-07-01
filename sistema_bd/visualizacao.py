import controle as c

#c.cadastrar_cliente('Julio da Silva', 'Rua X', '222.222.222-22')
#c.cadastrar_cliente('Tereza de Alcantara', 'Rua B', '888.888.888-88')

print(c.exibir_clientes())

print('=============================================================')

#print(c.pesquisar_cliente(cpf=888))

print('=============================================================')

c.excluir_clientes('888')
