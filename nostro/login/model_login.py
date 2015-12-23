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

class Usuarios(object):
    """
    Clase que representa a la tabla Usuarios.
    Una instancia de esta clase representa una fila.
    La instancia (objeto) puede estar en la BD o no.
    """

    __tablename__ = "usuario"
    idUsuario = None  # Primary Key
    nombre = ""
    apellido = ""
    rut = ""
    clave = ""
    tipo = ""
    status = ""

    #Constructor de la clase
    def __init__(self,
                 idUsuario = None,  
                 nombre = "",
                 apellido = "",
                 rut = "",
                 clave = "",
                 tipo = "",
                 status = ""):

        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.clave = clave
        self.tipo = tipo
        self.status = status

        self.valido = False

        if rut is not None and clave is not None:
            self.load(rut=rut,clave=clave)

    def load(self, rut=None, clave=None):
        """
        Carga un usuario de estado "1" desde la base de datos por su nombre y clave.
        """
        conn = connect()
        if rut is not None and clave is not None:
            query = ("SELECT * FROM usuario WHERE rut = '%s'" % rut + " AND clave = '%s'" % clave + " AND status = '%s'" % 1)
        conn.execute(query)
        row = conn.fetchone()
        conn.close()
        if row is not None:
            self.idUsuario = row[0]
            self.nombre = row[1]
            self.apellido = row[2]
            self.rut = row[3]
            self.clave = row[4]
            self.tipo = row[5]
            self.status = row[6]
            self.valido = True

    def userValido(self):
        """
        Método que retorna un booleano correspondiente a:
            True: usuario valido.
            False: usuario invalido.
        """
        return self.valido    

    def getTipoUsuarioPorRut(cls):
        """
        Método que obtiene el tipo de un usuario especifico.
        """
        conn = connect()
        query = ("SELECT tipo FROM usuario WHERE rut = '%s'" % cls.rut)
        conn.execute(query)
        Producto = conn.fetchall()
        return Producto
        conn.close()
