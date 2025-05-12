import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserir dados na tabela
cursor.execute(
    """
        INSERT INTO games (nome, ano, nota, genero)
        VALUES ('Elden Ring', 2022, 9.5, 'RPG')
    """
)
conexao.commit()
conexao.close()
print("Dados inseridos com sucesso!")
