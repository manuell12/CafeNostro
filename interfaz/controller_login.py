#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_login import Usuarios

def obtenerUsuario(rut=None,password=None):
    """Retorna una usuario (objeto) luego de buscarlo a travez de su nombre y clave"""
    usuario = Usuarios(None, None, None, rut, password, None, None)
    valido = usuario.userValido()
    return valido
