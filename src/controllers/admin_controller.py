from flask import Blueprint, jsonify, request
from src.schemas.schemas import ProductSchema
from src.services.products_service import ProductsService
from src.extensions import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/create/products', methods=['POST'])
def create_product():
    schema = ProductSchema()
    try:
        dados = schema.load(request.get_json())
        service = ProductsService(db.session, current_user)
        product = service.save_product(dados)
        return jsonify(schema.dump(product)), 201
    except Exception as err:
        return jsonify({"error": 'erro interno do servidor'}), 500
