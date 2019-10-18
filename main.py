# inicalizamos librerias/dependencias
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        num01 = int(request.form['num1'])
        num02 = int(request.form['num2'])
        operador = request.form['operador']
        
        if operador == '+':
            resultadoMAIN = num01 + num02
        elif operador == '-':
            resultadoMAIN = num01 - num02
        elif operador == '*':
            resultadoMAIN = num01 * num02
        elif operador == '/':
            resultadoMAIN = num01 / num02

        return render_template('index.html', resultado=resultadoMAIN)

    return render_template('index.html')


if __name__ == "__main__":
    app.run('127.0.0.1', 5009, debug=True)
