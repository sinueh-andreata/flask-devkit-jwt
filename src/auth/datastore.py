from flask_security import SQLAlchemyUserDatastore
from ..extensions import db
from ..models.models import User, Role

# define o user_datastore para ser usado na configuração do Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)