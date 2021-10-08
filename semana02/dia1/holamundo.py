from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>HOLA MUNDO FLASK</h1>'

@app.route('/alumnos')
def alumnos():
    return '<h2>LISTADO DE ALUMNOS</h2>'

app.run(debug = True)