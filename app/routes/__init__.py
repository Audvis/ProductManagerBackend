from flask import Blueprint, jsonify
from app.routes.category_routes import category_bp
from app.routes.product_routes import product_bp

# Ruta raíz usando un Blueprint
root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/')
def home():
    return jsonify({"message": "Welcome to ProductManager API!"})

def init_routes(app):
    # Registrar los Blueprints con prefijos
    app.register_blueprint(root_bp)  # Ruta raíz (/)
    app.register_blueprint(category_bp, url_prefix='/categories')  # Prefijo para categorías
    app.register_blueprint(product_bp, url_prefix='/products')  # Prefijo para productos
