import sqlite3
from flask import Flask, jsonify, request

#Criando conexão com o DB, criando tabela e fechando a conexão;
app = Flask(__name__)
conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Dados (idRegistro INT, ValorRegistro VARCHAR(5000))")
conn.close()

# POST
@app.route('/dados', methods=['POST'])
def inserDados():
    dados = request.get_json()
    conn = sqlite3.connect('sqlite.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Dados (idRegistro, ValorRegistro) VALUES (?, ?)", (dados['campo1'], dados['campo2']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Dados adicionados com sucesso!'})

# GET
@app.route('/dados', methods=['GET'])
def obter_dados():
    conn = sqlite3.connect('sqlite.db.')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dados")
    dados = cursor.fetchall()
    conn.close()
    return jsonify({'dados': dados})

if __name__ == '__main__':
    app.run(port=5000)