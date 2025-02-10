#Importamos librerias
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

##Se crea la conxion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_db'] = 'flaskcontact'

mysql = MySQL(app)

##Se crea seccion inicial y se llama a la pagina index.html
@app.route('/')
def Index():
    return render_template('index.html')

##Se crea ventana de añadir contacto
@app.route('/añadir', methods=['POST'])
def añadir_contacto():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        return 'dato recibido'

##Se crea ventana de editar contacto
@app.route('/editar')
def editar_contacto():
    return 'Sección editar contacto'

##Se crea ventana de eliminar contacto
@app.route('/eliminar')
def eliminar_contacto():
    return 'Sección eliminar contacto'

if __name__ == '__main__':
    app.run(port=3000, debug = True)