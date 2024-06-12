from . import ma
from models.producto import Producto
from schemas.imagen import ImagenSchema

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        load_instance = True

    imagenes = ma.Nested(ImagenSchema, many=True)
