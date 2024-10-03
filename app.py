from flask import Flask, render_template, json, request, Response
import config
from exemplo_sql import listarPessoas, criarPessoa  # Importando as funções do exemplo_sql.py

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index/index.html')

@app.get('/sobre')
def sobre():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/listar')
def listar():
    pessoas = listarPessoas()  # Usando a função já definida para listar pessoas

    # Transformar o resultado em uma lista de dicionários
    lista = [{'id': pessoa['id'], 'nome': pessoa['nome']} for pessoa in pessoas]

    return json.jsonify(lista)

@app.post('/criar')
def criar():
    dados = request.json
    print(dados['id'])
    print(dados['nome'])
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)

