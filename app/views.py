from flask import render_template
from app import app


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/contato')
def Contato():
    page = 'contato.html'
    return render_template('contato.html')

@app.route('/sobre')
def Sobre():
    page = 'sobre.html'
    return render_template('sobre.html')
