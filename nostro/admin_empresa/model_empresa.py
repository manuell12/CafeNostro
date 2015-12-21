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

def obtenerObjetoEmpresa(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i, row in enumerate(data):
        lista.append(Empresa(row[0], row[1], row[2],
                          row[3], row[4], row[5], row[6], row[7], row[8]))
    return lista

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
            print "Error al editar la empresa:", e.args[0]

        conn.close()

    def updateDataEmpresa(cls):
        try:
            conex = connect()
            conn = conex.cursor()
            query = """UPDATE empresa SET nombre = %s, rut = %s, direccion = %s, ciudad = %s, giro = %s, fono = %s, email = %s, num_mesas = {0} WHERE idEmpresa = 1""".format(
                cls.num_mesas)
            conn.execute(query,(cls.nombre,
                                cls.rut,
                                cls.direccion,
                                cls.ciudad,
                                cls.giro,
                                cls.fono,
                                cls.email))
            conex.commit()

        except MySQLdb.Error as e:
            print "Error al editar la empresa:", e.args[0]

        conn.close()