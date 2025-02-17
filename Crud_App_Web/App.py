#Importamos librerias
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)


##Se crea la conxion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskcontact'

mysql = MySQL(app)

#iniciamos sesion
app.secret_key = 'mysecretkey'

##Se crea seccion inicial y se llama a la pagina index.html
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html')

##Se crea ventana de añadir contacto y se conecta con el formulario
@app.route('/añadir', methods=['POST'])
def añadir_contacto():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        #creamos conector para enviar los datos a la base de datos
        cur = mysql.connection.cursor()
        cur.execute('insert into contacts (fullname, phone, email) values (%s, %s, %s)', (fullname, phone, email))
        #ejecutamos la consulta
        mysql.connection.commit()
        #Este mensaje muestra cuando se agrega de forma correcta a la base de datos
        flash('El contacto se agrego de forma correcta')
        return redirect(url_for('Index'))



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