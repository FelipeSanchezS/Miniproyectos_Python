from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_db'] = 'flaskcontact'

mysql = MySQL(app)


@app.route('/')
def Index():
    return 'Hello World'

@app.route('/añadir')
def añadir_contacto():
    return 'Sección de añadir contacto'

@app.route('/editar')
def editar_contacto():
    return 'Sección editar contacto'

@app.route('/eliminar')
def eliminar_contacto():
    return 'Sección eliminar contacto'

if __name__ == '__main__':
    app.run(port=3000, debug = True)