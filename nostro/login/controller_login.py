#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_login import Usuarios
import sys
sys.path.append('../admin_usuarios')
import cryptoraf as c

def obtenerUsuario(rut=None,password=None):
    """Retorna una usuario (objeto) luego de buscarlo a travez de su nombre y clave"""
    crypt = c.CryptoRAF()
    clave_encriptada = crypt.encrypt(password,"fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
    usuario = Usuarios(None, None, None, rut, clave_encriptada, None, None)
    valido = usuario.userValido()
    return valido
