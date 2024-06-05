from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Cargar configuración desde config.py
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definir el modelo de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre}

# Crear la base de datos y las tablas
with app.app_context():
     db.create_all()

# Ruta de prueba
@app.route('/api/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': '¡Hola, mundo!'})

# Ruta para obtener datos
@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    return jsonify({'usuarios': [usuario.to_dict() for usuario in usuarios]})

# Ruta para agregar un usuario
@app.route('/api/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()
    nuevo_usuario = Usuario(nombre=datos['nombre'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
