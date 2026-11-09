from flask import request, jsonify
from app import api, db
from models.producto import Producto
from sqlalchemy import exc

@api.route("/api/v1/productos/", methods=['POST'])
def crearProducto():
    try:
        datos = request.get_json(force=True)
        producto = Producto(
            proCodigo=datos['proCodigo'],
            proNombre=datos['proNombre'],
            proPrecio=datos['proPrecio'],
            proCategoria=datos['proCategoria']
        )
        db.session.add(producto)
        db.session.commit()
        return jsonify({"mensaje": 'Producto Agregado correctamente', "Producto": producto.to_dict()}), 201
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        return jsonify({"mensaje": str(error)}), 400

@api.route("/api/v1/productos/", methods=['GET'])
def obtenerProductos():
    try:
        productos = Producto.query.all()
        listaProductos = [p.to_dict() for p in productos]
        return jsonify({"mensaje": 'Productos', "Productos": listaProductos}), 200
    except exc.SQLAlchemyError as error:
        return jsonify({"mensaje": str(error)}), 500

@api.route("/api/v1/productos/<int:idProducto>", methods=['GET'])
def obtenerProductoPorID(idProducto):
    try:
        producto = Producto.query.get(idProducto)
        if producto is None:
            return jsonify({"mensaje": "No existe producto con ese ID"}), 404
        return jsonify({"mensaje": "Producto encontrado", "Producto": producto.to_dict()}), 200
    except exc.SQLAlchemyError as error:
        return jsonify({"mensaje": str(error)}), 500

@api.route("/api/v1/productos/<int:idProducto>", methods=['PUT'])
def actualizarProducto(idProducto):
    try:
        producto = Producto.query.get(idProducto)
        if producto is None:
            return jsonify({"mensaje": "No existe producto con ese ID"}), 404
        
        datos = request.get_json(force=True)
        producto.proCodigo = datos['proCodigo']
        producto.proNombre = datos['proNombre']
        producto.proPrecio = datos['proPrecio']
        producto.proCategoria = datos['proCategoria']
        
        db.session.commit()
        return jsonify({"mensaje": "Producto actualizado", "Producto": producto.to_dict()}), 200
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        return jsonify({"mensaje": str(error)}), 500

@api.route("/api/v1/productos/<int:idProducto>", methods=['DELETE'])
def eliminarProducto(idProducto):
    try:
        producto = Producto.query.get(idProducto)
        if producto is None:
            return jsonify({"mensaje": "No existe producto con ese ID"}), 404
        
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"mensaje": "Producto Eliminado"}), 200
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        return jsonify({"mensaje": str(error)}), 500