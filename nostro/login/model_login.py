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

        # Si el nombre viene con un valor hay que obtener la fila de la DB
        if rut is not None and clave is not None:
            self.load(rut=rut,clave=clave)

    def load(self, rut=None, clave=None):
        """
        Carga un usuario de estado "1" desde la base de datos por su nombre y clave.
        """

        conn = connect()
        #query = "SELECT * FROM {}".format(self.__tablename__)
        if rut is not None and clave is not None:
            query = ("SELECT * FROM usuario WHERE rut = '%s'" % rut + " AND clave = '%s'" % clave + " AND status = '%s'" % 1)
            #condition = "rut"
        """
        if clave is not None:
            query += " WHERE clave = ?"
            condition = clave
        """
        print query
        conn.execute(query)
        #print result
        row = conn.fetchone()
        print row
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
        else:
            print "El usuario no se encuentra en la base de datos"

    def userValido(self):
        return self.valido    

