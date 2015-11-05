#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_admin_user import Usuario


def usuarios():
	"""Retorna todos los usuarios de la base de datos"""
	return Usuario.all()
def getUsuarioId(id):
	"""Retorna los datos de un usuario especificando su id"""
	user = Usuario()
	user.id_usuario = id
	return Usuario.getUsuarioId(user)
def UpdateDataUsuario(id, nombre, apellido, rut, clave, tipo, status):
	"""Actualiza todos los campos de un usuario especificando su id, nombre, apellido, rut, clave, tipo y status"""
	user = Usuario(id, nombre, apellido, rut, clave, tipo, status)
	return Usuario.UpdateDataUsuario(user)
def AddDataUsuario(nombre, apellido, rut, clave, tipo, status):
	"""Agrega un usuario nuevo a la base de datos. Recibe como entrada todos los campos necesarios para su creacion"""
	user = Usuario(None, nombre, apellido, rut, clave, tipo, status)
	return Usuario.AddDataUsuario(user)