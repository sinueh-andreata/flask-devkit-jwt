from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt
from flask import Blueprint, request, jsonify
from src.models.models import User
from functools import wraps

jwt_bp = Blueprint("jwt", __name__, url_prefix="/auth")

def roles_required(*required_roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()

            claims = get_jwt()
            user_roles = claims.get("roles", [])

            if not any(role in user_roles for role in required_roles):
                return jsonify(msg="Acesso negado"), 403

            return fn(*args, **kwargs)
        return decorator
    return wrapper

@jwt_bp.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(email=request.json["email"]).first()
    if not user or not user.check_password(request.json["password"]):
        return {"msg": "credenciais inválidas"}, 401

    roles = [role.name for role in user.roles]

    access_token = create_access_token(
        identity=(user.id),
        additional_claims={"roles": roles}
    )

    return {"access_token": access_token}