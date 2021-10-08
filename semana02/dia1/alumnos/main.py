from flask import Flask,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'semana2'


mysql = MySQL(app)

@app.route('/')
def index():
    titulo = 'ALUMNOS'
    
    cursor = mysql.connection.cursor()
    
    cursor.execute('select * from alumnos')
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)
    
    context = {
        'titulo':titulo,
        'descripcion':'RELACIÓN DE ALUMNOS DEL CURSO DE PYTHON',
        'data': data
    }
    
    return render_template('index.html',**context)

if __name__ ==  '__main__':
    app.run(debug=True,port=5000)