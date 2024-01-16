# Importando a biblioteca necessária para conexão com banco de dados SQLite
import sqlite3

# Definindo o nome do arquivo do banco de dados ou criando um novo se não existir
db_file = 'exemplo.db'

# Tentando estabelecer uma conexão com o banco de dados
try:
    # Conectando ao banco de dados (se não existir, um novo será criado)
    connection = sqlite3.connect(db_file)

    # Criando um objeto cursor para executar comandos SQL
    cursor = connection.cursor()

    # Criando uma tabela de exemplo (se ainda não existir)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Inserindo dados de exemplo na tabela
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ('Exemplo', 'exemplo@email.com'))

    # Comitando as alterações no banco de dados
    connection.commit()

    # Consultando e exibindo os dados inseridos
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    print("Dados na tabela 'usuarios':")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    # Em caso de erro, imprimir mensagem de erro
    print(f"Erro na conexão com o banco de dados: {e}")

finally:
    # Fechando o cursor e a conexão, independentemente de ter havido erro ou não
    if cursor:
        cursor.close()
    if connection:
        connection.close()
