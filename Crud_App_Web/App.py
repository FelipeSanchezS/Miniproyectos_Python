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
    ##Acá llamamos los registros de la base de datos y hacemos que se envien al html index
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html' , contacts = data)

##Se crea ventana de añadir contacto y se conecta con el formulario, junto con el proceso de insert 
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



##Se crea ventana de editar contacto, el string es porque recibe un parametro que es el ID de contact
@app.route('/editar/<string:id>')
def obtener_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template ('editar.html', contact = data[0])



##Se crea ventana de eliminar contacto y se hace todo el proceso, el string es porque recibe un parametro que es el ID de contact
@app.route('/eliminar/<string:id>')
def eliminar_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado correctamente')
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port=3000, debug = True)