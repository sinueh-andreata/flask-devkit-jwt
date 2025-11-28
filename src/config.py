import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

#importando variaveis do .env e definindo configurações base
class ConfigBase:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = "argon2"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) 
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = True
    
    # Configurações do CSRF
    WTF_CSRF_TIME_LIMIT = 3600
    WTF_CSRF_SSL_STRICT = False
    
    # Configurações do Flask-Security
    SECURITY_TRACKABLE = False
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_RECOVERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_EMAIL_SENDER = False
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    SECURITY_POST_LOGIN_VIEW = '/home'
    # Templates customizados do Flask-Security
    SECURITY_FORGOT_PASSWORD_TEMPLATE = 'security/reset_password.html'
    SECURITY_LOGIN_USER_TEMPLATE = 'security/login_user.html'
    SECURITY_REGISTER_USER_TEMPLATE = 'security/register_user.html'

# Configurações específicas para desenvolvimento 
class ConfigDev(ConfigBase):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

# Configurações específicas para produção
class ConfigProd(ConfigBase):
    DEBUG = False