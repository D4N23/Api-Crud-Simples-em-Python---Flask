from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from src.constants.http_status_code import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
import validators
from src.database import User, db

auth = Blueprint("auth",__name__,url_prefix="/api/v1/auth")

# ROTA DE CRIAÇÃO DE USERS
@auth.post('/register')
def register():
    username = request.json['username']
    email =request.json['email']
    password = request.json['password']
    
    if len(password) < 8:
        return jsonify({'error': "Password is too short"}),HTTP_400_BAD_REQUEST
        
    if len(username) < 3:
        return jsonify({'error': "User is too short"}),HTTP_400_BAD_REQUEST
    
    if not username.isalnum() or "" in username:
        return jsonify({'error': "Username should be alphanumeric, also no spaces"}),HTTP_400_BAD_REQUEST   
    
    if not validators.email(email):
        return jsonify({'error': "Email is not valid"}),HTTP_400_BAD_REQUEST
    
    if User.queryfilter_by(email=email).first() is not None:
        return jsonify({'error': "Email is taken"}),HTTP_409_CONFLICT
    
    if User.queryfilter_by(username=username).first() is not None:
        return jsonify({'error': "UserName is taken"}),HTTP_409_CONFLICT
    
    pwd_hash = generate_password_hash(password)
    
    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({
        'user':{
            'refresh': refresh,
            'access': access,
            'username': user.username,
            'email': user.email
        }
    }),HTTP_200_OK

@auth.get("/me")
def me():
    return{"user":"me"}


