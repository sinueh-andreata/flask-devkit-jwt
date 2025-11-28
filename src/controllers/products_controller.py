from flask import Blueprint, jsonify, request, render_template
from src.schemas.schemas import ProductSchema
from src.services.products_service import ProductsService
from src.extensions import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def home_products():
    return render_template('products/index.html')

@products_bp.route('/create', methods=['POST'])
def create_product():
    schema = ProductSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session)
    product = service.save_product(dados)
    return jsonify(schema.dump(product)), 201

@products_bp.route('/list', methods=['GET'])
def list_all_products():
    service = ProductsService( db.session)
    products = service.list_all_products()
    schema = ProductSchema(many=True)
    return jsonify(schema.dump(products)), 200

@products_bp.route('/list/<int:id>', methods=['GET'])
def list_product(id):
    service = ProductsService(db.session)
    product = service.get_product(id)
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404

    schema = ProductSchema()
    return jsonify(schema.dump(product)), 200

@products_bp.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    schema = ProductSchema()
    dados = schema.load(request.get_json())
    service = ProductsService(db.session)
    product = service.update_product(dados, id)
    
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404
    return jsonify(schema.dump(product)), 200

@products_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    service = ProductsService(db.session)
    product = service.delete_product(id)
    
    if not product:
        return jsonify({'message': 'Product não encontrado'}), 404
    
    return jsonify({'message': 'Product deletado com sucesso'}), 200