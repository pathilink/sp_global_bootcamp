import sqlite3

conexao = sqlite3.connect('banco') # conexão com o bd
cursor = conexao.cursor()            

# cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INT, \
#                                                     nome VARCHAR(100), \
#                                                     endereco VARCHAR(100), \
#                                                     email VARCHAR(100));\
#                                                     ') 

# cursor.execute('CREATE TABLE IF NOT EXISTS produtos(id INT, \
#                                                     nome VARCHAR(100), \
#                                                     endereco VARCHAR(100), \
#                                                     email VARCHAR(100));\
#                                                     ') 

# cursor.execute('CREATE TABLE IF NOT EXISTS gerentes (id INT, \
#                                                     nome VARCHAR(100), \
#                                                     endereco VARCHAR(100), \
#                                                     email VARCHAR(100));\
#                                                     ') 

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# cursor.execute('DROP TABLE produtos')

# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, "Isadora", "França", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria", "Salvador", "maria@gmail.com", 789012)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(3, "José", "Curitiba", "jose@gmail.com", 345678)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(4, "Márcia", "São Paulo", "marcia@gmail.com", 901234)')

# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(4, "Márcia", "São Paulo", "marcia@gmail.com")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(1, "João", "São Paulo", "joao@gmail.com")')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, "Cíntia", "Inglaterra", "cintia@gmail.com")')

# cursor.execute('DELETE FROM usuario WHERE id = 1')

# cursor.execute('UPDATE usuario SET endereco = "Belo Horizonte" WHERE nome = "José"')

# dados = cursor.execute('SELECT * FROM gerentes')
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id')

dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)



conexao.commit() # envia as infos
conexao.close    # finaliza processo