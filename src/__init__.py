from flask import Flask
from .config import ConfigDev
from .extensions import db, csrf, security, ma, cors, limiter, jwt
from .models.models import create_default_roles, create_default_users
from src.auth.datastore import user_datastore  
from src.auth import init_app as init_auth
from src.routes.routes import routes_bp
from controllers.products_controller import products_bp
from auth.jwt_auth import jwt_bp

from .auth import auth

def create_app(config_class=ConfigDev):
    app = Flask(__name__, template_folder="templates")

    app.config.from_object(config_class)

    # inicializa as extensoes do extensions.py
    db.init_app(app)
    csrf.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)
    
    # configuração do Flask-Security
    security.init_app(app, user_datastore)

    # inicializa o modulo de autenticação
    auth.init_app(app)

    # importando rotas 
    app.register_blueprint(routes_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(jwt_bp)

    # Cria todas as tabelas do banco de dados automaticamente
    with app.app_context():
        db.create_all()
        create_default_roles() # cria roles defaults
        create_default_users() # cria users defaults
        
    return app