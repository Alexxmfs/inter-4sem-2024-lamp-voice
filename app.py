from flask import Flask, render_template, json, request, Response
import config

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index/index.html')

@app.get('/sobre')
def sobre():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/listar')
def listar():
    lista = [
        { 'id': 1, 'nome': 'Nome 1' },
        { 'id': 2, 'nome': 'Nome 2' }
	]
    return json.jsonify(lista)

@app.post('/criar')
def criar():
    dados = request.json
    print(dados['id'])
    print(dados['nome'])
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
