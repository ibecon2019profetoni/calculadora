# inicalizamos librerias/dependencias
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        expression = request.form.get('expression')
        # si le dan al = sin poner nigún número vamos hacer que se ponga el 0
        if expression == '':
            expression = '0'

        try:
            result = round(eval(expression),4)
        except SyntaxError:
            result = '0'

        return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run('127.0.0.1', 5009, debug=True)
