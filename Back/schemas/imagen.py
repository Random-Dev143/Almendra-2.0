from . import ma
from models.imagen import Imagen

class ImagenSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Imagen
        load_instance = True
