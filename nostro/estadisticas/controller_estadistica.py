#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from PySide import QtCore, QtGui
from model_estadistica import VentaProducto, Venta
from admin_productos.model_admin_producto import Producto

def getProductosPedido(id_pedido):
    productos = VentaProducto()
    productos.id_pedido = id_pedido
    return VentaProducto.getProductosPedido(productos)

def getVentas():
    return Venta.all()

class ProductoVenta(object):
    producto = Producto()
    fecha = ""
    precio = 0
    cantidad = 0
    def __init__(
            self,
            producto=Producto(),
            cantidad=0,
            precio=0,
            fecha=""):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = int(precio)
        self.fecha = fecha
