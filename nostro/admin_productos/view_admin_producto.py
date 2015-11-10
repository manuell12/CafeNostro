#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from admin_producto import Ui_AdminProductos
import controller_admin_producto
import sys
import view_formulario_producto


class AdminProductos(QtGui.QDialog):

    __header_table__ = ((u"ID", 20),
                        (u"Nombre", 200),
                        (u"Descripcion", 200),
                        (u"Tipo", 120),
                        (u"Precio neto", 100),
                        (u"Categoria",100))

    __type_productos__ = ((u"------"),
                      (u"Comida"),
                      (u"Helado"),
                      (u"Café"),
                      (u"Bebida"))

    def __init__(self):
        'Constructor de la clase'
        QtGui.QDialog.__init__(self)
        # super(AdminProductos, self).__init__()
        self.ui = Ui_AdminProductos()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.setFocus()
        self.setModal(True)
        self.set_model_table()
        self.set_source_model(self.load_productos(self))
        self.ui.tableProductos.verticalHeader().setVisible(False)
        self.ui.tableProductos.setColumnHidden(3, True)
        self.connect_actions()
        self.show()

    def connect_actions(self):
        """Conectar botones con su respectiva accion"""
        self.ui.editar_button.clicked.connect(self.action_btn_editar)
        self.ui.nuevo_button.clicked.connect(self.action_btn_nuevo)
        self.ui.eliminar_button.clicked.connect(self.action_btn_eliminar)

    def reload_data_table(self):
        self.set_source_model(self.load_productos(self))

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
            msgBox.setWindowTitle("Error")
            msgBox.setText("Debe seleccionar un producto.")
            msgBox.exec_()
            return False
        else:
            self.editProductoWindow = view_formulario_producto.FormularioProducto(
                self.id)
            self.editProductoWindow.reloadT.connect(self.reload_data_table)
            self.editProductoWindow.exec_()
            # self.load_productos(self)

    def action_btn_eliminar(self):
        """Accion a realizar al presionar el boton eliminar"""
        index = self.ui.tableProductos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado producto
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Debe seleccionar un producto.")
            msgBox.exec_()
            return False
        else:
            producto = controller_admin_producto.UpdateStatusProducto(0,self.id)
            self.reload_data_table()

    def load_productos(self, parent):
        """
        Carga la información de la base de datos en la tabla.
        Obtiene desde la base de datos a traves del controlador
        la información completa de la tabla.
        Crea un model para adjuntar los datos a la grilla y luego
        lo retorna para utilizarlo en setSourceModel.
        """
        self.typeModelClass = parent

        productos = controller_admin_producto.Productos()
        row = len(productos)

        model = QtGui.QStandardItemModel(row, len(self.__header_table__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)

        for i, data in enumerate(productos):
            row = [data[0], data[1], data[2], data[3], str(data[4]), data[6]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 5:
                    model.setData(index, self.__type_productos__[field])
                else:
                    model.setData(index, field)

        modelSel = self.ui.tableProductos.selectionModel()
        modelSel.currentChanged.connect(self.tabla_cell_selected)

        return model

    def tabla_cell_selected(self, index, indexp):
        model = self.ui.tableProductos.model()
        index = self.ui.tableProductos.currentIndex()
        self.id = model.index(index.row(), 0, QtCore.QModelIndex()).data()

    def set_model_table(self):
        """Define el módelo de la grilla para trabajarla."""
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.ui.tableProductos.setModel(self.proxyModel)

    def set_source_model(self, model):
        """
        Actualiza constantemente el origen de los datos para siempre tenerlos
        al día así pudiendo buscar y mostrar solo algunos datos.
        Además llama a las funciones que rellenan los comboBox de filtrado y
        asigna el tamaño de las columnas a las grillas respectivas.
        """
        self.proxyModel.setSourceModel(model)

        # Designamos los header de la grilla y sus respectivos anchos
        for col, h in enumerate(self.__header_table__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableProductos.setColumnWidth(col, h[1])

        self.ui.tableProductos.sortByColumn(0, QtCore.Qt.AscendingOrder)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = AdminProductos()
    myapp.show()
    sys.exit(app.exec_())