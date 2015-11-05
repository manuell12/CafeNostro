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

    def updateNombreUsuario(nombre,id):
        conex = connect()
        c = conex[0]
        conn = conex[1]
        query = "UPDATE usuario SET nombre = ? WHERE idUsuario = ?"
        c.execute(query, [nombre,idUsuario])
        conn.commit()
    def updateApellidoUsuario(apellido,id):
        conex = connect()
        c = conex[0]
        conn = conex[1]
        query = "UPDATE usuario SET apellido = ? WHERE idUsuario = ?"
        c.execute(query, [apellido,idUsuario])
        conn.commit()
    def updateRutUsuario(rut,id):
        conex = connect()
        c = conex[0]
        conn = conex[1]
        query = "UPDATE usuario SET rut = ? WHERE idUsuario = ?"
        c.execute(query, [rut,idUsuario])
        conn.commit()
    def UpdateDataUsuario(id, nombre, apellido, rut, clave):
        c = connect()
        query = "UPDATE usuario SET nombre = ?, apellido = ?, rut = ?, clave = ? WHERE idUsuario = ?"
        c[0].execute(query, [nombre,apellido,rut,clave,id])
        c[1].commit()
    def AddDataUsuario(nombre, apellido, rut, clave):
        c = connect()
        c[0].execute('''INSERT INTO usuario(nombre, apellido, rut, clave)
                        VALUES(?, ?, ?, ?)''',(nombre, apellido, rut, clave))
        c[1].commit()
    def getUsuarioId(id):
        c = connect()[0]
        query = "SELECT * FROM usuario WHERE idUsuario = ?"
        resultado = c.execute(query, [id])
        usuario = resultado.fetchall()
        return usuario
