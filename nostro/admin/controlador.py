# -*- coding: utf-8 -*-
import sys

def conectar():
	'''Por definir'''

def updateNombreUsuario(nombre,id):
	conex = conectar()
	c = conex[0]
	conn = conex[1]
	query = "UPDATE usuario SET nombre = ? WHERE idUsuario = ?"
	c.execute(query, [nombre,idUsuario])
	conn.commit()
def updateApellidoUsuario(apellido,id):
	conex = conectar()
	c = conex[0]
	conn = conex[1]
	query = "UPDATE usuario SET apellido = ? WHERE idUsuario = ?"
	c.execute(query, [apellido,idUsuario])
	conn.commit()
def updateRutUsuario(rut,id):
	conex = conectar()
	c = conex[0]
	conn = conex[1]
	query = "UPDATE usuario SET rut = ? WHERE idUsuario = ?"
	c.execute(query, [rut,idUsuario])
	conn.commit()
def UpdateDataUsuario(id, nombre, apellido, rut, clave):
	c = conectar()
	query = "UPDATE usuario SET nombre = ?, apellido = ?, rut = ?, clave = ? WHERE idUsuario = ?"
	c[0].execute(query, [nombre,apellido,rut,clave,id])
	c[1].commit()
def AddDataUsuario(nombre, apellido, rut, clave):
	c = conectar()
	c[0].execute('''INSERT INTO usuario(nombre, apellido, rut, clave)
					VALUES(?, ?, ?, ?)''',(nombre, apellido, rut, clave))
	c[1].commit()
def getUsuarioId(id):
	c = conectar()[0]
	query = "SELECT * FROM usuario WHERE idUsuario = ?"
	resultado = c.execute(query, [id])
	usuario = resultado.fetchall()
	return usuario

