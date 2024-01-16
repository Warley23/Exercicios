# Importando as bibliotecas necessárias
from flask import Flask, render_template, request, redirect
import sqlite3

# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados (SQLite neste exemplo)
db_file = 'app.db'

# Rota para exibir a lista de usuários
@app.route('/')
def listar_usuarios():
    # Conectando ao banco de dados
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Consultando todos os usuários
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    # Fechando a conexão
    connection.close()

    # Renderizando o template com a lista de usuários
    return render_template('lista_usuarios.html', usuarios=usuarios)

# Rota para adicionar um novo usuário
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        # Obtendo dados do formulário
        nome = request.form['nome']
        email = request.form['email']

        # Conectando ao banco de dados
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Inserindo um novo usuário no banco de dados
        cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
        connection.commit()

        # Fechando a conexão
        connection.close()

        # Redirecionando para a lista de usuários após adicionar
        return redirect('/')
    
    # Renderizando o formulário para adicionar um novo usuário
    return render_template('formulario.html', acao='Adicionar')

# Rota para editar um usuário existente
@app.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    # Conectando ao banco de dados
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    if request.method == 'POST':
        # Obtendo dados do formulário
        nome = request.form['nome']
        email = request.form['email']

        # Atualizando os dados do usuário no banco de dados
        cursor.execute('UPDATE usuarios SET nome=?, email=? WHERE id=?', (nome, email, usuario_id))
        connection.commit()

        # Fechando a conexão
        connection.close()

        # Redirecionando para a lista de usuários após editar
        return redirect('/')
    
    # Consultando os dados do usuário a ser editado
    cursor.execute('SELECT * FROM usuarios WHERE id=?', (usuario_id,))
    usuario = cursor.fetchone()

    # Fechando a conexão
    connection.close()

    # Renderizando o formulário para editar um usuário
    return render_template('formulario.html', acao='Editar', usuario=usuario)

# Rota para deletar um usuário
@app.route('/deletar/<int:usuario_id>')
def deletar_usuario(usuario_id):
    # Conectando ao banco de dados
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    # Deletando o usuário do banco de dados
    cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id,))
    connection.commit()

    # Fechando a conexão
    connection.close()

    # Redirecionando para a lista de usuários após deletar
    return redirect('/')

# Executando a aplicação
if __name__ == '__main__':
    app.run(debug=True)
