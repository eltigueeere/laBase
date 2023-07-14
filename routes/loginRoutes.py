from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash, current_app
from assets.common import db
from assets.usuarios import Usuario
from routes.panelRoutes import panel_routes
import bcrypt, requests

login_routes = Blueprint('login_routes', __name__)


@login_routes.route('/crear-cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidoPaterno = request.form.get('apellido_paterno')
        apellidoMaterno = request.form.get('apellido_materno')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        cp = request.form.get('cp')
        password = request.form.get('password')

        # Encripta la contraseña antes de guardarla en la base de datos
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Verifica si el correo ya existe en la base de datos
        cursor = db.cursor()
        query = "SELECT * FROM usuarios WHERE correo = %s"
        cursor.execute(query, (correo,))
        result = cursor.fetchone()

        if result:
            error_message = "El correo ya está registrado"
            return render_template('usuarios/crearCuenta.html', error_message=error_message)

        # Inserta los datos en la base de datos y guarda la fecha y hora de creación
        query = "INSERT INTO usuarios (nombres, apellidoPaterno, apellidoMaterno, correo, telefono, cp, password, create_time) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())"
        cursor.execute(query, (nombres, apellidoPaterno, apellidoMaterno, correo, telefono, cp, hashed_password))
        db.commit()
        # Redirige a la página de login en caso de éxito
        return redirect(url_for('login_routes.login_form', name='usuarioCreado'))


    return render_template('usuarios/crearCuenta.html')

@login_routes.route('/login-form')
@login_routes.route('/login-form/<name>')
def login_form(name=None):
    if name == "usuarioCreado":
        error_message="Se ha creado la cuenta exitosamente. Ingresa con tu correo y contraseña"
        return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html', name=name)

@login_routes.route('/login', methods=['POST'])
def login():
    correo = request.form.get('correo')
    password = request.form.get('password')
    cursor = db.cursor()
    query = "SELECT * FROM usuarios WHERE correo = %s"
    cursor.execute(query, (correo,))
    result = cursor.fetchone()
    stored_password = result[7]  # Obtén la contraseña almacenada en la base de datos
    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
        usuario = Usuario(consulta=result)
        current_app.config['usuario'] = usuario
        return redirect(url_for('panel_routes.welcome', datosUser='user'))
    else:
        error_message = "Credenciales incorrectas"
        flash(error_message, 'danger')
        return render_template('login.html', error_message=error_message)

@login_routes.route('/')
def index():
    return ("Pagina de inicio")

"""
@login_routes.route('/login/')
@login_routes.route('/login/<name>')
def login_init(name=None):
    return render_template('landinPage.html', name=name)

@login_routes.route('/lalos')
def get_api_data():
    api_url = 'http://127.0.0.1:8000/v1/login/'

    try:
        response = requests.get(api_url)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})
"""
