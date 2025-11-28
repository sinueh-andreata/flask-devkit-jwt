from src.models.models import Product
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

class ProductsService:
    def __init__(self, db_session, current_user):
        self.db_session = db_session
        self.current_user = current_user
    
    def create_product(self, dados):
        return Product(**dados, user_id=self.current_user.id)

    def save_product(self, dados):
        product = self.create_product(dados)
        try:
            self.db_session.add(product)
            self.db_session.commit()
            return product
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        except IntegrityError as err:
            self.db_session.rollback()
            return jsonify({"error": "Erro de integridade ao cadastrar o product."}), 409
        except Exception as err:
            return jsonify({"error": 'erro interno do servidor'}), 500
        
    def list_all_products(self):
        return Product.query.all()
    
    def get_product(self, id):
        return self.db_session.query(Product).filter_by(id=id).first()
    
    def update_product(self, dados, id):
        product = self.db_session.query(Product).filter_by(
            id=id,
            user_id=self.current_user.id
        ).first()
        
        if not product:
            return None
        
        for key, value in dados.items():
            setattr(product, key, value)
            
        try:
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise e
        return product
    
    def delete_product(self, id):
        product = self.db_session.query(Product).filter_by(
            id=id,
            user_id=self.current_user.id
        ).first()
        
        if not product:
            return None
        
        try:
            self.db_session.delete(product)
            self.db_session.commit()
            return product
        except Exception as e:
            self.db_session.rollback()
            raise e