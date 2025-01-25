from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Category

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/', methods=['POST'])
def create_category():
    data = request.json
    name = data.get('name', '').strip()

    # Validación
    if not name:
        return jsonify({'error': 'Name cannot be empty'}), 400

    new_category = Category(name=name)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({'message': 'Category successfully created'}), 201


@category_bp.route('/', methods=['GET'])
def list_categories():
    categories = Category.query.all()
    result = [{'id': c.id, 'name': c.name} for c in categories]
    return jsonify(result), 200

@category_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Category name is required'}), 400

    category = Category.query.get_or_404(id)
    category.name = name
    db.session.commit()

    return jsonify({'message': 'Category successfully updated'}), 200

@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()

    return jsonify({'message': 'Category successfully deleted'}), 200
