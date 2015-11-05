#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos, tiene la habilidad de crear, modificar y eliminar registros de ella.
"""

import MySQLdb


def connect():
    db = MySQLdb.connect("localhost", "root", "", "cafe_nostro")
    conn = db.cursor()
    return conn


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

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla pelicula.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)

        try:
            conn = connect()
            conn.execute(query)
            data = conn.fetchall()
            # print data
            return data

        except MySQLdb.Error as e:
            print "Error al obtener los usuarios:", e.args[0]
            return None

        conn.close()

    def updateNombreUsuario(cls,nombre,id):
        conn = connect()
        query = "UPDATE usuario SET nombre = ? WHERE idUsuario = ?"
        conn.execute(query, [nombre,idUsuario])
        conn.commit()
    def updateApellidoUsuario(cls,apellido,id):
        conn = connect()
        query = "UPDATE usuario SET apellido = ? WHERE idUsuario = ?"
        conn.execute(query, [apellido,idUsuario])
        conn.commit()
    def updateRutUsuario(cls,rut,id):
        conn = connect()
        query = "UPDATE usuario SET rut = ? WHERE idUsuario = ?"
        conn.execute(query, [rut,idUsuario])
        conn.commit()
    def UpdateDataUsuario(cls):
        conn = connect()
        query = "UPDATE usuario SET nombre = ?, apellido = ?, rut = ?, clave = ?, tipo = ?, status = ? WHERE idUsuario = ?"
        conn.execute(query, [nombre,apellido,rut,clave,tipo,status,id])
        conn.commit()
    def AddDataUsuario(cls):
        conn = connect()
        query = "INSERT INTO usuario(nombre, apellido, rut, clave, tipo, status) VALUES(%s, %s, %s, %s, %s, %s)"
        conn.execute(query ,(str(cls.nombre), str(cls.apellido), str(cls.rut), str(cls.clave), str(cls.tipo), str(cls.status)))
        conn.close()
    def getUsuarioId(cls):
        conn = connect()
        query = "SELECT * FROM usuario WHERE idUsuario = %s"
        conn.execute(query, (str(cls.id)))
        usuario = conn.fetchall()
        return usuario
