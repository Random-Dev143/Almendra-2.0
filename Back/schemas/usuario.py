from . import ma
from models.usuario import Usuario
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True

    password = fields.String(load_only=True)
