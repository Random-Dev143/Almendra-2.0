from flask import Blueprint, request, jsonify
from models.producto import Producto
from models.imagen import Imagen
from schemas.producto import ProductoSchema
from models import db

producto_bp = Blueprint('producto_bp', __name__)

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

@producto_bp.route('/', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    return productos_schema.jsonify(productos)

@producto_bp.route('/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return producto_schema.jsonify(producto)

@producto_bp.route('/', methods=['POST'])
def agregar_productos():
    datos = request.get_json()
    if not isinstance(datos, list):
        return jsonify({"error": "Se espera una lista de productos"}), 400
    
    nuevos_productos = []
    for datos_producto in datos:
        categoria = datos_producto.get('categoria')
        nombre = datos_producto.get('nombre')
        descripcion = datos_producto.get('descripcion')
        precio = datos_producto.get('precio')
        stock = datos_producto.get('stock')
        
        nuevo_producto = Producto(
            categoria=categoria,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        db.session.add(nuevo_producto)
        db.session.flush()  # Para obtener el ID del producto antes de hacer commit
        
        imagenes = datos_producto.get('imagenes', [])
        for img in imagenes:
            nueva_imagen = Imagen(url=img['url'], producto_id=nuevo_producto.id)
            db.session.add(nueva_imagen)
        
        nuevos_productos.append(nuevo_producto)
    
    db.session.commit()
    
    return productos_schema.jsonify(nuevos_productos), 201

@producto_bp.route('/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    datos = request.get_json()
    
    producto.categoria = datos.get('categoria', producto.categoria)
    producto.nombre = datos.get('nombre', producto.nombre)
    producto.descripcion = datos.get('descripcion', producto.descripcion)
    producto.precio = datos.get('precio', producto.precio)
    producto.stock = datos.get('stock', producto.stock)
    
    db.session.commit()
    
    return producto_schema.jsonify(producto)

@producto_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    # Eliminar imágenes asociadas
    Imagen.query.filter_by(producto_id=id).delete()
    
    # Eliminar el producto
    db.session.delete(producto)
    db.session.commit()
    
    return jsonify({"message": "Producto eliminado exitosamente"}), 200
