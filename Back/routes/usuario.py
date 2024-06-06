from flask import request, jsonify
from models.usuario import Usuario
from schemas.usuario import UsuarioSchema
from models import db
from routes import usuario_bp

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

@usuario_bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return usuarios_schema.jsonify(usuarios)

@usuario_bp.route('/', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()
    nombre = datos.get('nombre')
    email = datos.get('email')
    password = datos.get('password')

    nuevo_usuario = Usuario(nombre=nombre, email=email)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return usuario_schema.jsonify(nuevo_usuario), 201
