#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from estadistica import Ui_Estadistica
import controller_estadistica as controller
import admin_productos.controller_admin_producto as controller_admin_producto

class Estadistica(QtGui.QWidget):
    def __init__(self):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Estadistica()
        self.ui.setupUi(self)
        self.setFocus()

        self.lista_ProductoVenta = list()

        ventas = controller.getVentas()
        for venta in ventas:
            venta_productos = controller.getProductosPedido(venta.id_pedido)
            for ventaProducto in venta_productos:
                objeto_producto_venta = controller.ProductoVenta(
                    controller_admin_producto.getProductoId(ventaProducto.id_producto)[0],
                    ventaProducto.cantidad,
                    ventaProducto.precio_venta,
                    venta.fecha)
                self.lista_ProductoVenta.append(objeto_producto_venta)

        for producto_venta in self.lista_ProductoVenta:
            print producto_venta.producto.nombre,producto_venta.cantidad,producto_venta.precio,producto_venta.fecha
            
