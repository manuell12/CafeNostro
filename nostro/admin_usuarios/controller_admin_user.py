#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_admin_user import Usuario
import cryptoraf as c

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
    if clave == None:
        user = Usuario(id, nombre, apellido, rut, clave, tipo, status)
        Usuario.UpdateDataUsuarioWithoutNewPass(user)
    else:
        crypt = c.CryptoRAF()
        clave_encriptada = crypt.encrypt(
        clave, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
        user = Usuario(id, nombre, apellido, rut, clave_encriptada, tipo, status)
        Usuario.UpdateDataUsuario(user)

def UpdateStatusUsuario(id, status):
    """Actualiza el estado de un usuario especificando su id"""
    user = Usuario(status)
    user.status = status
    Usuario.UpdateStatusUsuario(user)

def AddDataUsuario(nombre, apellido, rut, clave, tipo, status):
    """Agrega un usuario nuevo a la base de datos. Recibe como entrada todos los campos necesarios para su creacion"""
    crypt = c.CryptoRAF()
    clave_encriptada = crypt.encrypt(
        clave, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
    user = Usuario(None, nombre, apellido, rut, clave_encriptada, tipo, int(status))
    Usuario.AddDataUsuario(user)

def getUsuarioStatus(status):
    """Obtiene los usuarios de la base de datos que tengan el mismo estado determinado por el parámetro entregado"""
    user = Usuario()
    user.status = status
    return Usuario.getUsuarioStatus(user)

def deleteUser(id):
    """Elimina un usuario de la base de datos"""
    user = Usuario()
    user.id_usuario = id
    Usuario.deleteUsers(user)
