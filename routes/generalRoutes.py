from flask import Blueprint, render_template, abort
from assets.common import db
import requests

general_routes = Blueprint('general_routes', __name__)




@general_routes.route('/')
def index():
    return ("Pagina de inicio")


# PAGINAS DE ERROR
# Ruta para manejar errores 404
@general_routes.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error_message="Página no encontrada"), 404

@general_routes.route('/ruta-inexistente')
def nonexistent_route():
    abort(404)  # Lanza el error 404 si se accede a esta ruta
