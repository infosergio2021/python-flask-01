from flask import Flask, render_template, request, url_for, redirect
from flask_wtf.csrf import CSRFProtect

# creando instancias a utilizar
app = Flask(__name__)
csrf = CSRFProtect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form['usuario'])
    print(request.form['password'])
    """
    if request.method == 'POST':
        # print(request.form['usuario'])
        # print(request.form['password'])
        if request.form['usuario'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# renderizado de pagina de error 404 not found

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    # configuracion del servidor
    app.config.from_object(config)
    # inicializar csrf
    csrf.init_app(app)
    # manejador de errores
    app.register_error_handler(404, pagina_no_encontrada)
    return app
