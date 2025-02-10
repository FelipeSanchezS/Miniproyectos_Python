from flask import Flask

app = Flask(__name__)

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