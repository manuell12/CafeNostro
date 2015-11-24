#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from model_admin_producto import Producto, Categoria


def Productos():
    """Retorna todos los Productos de la base de datos"""
    return Producto.all()


def getCategorias():
    """Retorna todas las categorias de la base de datos"""
    return Categoria.getCategorias()


def getNombresCategorias():
    """Retorna todos los nombres de todas las categorias ingresadas en la tabla 'categoria' de la base de datos"""
    return Categoria.getNombresCategorias()


def getProductoId(id):
    """Retorna los datos de un Producto especificando su id"""
    producto = Producto()
    producto.id_producto = id
    return Producto.getProductoId(producto)


def UpdateDataProducto(id, nombre, descripcion, precio_neto, precio_bruto, status, id_categoria):
    producto = Producto(id, nombre, descripcion, precio_neto,
                        precio_bruto, status, id_categoria)
    Producto.UpdateDataProducto(producto)


def UpdateStatusProducto(id, status):
    """Actualiza el estado de un Producto especificando su id"""
    producto = Producto()
    producto.id_producto = id
    producto.status = status
    Producto.UpdateStatusProducto(producto)


def AddDataProducto(nombre, descripcion, precio_neto, precio_bruto, status, id_categoria):
    """Agrega un Producto nuevo a la base de datos. Recibe como entrada todos los campos necesarios para su creacion"""
    producto = Producto(None, nombre, descripcion, precio_neto,
                        precio_bruto, status, int(id_categoria))
    Producto.AddDataProducto(producto)


def getProductoStatus(status):
    """Obtiene los Productos de la base de datos que tengan el mismo estado determinado por el parámetro entregado"""
    producto = Producto()
    producto.status = status
    return Producto.getProductoStatus(producto)


def deleteproducto(id):
    """Elimina un Producto de la base de datos"""
    producto = Producto()
    producto.id_producto = id
    Producto.deleteproductos(producto)


def validarNombreF(label, nombre):
    """Cambia el estado del label segun la respuesta de validacion del nombre ingresado"""
    if(validaTexto(nombre, "no_simbolos")):
        label.setText(
            u"<font color='green'><b>Nombre correcto.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Sólo puede contener letras y numeros.</b></font>")


def validarPrecioNetoF(label, precio_neto):
    """Cambia el estado del label segun la respuesta de validacion del apellido ingresado"""
    valida = validaTexto(precio_neto, "digito")
    if(valida):
        if(float(precio_neto) >= 0 and float(precio_neto) < 100000):
            label.setText(
                u"<font color='green'><b>Precio bruto correcto.</b></font>")
        else:
            label.setText(
                u"<font color='red'><b>Debe ser un valor entre 0 y 99999.</b></font>")
    else:
        label.setText(
            u"<font color='red'><b>Debe tener sólo números.</b></font>")


def validarDatos(nombre, precio_neto, categoria):
    if(nombre != u"<font color='green'><b>Nombre correcto.</b></font>"):
        return False
    if(precio_neto != u"<font color='green'><b>Precio bruto correcto.</b></font>"):
        return False
    if(categoria != u"<font color='green'><b>Selección correcta.</b></font>"):
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
        cadena = "0123456789"

    if (validacion == "no_simbolos"):
        cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789"

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

def monetaryFormat(price):
    price = str(price)
    price = price[::-1]
    price_formatted = ""
    for i,a in enumerate(price):
        if(i > 0 and i % 3 == 0):
            price_formatted = price_formatted + "."
        price_formatted = price_formatted + price[i]
    price_formatted = price_formatted[::-1]
    return price_formatted