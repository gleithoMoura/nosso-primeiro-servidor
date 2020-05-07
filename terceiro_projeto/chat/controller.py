from aplicacao import app
from flask import render_template

@app.route('/')
def index():
	contexto = {'titulo': 'index', 
	'mensagens': ['usuario1: ola', 'usuario2: ola']}
	return render_template('index.html', **contexto)

@app.route('/enviar')
def enviar():
	contexto = {'titulo': 'Enviar mensagem'}
	return render_template('mansagem.html', **contexto)

app.run(debug = True)