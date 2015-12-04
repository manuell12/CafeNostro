#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from PySide import QtCore, QtGui
from admin_productos.model_admin_producto import Producto
from model_venta import Pedido, VentaProducto, Venta, Pago
import admin_productos.controller_admin_producto as controller_admin_producto

def Productos():
    """Retorna todos los Productos de la base de datos"""
    return Producto.all()

def getPedidos():
    """Retorna todos los pedidos"""
    return Pedido.all()

def getVentas():
    """Retorna todos los pedidos"""
    return Venta.all()

def getVentaPedidoId(id_pedido):
    venta = Venta()
    venta.id_pedido = id_pedido
    return Venta.getVentaPedidoId(venta)

def getProductoStatus(status):
    """Obtiene los Productos de la base de datos que tengan el mismo estado determinado por el parámetro entregado"""
    producto = Producto()
    producto.status = status
    return Producto.getProductoStatus(producto)

def getProductoCategoria(categoria):
    """Obtiene los Productos de la base de datos que tengan la misma categoria determinado por el parámetro entregado"""
    producto = Producto()
    producto.id_categoria = categoria
    return Producto.getProductoCategoria(producto)

def getProductoCodigo(codigo):
    """Obtiene el producto determinado por su codigo"""
    producto = Producto()
    codigo = codigo+"%"
    producto.codigo = codigo
    return Producto.getProductoCodigo(producto)

def getProductoId(id_producto):
    """Obtiene los Productos de la base de datos que tengan el mismo id determinado por el parámetro entregado"""
    producto = Producto()
    producto.id_producto = id_producto
    return Producto.getProductoId(producto)

def addDataPedido(mesa):
    """Agrega un pedido a la base de datos y retorna el id"""
    en_curso = 1
    pedidos = len(getPedidos())
    pedido = Pedido(pedidos,mesa,en_curso)
    Pedido.addDataPedido(pedido)
    return pedidos

def addDataPago(pago_total, efectivo, tarjeta, propina, id_venta):
    """Agrega un pedido a la base de datos y retorna el id"""
    pago = Pago(None, pago_total, efectivo, tarjeta, propina, id_venta)
    Pago.addDataPago(pago)

def addDataVentaProducto(id_pedido, id_producto, precio_venta):
    """Agrega un producto a un pedido"""
    venta_producto = VentaProducto()
    venta_producto.id_pedido = id_pedido
    venta_producto.id_producto = id_producto
    venta_producto.precio_venta = precio_venta
    venta_producto.cantidad = 1
    venta_producto.porcentaje_descuento = 0
    if(hayProductoPedido(id_pedido,id_producto)):
        cambiarCantidadProducto(id_pedido,id_producto,"aumentar")
    else:
        VentaProducto.addDataVentaProducto(venta_producto)

def getProductosPedido(id_pedido):
    """Obtiene todos los productos de un pedido"""
    venta_producto = VentaProducto()
    venta_producto.id_pedido = id_pedido
    return VentaProducto.getProductosPedido(venta_producto)

def hayProductoPedido(id_pedido, id_producto):
    """Retorna True si existe un producto en un pedido"""
    venta_producto = VentaProducto()
    venta_producto.id_producto = id_producto
    venta_producto.id_pedido = id_pedido
    producto = VentaProducto.hayProductoPedido(venta_producto)
    try:
        intentar = producto[0]
        return True
    except:
        return False

def hayProducto(id_producto):
    """Retorna True si existe un producto en la tabla de venta"""
    venta_producto = VentaProducto()
    venta_producto.id_producto = id_producto
    producto = VentaProducto.hayProducto(venta_producto)
    try:
        intentar = producto[0]
        return True
    except:
        return False

def cambiarCantidadProducto(id_pedido, id_producto, cambiar):
    """
    Cambia la cantidad de un producto depentiendo el parámetro 'cambiar':
    cambiar="aumentar": aumenta en 1 la cantidad del producto.
    cambiar="disminuir": disminuye en 1 la cantidad del producto.
    Si la cantidad llega a 0, elimina el producto.
    retorna True si realizo el cambio satisfactoriamente y retorna False en caso contrario.
    """
    venta_producto = VentaProducto()
    venta_producto.id_producto = id_producto
    venta_producto.id_pedido = id_pedido
    VentaProducto.cambiarCantidadProducto(venta_producto,cambiar)
    try:
        cantidad = VentaProducto.hayProductoPedido(venta_producto)[0].cantidad
    except:
        return False
    if(cantidad <= 0):
        deleteProducto(id_pedido,id_producto)
    return True

def deleteProducto(id_pedido, id_producto):
    """Elimina un Producto de la base de datos"""
    venta_producto = VentaProducto()
    venta_producto.id_producto = id_producto
    venta_producto.id_pedido = id_pedido
    VentaProducto.deleteProducto(venta_producto)

def addDataVenta(fecha,num_documento,tipo,total_pago,id_usuario,id_pedido):
    """Agrega una venta a la base de datos y retorna el id"""
    venta = Venta(None,fecha,num_documento,tipo,total_pago,id_usuario,id_pedido)
    Venta.addDataVenta(venta)

class TotalProductosModel(QtGui.QSortFilterProxyModel):
    """
    Un QSortFilterProxyModel especializado que carga los datos dados en un modelo bidimensional QStandardItemModel.
    """
    def __init__(self, parent=None):
        super(TotalProductosModel, self).__init__(parent)
        self.setDynamicSortFilter(True)

    def load_data(self, datos, header):
        """
        Carga la información dada en un QStandardItemModel
        """
        row = len(datos)

        self.model = QtGui.QStandardItemModel(row, len(header))

        for i, data in enumerate(datos):
            row = [controller_admin_producto.zerosAtLeft(data.id_producto,2), data.codigo, data.nombre, controller_admin_producto.monetaryFormat(
                str(data.precio_bruto).split(".")[0])]
            for j, field in enumerate(row):
                item = QtGui.QStandardItem(field)
                self.model.setItem(i, j, item)

        for col, h in enumerate(header):
            self.model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])

        self.setSourceModel(self.model)

    #def set_headers(header)