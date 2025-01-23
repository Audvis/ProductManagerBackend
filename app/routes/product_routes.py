from flask import Blueprint, request, jsonify
from app.database import db
from app.models import Product, Category

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    category_id = data.get('category_id')

    if not all([name, price, stock, category_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify({'error': 'Category does not exist'}), 404

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
    result = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'stock': p.stock,
            'category': p.category.name
        }
        for p in products
    ]
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

    return jsonify({'message': 'Product successfully updated'}), 200

@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product successfully deleted'}), 200
