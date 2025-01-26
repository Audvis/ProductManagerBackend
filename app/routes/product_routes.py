from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Product, Category

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    name = data.get('name', '').strip()
    description = data.get('description', '').strip()
    price = data.get('price')
    stock = data.get('stock')
    category_id = data.get('category_id')

    # Validaciones
    if not name:
        return jsonify({'error': 'Name cannot be empty'}), 400
    if price is None or price <= 0:
        return jsonify({'error': 'Price must be a positive number'}), 400
    if stock is None or not isinstance(stock, int) or stock < 0:
        return jsonify({'error': 'Stock must be a non-negative integer'}), 400
    if not category_id or not Category.query.get(category_id):
        return jsonify({'error': 'Category ID must correspond to an existing category'}), 400

    new_product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id
    )
    db.session.add(new_product)
    db.session.commit()

    return jsonify({'message': 'Product successfully created'}), 201


@product_bp.route('/', methods=['GET'])
def list_products():
    products = Product.query.all()
    result = [p.to_dict() for p in products]  # Usa el método to_dict del modelo
    return jsonify(result), 200

@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    category_id = data.get('category_id')

    product = Product.query.get_or_404(id)

    if not all([name, price, stock, category_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category does not exist'}), 404

    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    product.category_id = category_id
    db.session.commit()

    return jsonify(product.to_dict()), 200


@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product successfully deleted'}), 200
