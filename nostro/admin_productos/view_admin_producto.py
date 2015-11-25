#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from admin_producto import Ui_AdminProductos
import controller_admin_producto
import sys
import view_formulario_producto
import os


class AdminProductos(QtGui.QWidget):

    __header_table__ = [(u"ID"),
                        (U"Código"),
                        (u"Nombre"),
                        (u"Descripcion"),
                        (u"Precio neto"),
                        (u"Precio bruto"),
                        (u"Categoria"),
                        (u"Activo")]

    types = controller_admin_producto.getNombresCategorias()
    __type_productos__ = ["----"]
    for data in types:
        __type_productos__.append(data.nombre)

    def __init__(self):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_AdminProductos()
        self.ui.setupUi(self)
        self.setFocus()
        self.load_data_table()
        self.connect_actions()

    def connect_actions(self):
        """Conectar botones con su respectiva accion"""
        self.ui.editar_button.clicked.connect(self.action_btn_editar)
        self.ui.nuevo_button.clicked.connect(self.action_btn_nuevo)
        self.ui.eliminar_button.clicked.connect(self.action_btn_eliminar)
        self.ui.estado_button.clicked.connect(self.action_btn_estado)
        self.ui.tableProductos.currentCellChanged.connect(self.tabla_cell_changed)

    def tabla_cell_changed(self, currentRow, currentColumn, previousRow, previousColumn):
        item = self.ui.tableProductos.item(currentRow,0)
        try:
            self.id = item.text()
        except:
            pass

    def load_data_table(self):
        self.ui.tableProductos.sortItems(0, QtCore.Qt.AscendingOrder)
        self.ui.tableProductos.setColumnCount(8)
        self.ui.tableProductos.setHorizontalHeaderLabels(self.__header_table__)
        __check_icons__ = [(QtGui.QIcon(os.getcwd() + "/admin_productos/icons/red_check.png")),
                           (QtGui.QIcon(os.getcwd() + "/admin_productos/icons/green_check.png"))]

        productos = controller_admin_producto.Productos()
        row = len(productos)
        self.ui.tableProductos.setRowCount(row)

        for i, data in enumerate(productos):
            row = [QtGui.QTableWidgetItem(controller_admin_producto.zerosAtLeft(data.id_producto,2)),
                   QtGui.QTableWidgetItem(data.codigo),
                   QtGui.QTableWidgetItem(data.nombre),
                   QtGui.QTableWidgetItem(data.descripcion),
                   QtGui.QTableWidgetItem(controller_admin_producto.monetaryFormat(int(data.precio_neto))),
                   QtGui.QTableWidgetItem(controller_admin_producto.monetaryFormat(int(data.precio_bruto))),
                   QtGui.QTableWidgetItem(self.__type_productos__[int(data.id_categoria)]),
                   QtGui.QTableWidgetItem(__check_icons__[int(data.status)],"")]
            for j, cell in enumerate(row):
                self.ui.tableProductos.setItem(i,j,cell)

        self.ui.tableProductos.sortItems(0, QtCore.Qt.DescendingOrder)
        self.ui.tableProductos.setColumnHidden(0, True)
        self.ui.tableProductos.resizeColumnsToContents()
        self.ui.tableProductos.resizeColumnsToContents()
        self.ui.tableProductos.horizontalHeader().setResizeMode(
            3, self.ui.tableProductos.horizontalHeader().Stretch)

    def reload_data_table(self):
        self.ui.tableProductos.setRowCount(0)
        self.load_data_table()

    def action_btn_nuevo(self):
        """Metodo para lanzar el formulario de creacion del nuevo producto"""
        self.nuevoProductoWindow = view_formulario_producto.FormularioProducto()
        self.nuevoProductoWindow.reloadT.connect(self.reload_data_table)
        self.nuevoProductoWindow.exec_()
        # self.load_productos(self)

    def action_btn_editar(self):
        index = self.ui.tableProductos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado producto
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle(u"Error")
            msgBox.setText(u"Debe seleccionar un producto.")
            msgBox.exec_()
            return False
        else:
            self.editProductoWindow = view_formulario_producto.FormularioProducto(
                self.id)
            self.editProductoWindow.reloadT.connect(self.load_data_table)
            self.editProductoWindow.exec_()
            # self.load_productos(self)

    def action_btn_eliminar(self):
        """Accion a realizar al presionar el boton eliminar"""
        index = self.ui.tableProductos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado producto
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle(u"Error")
            msgBox.setText(u"Debe seleccionar un producto.")
            msgBox.exec_()
            return False
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setStandardButtons(
                QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msgBox.setWindowTitle(u"Advertencia")
            msgBox.setText(
                u"¿Esta seguro de querer eliminar el producto seleccionado?")
            press = msgBox.exec_()
            if press == QtGui.QMessageBox.Ok:
                producto = controller_admin_producto.deleteProducto(
                    self.id)
                self.reload_data_table()
                self.ui.tableProductos.setFocus()
            else:
                return False

    def action_btn_estado(self):
        """Accion a realizar al presionar el boton cambiar estado"""
        index = self.ui.tableProductos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado producto
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle(u"Error")
            msgBox.setText(u"Debe seleccionar un producto.")
            msgBox.exec_()
            return False
        else:
            data = controller_admin_producto.getProductoId(self.id)
            estado = data[0].status
            if(int(estado) == 0):
                producto = controller_admin_producto.UpdateStatusProducto(
                    self.id, 1)
            else:
                producto = controller_admin_producto.UpdateStatusProducto(
                    self.id, 0)
            self.load_data_table()
            self.ui.tableProductos.setFocus()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AdminProductos()
    myapp.show()
    sys.exit(app.exec_())
