from flask import Blueprint, render_template, abort, current_app
from assets.common import db
from assets.usuarios import Usuario
import requests

panel_routes = Blueprint('panel_routes', __name__)

@panel_routes.route('/welcome')
@panel_routes.route('/welcome/<datosUser>')
def welcome(datosUser=None):
    
    usuario = current_app.config['usuario']
    nombre = usuario.nombre
    tipoUsuario = usuario.tipoUsuario
    return nombre

