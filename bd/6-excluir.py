import sqlite3

# 1 - Conectar ao banco de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Excluir os dados
id = (1,2)

cursor.execute(
    """
        DELETE FROM games 
        WHERE id IN (?, ?)
    """,
    id
)

# 3 - Salvar as alterações
conexao.commit()

print("Dados excluídos com sucesso!")