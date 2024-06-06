from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db, bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    from routes.usuario import usuario_bp
    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
