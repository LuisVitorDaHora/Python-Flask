import sqlite3

# 1 - Conectar ao banco de dados
def conecta_banco():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2 - Inserir os dados
def insere_dados(nome, ano, nota, genero):
    conexao = conecta_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
            INSERT INTO games (nome, ano, nota, genero) 
            VALUES (?, ?, ?, ?)
        """,
        (nome, ano, nota, genero)
    )

    # 3 - Salvar as alterações
    conexao.commit()
    conexao.close()

# 3 - Listagem dos dados
def obter_dados():
    conexao = conecta_banco()
    cursor = conexao.cursor()

    cursor.execute(
        """
            SELECT * FROM games
        """
    )

    dados = cursor.fetchall()
    conexao.close()
    return dados