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


class Producto(object):
    """
    Clase que representa a la tabla Producto.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "producto"
    id_producto = None  # Primary Key
    nombre = ""
    descripcion = ""
    tipo = ""
    precio_neto = ""
    status = ""
    id_categoria = ""

    def __init__(
            self,
            id_producto=None,
            nombre="",
            descripcion="",
            tipo="",
            precio_neto="",
            status="",
            id_categoria=""):

        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.precio_neto = precio_neto
        self.status = status
        self.id_categoria = id_categoria

    def updateNombreProducto(cls, nombre, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE producto SET nombre = ? WHERE idProducto = ?"
        conn.execute(query, [nombre, idproducto])
        conex.commit()
        conn.close()

    def updateApellidoProducto(cls, descripcion, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE producto SET descripcion = ? WHERE idProducto = ?"
        conn.execute(query, [descripcion, idproducto])
        conex.commit()
        conn.close()

    def updateRutproducto(cls, tipo, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE producto SET tipo = ? WHERE idProducto = ?"
        conn.execute(query, [tipo, idproducto])
        conex.commit()
        conn.close()

    def UpdateDataProducto(cls):
        conex = connect()
        conn = conex.cursor()

        query = "UPDATE producto SET nombre = %s, descripcion = %s, precio_neto = %s, precio_bruto =  %s , status = %s, idCategoria = %s WHERE idProducto = %s"
        conn.execute(query,
                     (cls.nombre,
                      cls.descripcion,
                      cls.tipo,
                      cls.precio_neto,
                      cls.status,
                      cls.id_categoria,
                      cls.id_producto))
        conex.commit()
        conn.close()

    def UpdateStatusProducto(cls):
        '''Interacciona con la base de datos a travez de una query que actualiza el estado de un Producto, especificando su id'''
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE producto SET status = %s WHERE idProducto = %s"
        conn.execute(query,
                     (int(cls.status),
                      cls.id_producto))
        conex.commit()
        conn.close()

    def AddDataProducto(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO producto(nombre, descripcion, precio_neto, precio_bruto, status, idCategoria) VALUES(%s, %s, %s, %s, %s, %s)"
        conn.execute(query,
                     (cls.nombre,
                      cls.descripcion,
                      cls.tipo,
                      cls.precio_neto,
                      cls.status,
                      cls.id_categoria))
        conex.commit()
        conn.close()

    def getProductoId(cls):
        conex = connect()
        conn = conex.cursor()
        query = "SELECT * FROM producto WHERE idProducto = {}".format(
            cls.id_producto)
        conn.execute(query)
        Producto = conn.fetchall()
        return Producto
        conn.close()

    def getProductoCategoria(cls):
        conex = connect()
        conn = conex.cursor()
        query = "SELECT * FROM producto WHERE idCategoria = {} and status = 1".format(
            cls.id_categoria)
        conn.execute(query)
        Producto = conn.fetchall()
        return Producto
        conn.close()


    def deleteProducto(cls):
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM producto WHERE idProducto = {}".format(
            cls.id_producto)
        conn.execute(query)
        conex.commit()
        conn.close()

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla Producto.
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
            # print data
            return data

        except MySQLdb.Error as e:
            print "Error al obtener los Productos:", e.args[0]
            return None

        conn.close()

    def getProductoStatus(cls):
        """
        Método utlizado para obtener los Productos que compartan un valor de id_categoria.
        """
        query = "SELECT * FROM producto WHERE status = {}".format(
            cls.status)

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

class Categoria(object):
    """
    Clase que representa a la tabla categoria.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "categoria"
    id_categoria = None  # Primary Key
    nombre = ""
    descripcion = ""
    preparada_en = ""

    def __init__(
            self,
            id_producto=None,
            nombre="",
            descripcion="",
            categoria=""):

        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria

    @classmethod
    def getCategorias(cls):
        """
        Método utlizado para obtener todas las filas de la tabla categoria
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM categoria"

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            # print data
            return data

        except MySQLdb.Error as e:
            print "Error al obtener las categorias", e.args[0]
            return None

        conn.close()

    @classmethod
    def getNombresCategorias(cls):
        """
        Método utlizado para obtener todos los nomrbes de las categorias ingresadas
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT nombre FROM categoria"

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            # print data
            return data

        except MySQLdb.Error as e:
            print "Error al obtener las categorias", e.args[0]
            return None

        conn.close()
