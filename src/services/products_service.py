from src.models.models import Product
from sqlalchemy.exc import IntegrityError

class ProductsService:
    def __init__(self, db_session, user_id: int):
        self.db_session = db_session
        self.user_id = user_id

    def create_product(self, dados):
        return Product(**dados, user_id=self.user_id)

    def save_product(self, dados):
        product = self.create_product(dados)
        try:
            self.db_session.add(product)
            self.db_session.commit()
            return product
        except IntegrityError:
            self.db_session.rollback()
            raise  # deixa o controller tratar o erro
        except Exception:
            self.db_session.rollback()
            raise

    def list_all_products(self):
        return Product.query.all()

    def get_product(self, id):
        return self.db_session.query(Product).filter_by(id=id).first()

    def update_product(self, dados, id):
        product = self.db_session.query(Product).filter_by(
            id=id,
            user_id=self.user_id
        ).first()

        if not product:
            return None

        for key, value in dados.items():
            setattr(product, key, value)

        try:
            self.db_session.commit()
            return product
        except Exception:
            self.db_session.rollback()
            raise

    def delete_product(self, id):
        product = self.db_session.query(Product).filter_by(
            id=id,
            user_id=self.user_id
        ).first()

        if not product:
            return None

        try:
            self.db_session.delete(product)
            self.db_session.commit()
            return product
        except Exception:
            self.db_session.rollback()
            raise
