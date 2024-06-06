from flask import Blueprint, request, jsonify
from models.usuario import Usuario
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = Usuario.query.filter_by(email=email).first()
    if user and user.check_password(password):
        
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    else:
        
        return jsonify({'error': 'Invalid credentials'}), 401
