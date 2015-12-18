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


def obtenerObjetoPagos(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(Pago(row[0], row[1], row[2],
                          row[3], row[4], row[5]))
    return lista

def obtenerObjetoEmpresa(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(Empresa(row[0], row[1], row[2],
                          row[3], row[4], row[5], row[6], row[7], row[8]))
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

    def finalizarPedido(cls):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE pedido SET en_curso = 0 WHERE idPedido = {0}".format(
            cls.id_pedido)
        conn.execute(query)
        conex.commit()
        conn.close()

    def deletePedido(cls):
        try:
            conex = connect()
            conn = conex.cursor()
            query = "DELETE FROM pedido WHERE idPedido = {0}".format(
                cls.id_pedido)
            conn.execute(query)
            conex.commit()
            conn.close()
        except MySQLdb.Error as e:
            conn.close()
            return "Error"

    def getPedido(cls):
        query = "SELECT * FROM pedido WHERE idPedido = {0}".format(
            cls.id_pedido)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            conn.close()
            return obtenerObjetoPedidos(data)

        except MySQLdb.Error as e:
            conn.close()
            print "Error al obtener los Productos:", e.args[0]
            return None

    def getPedidoActivoPorMesa(cls):
        query = "SELECT * FROM pedido WHERE mesa = {0} and en_curso = 1".format(
            cls.mesa)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            conn.close()
            return obtenerObjetoPedidos(data)

        except MySQLdb.Error as e:
            conn.close()
            print "Error al obtener los Productos:", e.args[0]
            return None

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
        Método utlizado para obtener los productos de un pedido especifico.
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

    def deleteProductosPedido(cls):
        """
        Método que elimina todos los productos de un pedido.
        """
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM venta_has_producto WHERE idPedido = {0}".format(
            cls.id_pedido)
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

    def getVentaPedidoId(cls):
        """
        Método utlizado para obtener la venta de un pedido.
        """
        query = "SELECT * FROM venta WHERE idPedido = {}".format(
            cls.id_pedido)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            return obtenerObjetoVentas(data)

        except MySQLdb.Error as e:
            print "Error al obtener los Productos:", e.args[0]
            return None

        conn.close()

    def edit_data_venta(cls):
        print("{}\t{}\t{}\t{}".format(cls.id_venta,
                                      cls.fecha, cls.total_pago, cls.id_usuario))
        try:
            conex = connect()
            conn = conex.cursor()
            query = "UPDATE venta SET total_pago = {} WHERE idVenta = {}".format(
                cls.total_pago,
                cls.id_venta)
            print(query)
            conn.execute(query)
            conex.commit()

        except MySQLdb.Error as e:
            print "Error al editar la venta:", e.args[0]

        conn.close()

    def delete_venta(cls):
        """Método que se encarga de eliminar un venta identificandola con su PK"""
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM venta WHERE idVenta = {}".format(cls.id_venta)
        conn.execute(query)
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
    def get_id_venta(cls, id_pedido):
        """ Obtiene el id venta que esta asociado a un pedido """
        conex = connect()
        conn = conex.cursor()
        query = "SELECT `idVenta` FROM `venta` WHERE `idPedido` = {}".format(
            id_pedido)
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


class Pago(object):
    """
    Clase que representa a la tabla Pedido.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "pago"
    id_pago = None  # Primary Key
    pago_total = 0
    efectivo = 0
    tarjeta = 0
    propina = 0
    id_venta = 0

    def __init__(
            self,
            id_pago=None,
            pago_total=0,
            efectivo=0,
            tarjeta=0,
            propina=0,
            id_venta=0):

        self.id_pago = id_pago  # Primary Key
        self.pago_total = pago_total
        self.efectivo = efectivo
        self.tarjeta = tarjeta
        self.propina = propina
        self.id_venta = id_venta

    def addDataPago(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO pago(idPago, pago_total, efectivo, tarjeta, propina, idVenta) VALUES(%s,%s, %s, %s, %s, %s)"
        conn.execute(query,
                     (cls.id_pago,
                      cls.pago_total,
                      cls.efectivo,
                      cls.tarjeta,
                      cls.propina,
                      cls.id_venta))
        conex.commit()
        conn.close()

    def delete_pago(cls):
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM pago WHERE idVenta = {}".format(cls.id_venta)
        conn.execute(query)
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
            conn.close()
            return obtenerObjetoPagos(data)

        except MySQLdb.Error as e:
            print "Error al obtener los pagos:", e.args[0]
            conn.close()
            return None

class Empresa(object):
    """
    Clase que representa a la empresa del café
    """
    id_empresa = 0
    rut = ""
    nombre = ""
    direccion = ""
    ciudad = ""
    giro = ""
    fono = ""
    email = ""
    num_mesas = 0
    def __init__(self,
                id_empresa=0,
                rut="",
                nombre="",
                direccion="",
                ciudad="",
                giro="",
                fono="",
                email="",
                num_mesas=0):
        self.id_empresa = id_empresa
        self.rut = rut
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.giro = giro
        self.fono = fono
        self.email = email
        self.num_mesas = num_mesas

    def getEmpresa(cls):
        """
        Método utlizado para obtener la empresa de un id especifico.
        """
        query = "SELECT * FROM empresa WHERE idEmpresa = {}".format(
            cls.id_empresa)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            return obtenerObjetoEmpresa(data)

        except MySQLdb.Error as e:
            print "Error al obtener los datos:", e.args[0]
            return None

        conn.close()

    def editNumMesasEmpresa(cls):
        try:
            conex = connect()
            conn = conex.cursor()
            query = "UPDATE empresa SET num_mesas = {0} WHERE idEmpresa = 1".format(
                cls.num_mesas)
            conn.execute(query)
            conex.commit()

        except MySQLdb.Error as e:
            print "Error al editar la venta:", e.args[0]

        conn.close()

