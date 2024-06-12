from flask import Flask
from config import Config
from models import db, bcrypt
from flask_migrate import Migrate
from flask_cors import CORS  
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
 
    from routes.usuario import usuario_bp
    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')

    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from routes.producto import producto_bp  
    app.register_blueprint(producto_bp, url_prefix='/api/productos')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
