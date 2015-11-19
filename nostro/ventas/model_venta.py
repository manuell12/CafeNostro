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
        query = "INSERT INTO pedido(mesa, en_curso) VALUES(%s, %s)"
        conn.execute(query,
                     (cls.mesa,
                      cls.en_curso))
        conex.commit()
        conn.close()
        return 0

class VentaProducto(object):
    """
    Clase que representa a la tabla venta_has_producto.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "venta_has_producto"
    id_pedido = None  # FK
    id_producto = None # FK
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
            # print data
            return data

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
            cls.id_pedido,cls.id_producto)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            # print data
            return data

        except MySQLdb.Error as e:
            print "Error al obtener los Productos:", e.args[0]
            return None

        conn.close()

    def cambiarCantidadProducto(cls,cambiar):
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

