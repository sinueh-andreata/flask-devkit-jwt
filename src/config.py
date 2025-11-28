import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

#importando variaveis do .env e definindo configurações base
class ConfigBase:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# Configurações específicas para desenvolvimento 
class ConfigDev(ConfigBase):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

# Configurações específicas para produção
class ConfigProd(ConfigBase):
    DEBUG = False