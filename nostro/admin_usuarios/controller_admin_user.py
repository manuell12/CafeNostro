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
    """
    Retorna todos los usuarios de la base de datos
    """
    return Usuario.all()

def getUsuarioId(id):
    """
    Retorna los datos de un usuario especificando su id
    """
    user = Usuario()
    user.id_usuario = id
    return Usuario.getUsuarioId(user)

def getUsuarioRut(rut):
    """
    Retorna los datos de un usuario especificando su rut
    """
    user = Usuario()
    user.rut = rut
    return Usuario.getUsuarioRut(user)

def UpdateDataUsuario(id, nombre, apellido, rut, clave, tipo, status):
    """
    Actualiza todos los campos de un usuario especificando 
    su id, nombre, apellido, rut, clave, tipo y status.
    """
    if clave == None:
        user = Usuario(id, nombre, apellido, rut, clave, tipo, status)
        Usuario.UpdateDataUsuarioWithoutNewPass(user)
    else:
        crypt = c.CryptoRAF()
        clave_encriptada = crypt.encrypt(
        clave, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
        user = Usuario(id, 
            nombre, apellido, rut, clave_encriptada, tipo, status)
        Usuario.UpdateDataUsuario(user)

def UpdateStatusUsuario(id, status):
    """
    Actualiza el estado de un usuario especificando su id.
    """
    user = Usuario()
    user.id_usuario = id
    user.status = status
    Usuario.UpdateStatusUsuario(user)

def AddDataUsuario(nombre, apellido, rut, clave, tipo, status):
    """
    Agrega un usuario nuevo a la base de datos. Recibe como entrada 
    todos los campos necesarios para su creacion.
    """
    crypt = c.CryptoRAF()
    clave_encriptada = crypt.encrypt(
        clave, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
    user = Usuario(
        None, nombre, apellido, rut, clave_encriptada, tipo, int(status))
    Usuario.AddDataUsuario(user)

def getUsuarioStatus(status):
    """
    Obtiene los usuarios de la base de datos que tengan el mismo estado 
    determinado por el parámetro entregado
    """
    user = Usuario()
    user.status = status
    return Usuario.getUsuarioStatus(user)

def deleteUser(id):
    """
    Elimina un usuario de la base de datos
    """
    user = Usuario()
    user.id_usuario = id
    Usuario.deleteUsers(user)

def validarNombreF(label, nombre):
    """
    Cambia el estado del label segun la respuesta de validacion 
    del nombre ingresado
    """
    if(validaTexto(nombre,"texto")):
        label.setText(
            u"<font color='green'><b>Nombre correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Debe tener sólo letras.</b></font>")

def validarApellidoF(label, apellido):
    """
    Cambia el estado del label segun la respuesta de validacion 
    del apellido ingresado
    """
    if(validaTexto(apellido,"texto")):
        label.setText(
            u"<font color='green'><b>Apellido correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Debe tener sólo letras.</b></font>")

def validarRutF(label, rut):
    """
    Cambia el estado del label segun la respuesta de validacion 
    del apellido ingresado
    """
    if(validaRut(rut)):
        label.setText(
            u"<font color='green'><b>Rut correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Rut incorrecto, ej: 12345678-9</b></font>")

def validarDatos(nombre,apellido,rut,verif,clave_ac,tipo):
    """
    Retorna True si todos los campos estan ingresados correctamente y
    retorna False en caso contrario.
    """
    if(clave_ac == None and verif !=None): # Nuevo usuario
        if(nombre != u"<font color='green'><b>Nombre correcto.</b></font>"):
            return False
        if(apellido != u"<font color='green'><b>Apellido correcto.</b></font>"):
            return False
        if(rut != u"<font color='green'><b>Rut correcto.</b></font>"):
            return False
        if(verif != u"<font color='green'><b>Contraseñas coinciden.</b></font>"):
            return False
        if(tipo != u"<font color='green'><b>Seleccion correcta.</b></font>"):
            return False
        return True
    if(clave_ac == None and verif == None): # Editar usuario, sin cambio de clave
        if(nombre != u"<font color='green'><b>Nombre correcto.</b></font>"):
            return False
        if(apellido != u"<font color='green'><b>Apellido correcto.</b></font>"):
            return False
        if(rut != u"<font color='green'><b>Rut correcto.</b></font>"):
            return False
        if(tipo != u"<font color='green'><b>Seleccion correcta.</b></font>"):
            return False
        return True
    else: # Cambio de clave
        if(nombre != u"<font color='green'><b>Nombre correcto.</b></font>"):
            return False
        if(apellido != u"<font color='green'><b>Apellido correcto.</b></font>"):
            return False
        if(rut != u"<font color='green'><b>Rut correcto.</b></font>"):
            return False
        if(clave_ac != u"<font color='green'><b>Contraseña ingresada correcta.</b></font>"):
            return False
        if(verif != u"<font color='green'><b>Contraseñas coinciden.</b></font>"):
            return False
        if(tipo != u"<font color='green'><b>Seleccion correcta.</b></font>"):
            return False
        return True

def validaTexto(text,validacion):
    """
    Función que evalua y valida el string 'text' dependiendo el valor del 
    segundo parámetro:
        texto: retorna 'True' si el string text esta compuesto sólo por
               letras (mayusculas y minusculas y tildes) y espacios.
        digito: retorna 'True' si el string 'text' posee sólo numeros y ".".
        numeros: retorna 'True' si el string 'text' esta compuesto sólo por
                 números.

    Retorna 'False' en caso contrario o si el string 'text' esta vacío
    """

    valido=True

    if (validacion=="digito"):
        cadena = "0123456789kK"

    if (validacion=="numeros"):
        cadena = "0123456789"

    if (validacion=="texto"):
        cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"

    i=0
    #print(text)
    string_num=str(text.encode('utf-8'))

    if(len(string_num)==0):
        valido=False

    while(valido and (i<len(string_num))):
        if (not string_num[i] in cadena):
            valido=False
        i=i+1
    return valido

def validaRut(rut):
    """Función que valida si el rut es valido, retorna un 
    booleano (true si es valido, false sino)
    """
    valido = False
    suma = 0
    multi= 2
    datos_rut = rut.split('-') #separamos la cadena por '-'
    if(len(datos_rut) == 2 and datos_rut[1] != ""):
        valido = validaTexto(datos_rut[0],"numeros")
        if(len(datos_rut[1])==1 and valido):
            valido = validaTexto(datos_rut[1],"digito")
        else:
            valido = False
        rut_1 = datos_rut[0]
        dig = datos_rut[1]
        if(len(rut_1)>= 6 and valido):
            for r in rut_1[::-1]:
                suma += int(r)* multi
                multi+= 1
                if multi == 8:
                    multi = 2
            resto = suma%11
            resta = 11 - resto
            if resta == 11:
                dig_r = 0
            elif resta == 10:
                dig_r = 'k'
            else:
                dig_r = resta
            if(str(dig_r) != str(dig)):
                valido = False
            else:
                valido = True
        else:
            valido = False
    else:
        valido = False
    return valido
