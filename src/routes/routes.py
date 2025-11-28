from flask import render_template, Blueprint
from flask_security import login_required
from flask_security import LoginForm

routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/")
def index():
    form = LoginForm()
    return render_template('security/login_user.html', login_user_form=form)
        # descomente essa linha caso nao seja necessario logar para acessar a pagina inicial
        # return render_template('index.html')
        
@routes_bp.route("/home")
@login_required
def home():
    return render_template('home.html')

@routes_bp.route("/jwt_login")
def jwt_login():
    return render_template('jwt_login.html')