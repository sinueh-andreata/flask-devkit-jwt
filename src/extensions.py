from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_security import Security
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager

jwt = JWTManager()
db = SQLAlchemy()
csrf = CSRFProtect()
security = Security()
ma = Marshmallow()
cors = CORS()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])