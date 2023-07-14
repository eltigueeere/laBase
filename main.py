from flask import Flask
from routes.loginRoutes import  login_routes
from routes.generalRoutes import general_routes
from routes.panelRoutes import panel_routes
from assets.usuarios import Usuario
app = Flask(__name__)

# Registrar las rutas
app.register_blueprint(login_routes)
app.register_blueprint(general_routes)
app.register_blueprint(panel_routes)
app.secret_key = 'jegm031194'

app.config['usuario'] = Usuario
if __name__ == "__main__":
    app.run(debug=True)