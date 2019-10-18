# inicalizamos librerias/dependencias
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# rutas
@app.route('/', methods=['GET', 'POST'])
def inicio():



if __name__ == "__main__":
    app.run('127.0.0.1', 5009, debug=True)
