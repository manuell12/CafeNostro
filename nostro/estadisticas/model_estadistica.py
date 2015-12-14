#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos, tiene la habilidad de crear, modificar y eliminar registros de ella.
"""

import MySQLdb


def connect():
    conex = MySQLdb.connect("localhost", "root", "", "cafe_nostro")
    return conex

def obtenerObjetoVentaProductos(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(VentaProducto(row[0], row[1], row[2], row[3], row[4]))
    return lista

def obtenerObjetoVentas(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(Venta(row[0], row[1], row[2],
                           row[3], row[4], row[5], row[6]))
    return lista

class VentaProducto(object):
    """
    Clase que representa a la tabla venta_has_producto.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "venta_has_producto"
    id_pedido = None  # FK
    id_producto = None  # FK
    cantidad = 0
    precio_venta = 0
    porcentaje_descuento = 0

    def __init__(
            self,
            id_pedido=None,
            id_producto=None,
            cantidad=0,
            precio_venta=0,
            porcentaje_descuento=0):

        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_venta = precio_venta
        self.porcentaje_descuento = porcentaje_descuento

    def getProductosPedido(cls):
        """
        Método utlizado para obtener todos los productos de un pedido.
        """
        query = "SELECT * FROM venta_has_producto WHERE idPedido = {}".format(
            cls.id_pedido)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            return obtenerObjetoVentaProductos(data)

        except MySQLdb.Error as e:
            print "Error al obtener los Productos:", e.args[0]
            return None

        conn.close()

    @classmethod
    def getProductosPorFecha(cls,fecha):
        """
        Método utlizado para obtener la cantidad vendida de un producto en un dia especificado.
        """
        query = "SELECT VP.idPedido,VP.idProducto,SUM(VP.cantidad) as cantidad,VP.precio_venta,VP.porcentaje_descuento FROM venta_has_producto VP, venta V WHERE V.idPedido = VP.idPedido and V.fecha = '{0}' GROUP by VP.idProducto".format(fecha)
        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            return obtenerObjetoVentaProductos(data)

        except MySQLdb.Error as e:
            print "Error al obtener los Productos:", e.args[0]
            return None

        conn.close()

class Venta(object):
    """
    Clase que representa a la tabla Pedido.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "venta"
    id_venta = None  # Primary Key
    fecha = ""
    num_documento = 0
    tipo = ""
    total_pago = 0
    id_usuario = 0
    id_pedido = 0

    def __init__(
            self,
            id_venta=None,
            fecha="",
            num_documento=0,
            tipo="",
            total_pago=0,
            id_usuario=0,
            id_pedido=0):

        self.id_venta = id_venta
        self.fecha = fecha
        self.num_documento = num_documento
        self.tipo = tipo
        self.total_pago = total_pago
        self.id_usuario = id_usuario
        self.id_pedido = id_pedido

    @classmethod
    def getVentasPorFecha(cls, fecha_inicio, fecha_fin):
        """
        Método utlizado para obtener la colección de filas en la tabla venta comprendidas entre las fechas dadas 
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM venta WHERE fecha >= %s and fecha <= %s"

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query,(fecha_inicio,fecha_fin))
            data = conn.fetchall()
            conn.close()
            return obtenerObjetoVentas(data)

        except MySQLdb.Error as e:
            print "Error al obtener las ventas:", e.args[0]
            conn.close()
            return None


    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla venta
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(
            cls.__tablename__)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            conn.close()
            return obtenerObjetoVentas(data)

        except MySQLdb.Error as e:
            print "Error al obtener las ventas:", e.args[0]
            conn.close()
            return None

        