from flask import Blueprint, jsonify, request
from src.schemas.schemas import ProductSchema
from src.services.products_service import ProductsService
from src.extensions import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.auth.jwt_auth import roles_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/create/products', methods=['POST'])
@roles_required('admin')
def create_product():
    schema = ProductSchema()
    try:
        dados = schema.load(request.get_json())
        user_id = get_jwt_identity()
        service = ProductsService(db.session, user_id)
        product = service.save_product(dados)
        return jsonify(schema.dump(product)), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except IntegrityError:
        return jsonify({"error": "Produto já existe"}), 409
    except Exception:
        return jsonify({"error": "Erro interno do servidor"}), 500

