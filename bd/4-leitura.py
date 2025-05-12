import sqlite3

# 1 - Conexão com o banco de dados SQLite
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Ler dados da tabela
dados = cursor.execute(
    """
        SELECT * FROM games
    """
)

print(dados.fetchall())

