from flask import Flask
from app.database import db
from app.routes import init_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

# Configurar CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Configuración
    app.config.from_object('app.config.Config')
    
    # Inicializar la base de datos
    db.init_app(app)

    # Registrar las rutas
    init_routes(app)

    return app
