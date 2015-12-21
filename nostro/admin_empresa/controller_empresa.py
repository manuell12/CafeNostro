#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_empresa import Empresa

def getEmpresa(id_empresa):
    empresa = Empresa()
    empresa.id_empresa = id_empresa
    return Empresa.getEmpresa(empresa)

def editNumMesasEmpresa(num_mesas):
    empresa = Empresa()
    empresa.num_mesas = num_mesas
    Empresa.editNumMesasEmpresa(empresa)

def updateDataEmpresa(nombre,rut,direccion,ciudad,giro,fono,email,num_mesas):
	empresa = Empresa(1,rut,nombre,direccion,ciudad,giro,fono,email,num_mesas)
	Empresa.updateDataEmpresa(empresa)    

def validarNombreF(label, nombre):
    """Cambia el estado del label segun la respuesta de validacion del nombre ingresado"""
    if(validaTexto(nombre, "no_simbolos")):
        label.setText(
            u"<font color='green'><b>Nombre correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Sólo puede contener letras y numeros.</b></font>")

def validarDireccionF(label, direccion):
    """Cambia el estado del label segun la respuesta de validacion de la direccion ingresada"""
    if(validaTexto(direccion, "direccion")):
        label.setText(
            u"<font color='green'><b>Direccion correcta.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Direccion incorrecta.</b></font>")

def validarCiudadF(label, ciudad):
    """Cambia el estado del label segun la respuesta de validacion de la direccion ingresada"""
    if(validaTexto(ciudad, "no_simbolos")):
        label.setText(
            u"<font color='green'><b>Ciudad correcta.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Sólo puede contener letras y números.</b></font>")

def validarGiroF(label, giro):
    """Cambia el estado del label segun la respuesta de validacion de la direccion ingresada"""
    if(validaTexto(giro, "no_simbolos")):
        label.setText(
            u"<font color='green'><b>Giro correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Sólo puede contener letras y números.</b></font>")

def validarDatos(nombre, direccion, ciudad, giro):
    if(nombre != u"<font color='green'><b>Nombre correcto.</b></font>"):
        return False
    if(direccion != u"<font color='green'><b>Direccion correcta.</b></font>"):
        return False
    if(ciudad != u"<font color='green'><b>Ciudad correcta.</b></font>"):
        return False
    if(giro != u"<font color='green'><b>Giro correcto.</b></font>"):
        return False
    return True

def validaTexto(text, validacion):
    """Función que evalua y valida el string 'text' dependiendo el valor del segundo parámetro:
    numeros: retorna 'True' si el string 'text' posee sólo numeros
    no_simbolos: retorna 'True' si el string 'text' posee sólo letras (mayusculas o minusculas o acentos) y/o números
    Retorna 'False' en caso contrario o si el string 'text' esta vacío"""

    valido = True

    if (validacion == "digito"):
        cadena = "0123456789."

    if (validacion == "numeros"):
        cadena = " 0123456789"

    if (validacion == "no_simbolos"):
        cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789"

    if (validacion == "direccion"):
        cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789#'"

    if (validacion == "codigo"):
        cadena = "0123456789abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if (validacion == "texto"):
        cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"

    i = 0
    try:
        string_num = str(text.encode('utf-8'))
    except:
        return False

    if(len(string_num) == 0):
        valido = False

    while(valido and (i < len(string_num))):
        if (not string_num[i] in cadena):
            valido = False
        i = i + 1
    return valido