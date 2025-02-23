import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1
# cursor.execute('CREATE TABLE IF NOT EXISTS alunos( \
#                id INT, \
#                nome VARCHAR(100), \
#                idade INT, \
#                curso VARCHAR(50) \
#                )') 

# 2
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (1, "Fernanda", 25, "Administração")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (2, "Sarah", 24, "Fisioterapia")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (3, "Camila", 35, "Computação")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (4, "Lorena", 43, "Jornalismo")')
# cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (5, "Priscila", 55, "Matemática")')

# 3
# dados = cursor.execute('SELECT * FROM alunos')
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# dados = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
# dados = cursor.execute('SELECT COUNT(*) FROM alunos')
# for aluna in dados:
#     print(aluna)

# 4
# cursor.execute('UPDATE alunos SET idade = 22 WHERE id = 1')
# cursor.execute('DELETE FROM alunos WHERE id = 2')

# 5
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes( \
#                id INT PRIMARY KEY, \
#                nome VARCHAR(100), \
#                idade INT, \
#                saldo FLOAT \
#                )') 

# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "Fernanda", 25, 1234.0)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Sarah", 24, 4567.80)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Camila", 35, 8901.0)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Lorena", 43, 234.56)')
# cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Priscila", 55, 789.10)')

# 6
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
# dados = cursor.execute('SELECT *, MAX(saldo) AS maximo FROM clientes')
# dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
# for cliente in dados:
#     print(cliente)

# 7
# cursor.execute('UPDATE clientes SET saldo = 2340.56 WHERE id = 4')
# cursor.execute('DELETE FROM clientes WHERE id = 1')

# 8
# Habilitar suporte a FOREIGN KEY no SQLite
# cursor.execute('PRAGMA foreign_keys = ON;')

# cursor.execute('CREATE TABLE IF NOT EXISTS compras( \
#                id INT PRIMARY KEY, \
#                cliente_id INT NOT NULL,\
#                produto VARCHAR(100), \
#                valor FLOAT, \
#                FOREIGN KEY (cliente_id) REFERENCES clientes (id) \
#                )') 

# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 2, "lápis", 1.20)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (2, 3, "caderno", 45.80)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (3, 2, "caneta", 8.10)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (4, 5, "borracha", 2.50)')
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (5, 4, "apontador", 7.10)')

dados = cursor.execute('SELECT nome, produto, valor FROM clientes \
                        INNER JOIN compras \
                        ON clientes.id = compras.cliente_id \
                        ')

for compra in dados:
    print(compra)

conexao.commit()
conexao.close 