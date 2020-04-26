from flask import render_template

from aplicacao import app

@app.route('/home')

def ola():
        return render_template('index.html')

app.run(debug=True)