#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from admin_venta import Ui_AdminVentas
import controller_venta
import sys
import admin_productos.controller_admin_producto as c
import admin_usuarios.controller_admin_user as controller
#import view_formulario_admin_venta


class AdminVentas(QtGui.QWidget):

    __header_table__ = ((u"ID", 20),
                        (u"Número documento", 150),
                        (u"Fecha", 200),
                        (u"Tipo", 120),
                        (u"Total pago", 100),
                        (u"Usuario encargado", 200))

    def __init__(self, parent=None, formularioVenta=None):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_AdminVentas()
        self.ui.setupUi(self)
        self.setFocus()
        self.set_model_table()
        self.set_source_model(self.load_ventas(self))
        self.ui.tableView_ventas.verticalHeader().setVisible(False)
        self.ui.tableView_ventas.setColumnHidden(0, True)
        self.connect_actions()
        self.mainwindow = parent
        self.formularioVenta = formularioVenta

    def connect_actions(self):
        """Conectar botones con su respectiva accion"""
        self.ui.pushButton_editar.clicked.connect(self.action_btn_editar)
        self.ui.pushButton_eliminar.clicked.connect(self.action_btn_eliminar)
        # self.ui.tableView_ventas.viewportEntered.connect(self.mouse_entered)

    def reload_data_table(self):
        self.set_source_model(self.load_ventas(self))

    def mouse_entered(self):
        self.reload_data_table()

    def action_btn_editar(self):
        """
        Luego de seleccionar una venta de la lista cambia a  la ventana
        de venta con los datos de la venta seleccionada para poder realizar
        cambios en ella.
        """
        index = self.ui.tableView_ventas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado venta
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Debe seleccionar un venta.")
            msgBox.exec_()
            return False
        else:
            model = self.ui.tableView_ventas.model()
            id_venta = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            print("ID Venta {}".format(id_venta))
            id_pedido = controller_venta.getIdPedido(id_venta)
            print("ID Pedido {}".format(id_pedido))
            # print(id_pedido)
            # productos = controller_venta.getProductosPedido(id_pedido)
            # # print(len(productos))

            # for producto in productos:
            #     for c in range(0, producto.cantidad):
            #         print("{}\t{}\t{}\t{}\t{}".format(
            #             producto.id_pedido,
            #             producto.id_producto,
            #             producto.cantidad,
            #             producto.precio_venta,
            #             producto.porcentaje_descuento))
            #         controller_venta.addDataVentaProducto(
            #             producto.id_pedido,
            #             producto.id_producto,
            #             producto.precio_venta)

            self.mainwindow.stackedWidget.setCurrentIndex(4)
            self.mainwindow.stackedWidget.currentWidget().id_pedido = id_pedido
            self.mainwindow.stackedWidget.currentWidget().reload_data_table2()
            self.mainwindow.stackedWidget.currentWidget().load_productos_table2(id_pedido)
            self.set_source_model(self.load_ventas(self))

    def action_btn_eliminar(self):
        """Accion a realizar al presionar el boton eliminar"""
        index = self.ui.tableView_ventas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado venta
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Debe seleccionar un venta.")
            msgBox.exec_()
            return False
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setStandardButtons(
                QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            msgBox.setWindowTitle(u"Advertencia")
            msgBox.setText(
                u"¿Esta seguro de querer eliminar la venta seleccionada?")
            press = msgBox.exec_()
            if press == QtGui.QMessageBox.Ok:
                model = self.ui.tableView_ventas.model()
                id_venta = model.index(
                    index.row(), 0, QtCore.QModelIndex()).data()
                id_pedido = controller_venta.getIdPedido(id_venta)
                mensaje = controller_venta.delete_venta(id_venta, id_pedido)
                if mensaje == "Error":
                    msgBox = QtGui.QMessageBox()
                    msgBox.setIcon(QtGui.QMessageBox.Critical)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Esta venta no puede ser eliminada por tener productos asociados.")
                    msgBox.exec_()
                else:
                    self.set_source_model(self.load_ventas(self))
            else:
                return False

    def load_ventas(self, parent):
        """
        Carga la información de la base de datos en la tabla.
        Obtiene desde la base de datos a traves del controlador
        la información completa de la tabla.
        Crea un model para adjuntar los datos a la grilla y luego
        lo retorna para utilizarlo en setSourceModel.
        """
        self.typeModelClass = parent

        ventas = controller_venta.getVentas()
        row = len(ventas)

        model = QtGui.QStandardItemModel(row, len(self.__header_table__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)

        for i, data in enumerate(ventas):
            row = [data.id_venta, c.zerosAtLeft(data.num_documento, 8), str(data.fecha), data.tipo, c.monetaryFormat(int(data.total_pago)), unicode(
                controller.getUsuarioId(data.id_usuario)[0].nombre) + " " + unicode(controller.getUsuarioId(data.id_usuario)[0].apellido)]
            # row = [data.id_venta, data.num_documento, str(data.fecha), data.tipo, c.monetaryFormat(int(data.total_pago)), unicode(
            # controller.getUsuarioId(data.id_usuario)[0].nombre) + " " +
            # unicode(controller.getUsuarioId(data.id_usuario)[0].apellido)]

            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 4:
                    # print self.__type_ventas__[field]
                    model.setData(index, field)
                else:
                    model.setData(index, field)

        modelSel = self.ui.tableView_ventas.selectionModel()
        modelSel.currentChanged.connect(self.tabla_cell_selected)

        return model

    def tabla_cell_selected(self, index, indexp):
        model = self.ui.tableView_ventas.model()
        index = self.ui.tableView_ventas.currentIndex()
        self.id = model.index(index.row(), 0, QtCore.QModelIndex()).data()

    def set_model_table(self):
        """Define el módelo de la grilla para trabajarla."""
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.ui.tableView_ventas.setModel(self.proxyModel)

    def set_source_model(self, model):
        """
        Actualiza constantemente el origen de los datos para siempre tenerlos
        al día así pudiendo buscar y mostrar solo algunos datos.
        Además llama a las funciones que rellenan los comboBox de filtrado y
        asigna el tamaño de las columnas a las grillas respectivas.
        """
        self.proxyModel.setSourceModel(model)

        self.ui.tableView_ventas.horizontalHeader().setResizeMode(
            2, self.ui.tableView_ventas.horizontalHeader().Stretch)
        self.ui.tableView_ventas.horizontalHeader().setResizeMode(
            3, self.ui.tableView_ventas.horizontalHeader().Stretch)

        # Designamos los header de la grilla y sus respectivos anchos
        for col, h in enumerate(self.__header_table__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableView_ventas.setColumnWidth(col, h[1])

        self.ui.tableView_ventas.sortByColumn(0, QtCore.Qt.AscendingOrder)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AdminVentas()
    myapp.show()
    sys.exit(app.exec_())
