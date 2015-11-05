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
	return Usuario.getUsuarioId(id)