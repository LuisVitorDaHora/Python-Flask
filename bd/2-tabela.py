import sqlite3

# 1 - Conectando ao banco de dados
conexao = sqlite3.connect('titulo.db')

# 2 - Criando um cursor
cursor = conexao.cursor()

# 3 - Criando a tabela
cursor.execute(
    ''' 
        CREATE TABLE games(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL,
            genero TEXT NOT NULL
        );
    '''
)

# 4 - Fechando a conexão
conexao.close()
print("Tabela criada com sucesso!")