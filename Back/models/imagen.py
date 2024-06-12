from . import db

class Imagen(db.Model):
    __tablename__ = 'imagenes'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)

    producto = db.relationship('Producto', back_populates='imagenes')
