from flask import render_template
from aplicacao import app

@app.route('/home')
def ola():
	return render_template('index.html')

@app.route('/')
def pg_principal():
	return '<h1>Página Principal</h1>'

@app.route('/Outra')
def outra_pg():
	return '<h1>Outra Página</h1><p>escrevi algo aqui </p>'


app.run(debug = True)