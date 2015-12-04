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


def obtenerObjetoPedidos(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(Pedido(row[0], row[1], row[2]))
    return lista


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


class Pedido(object):
    """
    Clase que representa a la tabla Pedido.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "pedido"
    id_pedido = None  # Primary Key
    mesa = ""
    en_curso = 0

    def __init__(
            self,
            id_pedido=None,
            mesa="",
            en_curso=0):

        self.id_pedido = id_pedido
        self.mesa = mesa
        self.en_curso = en_curso

    def addDataPedido(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO pedido(idPedido, mesa, en_curso) VALUES(%s, %s, %s)"
        conn.execute(query,
                     (cls.id_pedido,
                      cls.mesa,
                      cls.en_curso))
        conex.commit()
        conn.close()

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla pedido
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
            return obtenerObjetoPedidos(data)

        except MySQLdb.Error as e:
            print "Error al obtener los usuarios:", e.args[0]
            return None

        conn.close()


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

    def addDataVentaProducto(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO venta_has_producto(idPedido, idProducto, cantidad, precio_venta, porcentaje_descuento) VALUES(%s, %s, %s, %s, %s)"
        conn.execute(query,
                     (cls.id_pedido,
                      cls.id_producto,
                      cls.cantidad,
                      cls.precio_venta,
                      cls.porcentaje_descuento))
        conex.commit()
        conn.close()
        return 0

    def getProductosPedido(cls):
        """
        Método utlizado para obtener los productos de un pedido espedifico.
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

    def deleteProducto(cls):
        """
        Método que borra un producto de un pedido especifico en la tabla venta_has_producto.
        """
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM venta_has_producto WHERE idProducto = {0} and idPedido = {1}".format(
            cls.id_producto, cls.id_pedido)
        conn.execute(query)
        conex.commit()
        conn.close()

    def hayProductoPedido(cls):
        """
        Método que retorna un producto de un pedido en la tabla venta_has_producto.
        """
        query = "SELECT * FROM venta_has_producto WHERE idPedido = {0} and idProducto = {1}".format(
            cls.id_pedido, cls.id_producto)

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

    def hayProducto(cls):
        """
        Método que retorna un producto en la tabla venta_has_producto.
        """
        query = "SELECT * FROM venta_has_producto WHERE idProducto = {0}".format(
            cls.id_producto)

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

    def cambiarCantidadProducto(cls, cambiar):
        '''Interacciona con la base de datos a travez de una query que actualiza el estado de un Producto, especificando su id'''
        conex = connect()
        conn = conex.cursor()
        if(cambiar == "aumentar"):
            query = "UPDATE venta_has_producto SET cantidad = cantidad + 1 WHERE idProducto = %s and idPedido = %s"
            conn.execute(query,
                         (cls.id_producto,
                          cls.id_pedido))
            conex.commit()
            conn.close()
        if(cambiar == "disminuir"):
            query = "UPDATE venta_has_producto SET cantidad = cantidad - 1 WHERE idProducto = %s and idPedido = %s"
            conn.execute(query,
                         (cls.id_producto,
                          cls.id_pedido))
            conex.commit()
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

    def addDataVenta(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO venta(fecha, num_documento, tipo, total_pago, idUsuario, idPedido) VALUES(%s, %s, %s, %s, %s, %s)"
        conn.execute(query,
                     (cls.fecha,
                      cls.num_documento,
                      cls.tipo,
                      cls.total_pago,
                      cls.id_usuario,
                      cls.id_pedido))
        conex.commit()
        conn.close()

    @classmethod
    def getIdPedido(cls, id_venta):
        conex = connect()
        conn = conex.cursor()
        query = "SELECT `idPedido` FROM `venta` WHERE `idVenta` = {}".format(
            id_venta)
        conn.execute(query)
        data = conn.fetchall()[0][0]
        # print(data)
        conex.commit()
        conn.close()
        return data

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla pedido
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
            return obtenerObjetoVentas(data)

        except MySQLdb.Error as e:
            print "Error al obtener las ventas:", e.args[0]
            return None

        conn.close()
