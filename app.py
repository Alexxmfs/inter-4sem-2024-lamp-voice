from flask import Flask, render_template, json, request, Response
import config
from exemplo_sql import listarDispositivos, listarLeituras, criarDispositivo, criarLeitura  # Importando as funções necessárias

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index/index.html')

@app.get('/home')
def home():
    return render_template('index/home.html')

@app.get('/sobre')
def sobre():
    return render_template('index/sobre.html', titulo='Sobre Nós')

@app.get('/listar-dispositivos')
def listar_dispositivos():
    dispositivos = listarDispositivos()  

    lista = [{'id_dispositivo': dispositivo['id_dispositivo'], 'nome': dispositivo['nome']} for dispositivo in dispositivos]

    return json.jsonify(lista)

@app.get('/listar-leituras')
def listar_leituras():
    leituras = listarLeituras()  

    lista = [
        {'id_leitura': leitura['id_leitura'], 'nome_dispositivo': leitura['nome_dispositivo'], 'consumo': leitura['consumo'], 'data': leitura['data']}
        for leitura in leituras
    ]

    return json.jsonify(lista)

@app.post('/criar-dispositivo')
def criar_dispositivo():
    dados = request.json
    nome = dados['nome']  
    criarDispositivo(nome)  
    return Response(status=204)

@app.post('/criar-leitura')
def criar_leitura():
    dados = request.json
    id_dispositivo = dados['id_dispositivo']  
    consumo = dados['consumo']  
    data = dados['data'] 
    criarLeitura(id_dispositivo, consumo, data) 
    return Response(status=204)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=True)
