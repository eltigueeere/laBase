from flask import Flask
from routes.routesLogin import  routes_login

app = Flask(__name__)

# Registrar las rutas
app.register_blueprint(routes_login)

if __name__ == "__main__":
    app.run(debug=True)