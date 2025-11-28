from datetime import datetime
import uuid
from src.extensions import db
from argon2 import PasswordHasher

class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))
    
roles_users = RolesUsers.__table__
    
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model,):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
        
    def check_password(self, password):
        return verify_password(password, self.password)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))     
    user = db.relationship('User', backref=db.backref('products', lazy=True))

def create_default_roles():
    default_roles = ['admin', 'user', 'root']
    for role_name in default_roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            role = Role(name=role_name)
            db.session.add(role)
    db.session.commit()

def create_default_users():
    ph = PasswordHasher()

    default_users = [
        {
            # users
            'email': 'user@mail.com',
            'password': 'userpassword123',
            'active': True,
            'confirmed_at': datetime.utcnow(),
            'fs_uniquifier': str(uuid.uuid4()),
            'roles': ['user']
        },
        {
            # admins
            'email': 'admin@mail.com',
            'password': 'adminpassword123',
            'active': True,
            'confirmed_at': datetime.utcnow(),
            'fs_uniquifier': str(uuid.uuid4()),
            'roles': ['admin']
        },
        {
            # roots
            'email': 'root@mail.com',
            'password': 'rootpassword123',
            'active': True,
            'confirmed_at': datetime.utcnow(),
            'fs_uniquifier': str(uuid.uuid4()),
            'roles': ['root']
        }
    ]

    create_default_roles()
    for u in default_users:
        existing_user = User.query.filter_by(email=u['email']).first()
        if existing_user:
            continue

        hashed_password = hash_password(u['password'])

        user = User(
            email=u['email'],
            password=hashed_password,
            active=u.get('active', True),
            confirmed_at=u.get('confirmed_at', datetime.utcnow()),
            fs_uniquifier=u.get('fs_uniquifier', str(uuid.uuid4()))
        )

        for role_name in u.get('roles', []):
            role = Role.query.filter_by(name=role_name).first()
            if role:
                user.roles.append(role)

        db.session.add(user)

    db.session.commit()
