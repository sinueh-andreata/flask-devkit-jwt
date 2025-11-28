from flask import Blueprint, jsonify, request, render_template
from flask_security import login_required
from flask_security.decorators import current_user, roles_accepted
from src.schemas.schemas import ProductSchema
from src.services.products_service import ProductsService
from src.extensions import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def home_products():
    return render_template('products/index.html')

@products_bp.route('/create', methods=['POST'])
@login_required
@roles_accepted('admin', 'user')
def create_product():
    schema = ProductSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session, current_user)
    product = service.save_product(dados)
    return jsonify(schema.dump(product)), 201

@products_bp.route('/list', methods=['GET'])
@login_required
@roles_accepted('admin', 'user')
def list_all_products():
    service = ProductsService(db.session, current_user)
    products = service.list_all_products()
    schema = ProductSchema(many=True)
    return jsonify(schema.dump(products)), 200

@products_bp.route('/list/<int:id>', methods=['GET'])
@login_required
@roles_accepted('admin', 'user')
def list_product(id):
    service = ProductsService(db.session, current_user)
    product = service.get_product(id)
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404

    schema = ProductSchema()
    return jsonify(schema.dump(product)), 200

@products_bp.route('/update/<int:id>', methods=['PUT'])
@login_required
@roles_accepted('admin', 'user')
def update_product(id):
    schema = ProductSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session, current_user)
    product = service.update_product(dados, id)
    
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404
    return jsonify(schema.dump(product)), 200

@products_bp.route('/delete/<int:id>', methods=['DELETE'])
@login_required
@roles_accepted('admin', 'user')
def delete_product(id):
    service = ProductsService(db.session, current_user)
    product = service.delete_product(id)
    
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404
    
    return jsonify({'message': 'Product deletado com sucesso'}), 200