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

def obtenerObjetoUsuarios(data):
    """
    Recibe como parametro la tupla recibida desde la BD y retorna una lista de objetos con todos los datos de los productos.
    """
    lista = list()
    for i,row in enumerate(data):
        lista.append(Usuario(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    return lista

class Usuario(object):
    """
    Clase que representa a la tabla Usuario.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """
    __tablename__ = "usuario"
    id_usuario = None  # Primary Key
    nombre = ""
    apellido = ""
    rut = ""
    clave = ""
    tipo = ""
    status = ""

    def __init__(
            self,
            id_usuario=None,
            nombre="",
            apellido="",
            rut="",
            clave="",
            tipo="",
            status=""):

        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.clave = clave
        self.tipo = tipo
        self.status = status

    def updateNombreUsuario(cls, nombre, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET nombre = ? WHERE idUsuario = ?"
        conn.execute(query, [nombre, idUsuario])
        conex.commit()
        conn.close()

    def updateApellidoUsuario(cls, apellido, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET apellido = ? WHERE idUsuario = ?"
        conn.execute(query, [apellido, idUsuario])
        conex.commit()
        conn.close()

    def updateRutUsuario(cls, rut, id):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET rut = ? WHERE idUsuario = ?"
        conn.execute(query, [rut, idUsuario])
        conex.commit()
        conn.close()

    def UpdateDataUsuario(cls):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET nombre = %s, apellido = %s, rut = %s, clave =  %s , tipo = %s, status = %s WHERE idUsuario = %s"
        conn.execute(query,
                     (cls.nombre,
                      cls.apellido,
                      cls.rut,
                      cls.clave,
                      cls.tipo,
                      cls.status,
                      cls.id_usuario))
        conex.commit()
        conn.close()

    def UpdateDataUsuarioWithoutNewPass(cls):
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET nombre = %s, apellido = %s, rut = %s, tipo = %s, status = %s WHERE idUsuario = %s"
        conn.execute(query,
                     (cls.nombre,
                      cls.apellido,
                      cls.rut,
                      cls.tipo,
                      cls.status,
                      cls.id_usuario))
        conex.commit()
        conn.close()

    def UpdateStatusUsuario(cls):
        '''Interacciona con la base de datos a travez de una query que actualiza el estado de un usuario, especificando su id'''
        conex = connect()
        conn = conex.cursor()
        query = "UPDATE usuario SET status = %s WHERE idUsuario = %s"
        conn.execute(query,
                     (int(cls.status),
                      cls.id_usuario))
        conex.commit()
        conn.close()

    def AddDataUsuario(cls):
        conex = connect()
        conn = conex.cursor()
        query = "INSERT INTO usuario(nombre, apellido, rut, clave, tipo, status) VALUES(%s, %s, %s, %s, %s, %s)"
        conn.execute(query,
                     (cls.nombre,
                      cls.apellido,
                      cls.rut,
                      cls.clave,
                      cls.tipo,
                      cls.status))
        conex.commit()
        conn.close()

    def getUsuarioId(cls):
        conex = connect()
        conn = conex.cursor()
        query = "SELECT * FROM usuario WHERE idUsuario = {}".format(
            cls.id_usuario)
        conn.execute(query)
        usuario = conn.fetchall()
        conn.close()
        return obtenerObjetoUsuarios(usuario)

    def getUsuarioRut(cls):
        conex = connect()
        conn = conex.cursor()
        query = "SELECT * FROM usuario WHERE rut = '{0}'".format(
            cls.rut)
        conn.execute(query)
        usuario = conn.fetchall()
        conn.close()
        return obtenerObjetoUsuarios(usuario)

    def deleteUsers(cls):
        conex = connect()
        conn = conex.cursor()
        query = "DELETE FROM usuario WHERE idUsuario = {}".format(
            cls.id_usuario)
        conn.execute(query)
        conex.commit()
        conn.close()

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla usuario.
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
            return obtenerObjetoUsuarios(data)

        except MySQLdb.Error as e:
            print "Error al obtener los usuarios:", e.args[0]
            return None

        conn.close()

    def getUsuarioStatus(cls):
        """
        Método utlizado para obtener los usuarios que compartan un valor de status.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM usuario WHERE status = {}".format(
            cls.status)

        try:
            conex = connect()
            conn = conex.cursor()
            conn.execute(query)
            data = conn.fetchall()
            return obtenerObjetoUsuarios(data)

        except MySQLdb.Error as e:
            print "Error al obtener los usuarios:", e.args[0]
            return None

        conn.close()
