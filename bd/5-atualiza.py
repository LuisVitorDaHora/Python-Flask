import sqlite3

# 1 - Conectar ao banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Atualizar os dados
id = 1 
cursor.execute(
    """
        UPDATE games SET genero = ?
        WHERE id = ?
    """,
    ('Aventura', id)
)

# 3 - Salvar as alterações
conexao.commit()
print("Dados atualizados com sucesso!")