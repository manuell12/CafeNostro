#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_admin_producto import Producto

def Productos():
    """Retorna todos los Productos de la base de datos"""
    return Producto.all()

def getProductoId(id):
    """Retorna los datos de un Producto especificando su id"""
    producto = Producto()
    producto.id_producto = id
    return Producto.getProductoId(producto)

def UpdateDataProducto(id, nombre, descripcion, tipo, precio_neto, status, id_categoria):
    producto = Producto(id, nombre, descripcion, tipo, precio_neto, status, id_categoria)
    Producto.UpdateDataProducto(producto)

def UpdateStatusProducto(id, id_categoria):
    """Actualiza el estado de un Producto especificando su id"""
    producto = Producto(id_categoria)
    producto.id_categoria = id_categoria
    Producto.UpdateStatusProducto(producto)

def AddDataProducto(nombre, descripcion, tipo, precio_neto, status, id_categoria):
    """Agrega un Producto nuevo a la base de datos. Recibe como entrada todos los campos necesarios para su creacion"""
    producto = Producto(None, nombre, descripcion, tipo, precio_neto, status, int(id_categoria))
    Producto.AddDataProducto(producto)

def getProductoStatus(id_categoria):
    """Obtiene los Productos de la base de datos que tengan el mismo estado determinado por el parámetro entregado"""
    producto = Producto()
    producto.id_categoria = id_categoria
    return Producto.getProductoStatus(producto)

def deleteproducto(id):
    """Elimina un Producto de la base de datos"""
    producto = Producto()
    producto.id_Producto = id
    Producto.deleteproductos(producto)
