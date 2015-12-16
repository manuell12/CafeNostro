#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from estadistica import Ui_Estadistica
import controller_estadistica as controller
import admin_productos.controller_admin_producto as controller_admin_producto
import datetime
import os

class Estadistica(QtGui.QWidget):
    """
    Clase que genera un widget donde se muestran graficos y tablas con estadisticas sobre el local.
    """
    __header_table__ = ((u"Código", 50),
                        (u"Nombre", 200),
                        (u"Cantidad", 60),
                        (u"Precio/unidad", 100),
                        (u"Total", 60))
    def __init__(self):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Estadistica()
        self.ui.setupUi(self)
        self.setFocus()
        self.connect_actions()
        #self.actualizar_productos()

    def crearymostrar_html(self):
        """
        Método que crea el html 'charts.htm', donde se muestran los graficos.
        """
        fecha_inicio = self.ui.calendarWidget_inicio.selectedDate()
        fecha_fin = self.ui.calendarWidget_fin.selectedDate()

        file = open("estadisticas/charts.htm", "w+")
        file.write(controller.crear_html(self.lista_ProductoVenta,fecha_inicio,fecha_fin).encode('utf-8'))
        file.close()

        self.ui.webView.load(QtCore.QUrl("file:///"+os.getcwd()+"/estadisticas/charts.htm"))
        self.ui.webView.show()

    def connect_actions(self):
        """
        Método que accede a los slots de los widgets de la interfaz gráfica y los conecta con metodos de la clase Estadistica
        """
        self.ui.calendarWidget_inicio.selectionChanged.connect(self.actualizar_productos)
        self.ui.calendarWidget_fin.selectionChanged.connect(self.actualizar_productos)

    def actualizar_productos(self):
        """
        Método que realiza consultas a la base de datos sobre productos vendidos y los carga en la interfaz
        """
        self.lista_ProductoVenta = list()

        fecha_inicio = self.ui.calendarWidget_inicio.selectedDate().toString("yyyy-MM-dd")
        fecha_fin = self.ui.calendarWidget_fin.selectedDate().toString("yyyy-MM-dd")

        ventas = controller.getVentasPorFecha(fecha_inicio,fecha_fin)
        for venta in ventas:
            venta_productos = controller.getProductosPedido(venta.id_pedido)
            for ventaProducto in venta_productos:
                agregar = True
                for producto in self.lista_ProductoVenta:
                    if(ventaProducto.id_producto == producto.producto.id_producto):
                        producto.cantidad = producto.cantidad + ventaProducto.cantidad
                        agregar = False
                if(agregar):
                    objeto_producto_venta = controller.ProductoVenta(
                        controller_admin_producto.getProductoId(ventaProducto.id_producto)[0],
                        ventaProducto.cantidad,
                        ventaProducto.precio_venta,
                        venta.fecha)
                    self.lista_ProductoVenta.append(objeto_producto_venta)

        ingreso_total = 0
        productos_totales = 0
        for producto_venta in self.lista_ProductoVenta:
            ingreso_total = ingreso_total + (producto_venta.cantidad * producto_venta.precio)
            productos_totales = productos_totales + producto_venta.cantidad
        self.ui.label_ingreso_total.setText(str(ingreso_total))
        self.ui.label_total_productos.setText(str(productos_totales))

        self.load_model_total_productos(self.lista_ProductoVenta)

        self.crearymostrar_html()

    def load_model_total_productos(self, data=""):
        """
        Método que carga en la tabla 'tableView' la información pasada en el atributo 'data', debe ser una lista de objetos
        """
        model = controller.TotalProductosModel()
        self.ui.tableView.setModel(model)
        model.load_data(data, self.__header_table__)

        self.set_columns_total_productos()

    def set_columns_total_productos(self):
        """
        Método que ajusta el tamaño de las columnas de la tabla al especificado en '__header_table__'
        """
        self.ui.tableView.horizontalHeader().setResizeMode(
            1, self.ui.tableView.horizontalHeader().Stretch)

        for col, h in enumerate(self.__header_table__):
            self.ui.tableView.setColumnWidth(col, h[1])

        self.ui.tableView.sortByColumn(
            2, QtCore.Qt.DescendingOrder)
            
