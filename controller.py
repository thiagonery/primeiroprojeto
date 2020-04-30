from flask import render_template

from aplicacao import app

@app.route('/home')

def ola():
        retorno = render_template(
                'index.html', 
                title='PaginaFlask',
                outra = 'novo texto',
                lista = ['a','b','c']
                )

        return retorno

@app.route('/')

def pagina_principal():
        return '<h1> pagina principal </h1><p> ola </p>'

@app.route('/outrapagina')

def outra_pagina():
        return '<h1> Outra pagina </h1>'        

app.run(debug=True)
