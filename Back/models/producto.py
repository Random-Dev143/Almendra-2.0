from . import db

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(128), nullable=False)
    nombre = db.Column(db.String(128), nullable=False)
    descripcion = db.Column(db.String(5000), nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    imagenes = db.relationship('Imagen', back_populates='producto', cascade='all, delete-orphan')
