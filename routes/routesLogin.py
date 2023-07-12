from flask import Blueprint, render_template, jsonify
import requests

routes_login = Blueprint('routes_login', __name__)

@routes_login.route('/')
def index():
    return ("Pagina de inicio")

@routes_login.route('/login/')
@routes_login.route('/login/<name>')
def login_init(name=None):
    return render_template('landinPage.html', name=name)

@routes_login.route('/lalos')
def get_api_data():
    api_url = 'http://127.0.0.1:8000/v1/login/'

    try:
        response = requests.get(api_url)
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})
