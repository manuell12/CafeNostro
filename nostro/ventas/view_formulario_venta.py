#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from formulario_venta import Ui_FormularioVenta
import sys
import controller_venta as controller

class FormularioVenta(QtGui.QWidget):

    __header_table__ = ((u"ID", 20),
                        (u"Nombre", 400),
                        (u"Precio bruto", 100))

    __header_table2__ = ((u"ID", 20),
                         (u"Nombre", 300),
                         (u"Cantidad", 100),
                         (u"Precio bruto", 100))

    def __init__(self, rut_usuario, mesa):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_FormularioVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.connect_actions()
        if(mesa == "0"):
            self.id_pedido = controller.addDataPedido(mesa)

        self.reload_data_table1()
        self.reload_data_table2()


    def connect_actions(self):
        self.ui.pushButton_agregar.clicked.connect(self.action_agregar)
        self.ui.pushButton_eliminar.clicked.connect(self.action_eliminar)
        self.ui.pushButton_aumentar_cantidad.clicked.connect(self.action_aumentar)
        self.ui.pushButton_disminuir_cantidad.clicked.connect(self.action_disminuir)
        self.ui.pushButton_filtrar_cafeteria.clicked.connect(self.action_cafeteria)
        self.ui.pushButton_filtrar_cocina.clicked.connect(self.action_cocina)
        self.ui.pushButton_filtrar_bebidas.clicked.connect(self.action_bebidas)
        self.ui.pushButton_filtrar_helados.clicked.connect(self.action_helados)


    def action_agregar(self):
        controller.addDataVentaProducto(self.id_pedido,self.id_tablaP,self.precio_tablaP)
        self.reload_data_table2()

    def action_eliminar(self):
        controller.deleteProducto(self.id_pedido,self.id_tablaPd)
        self.reload_data_table2()

    def action_aumentar(self):
        controller.cambiarCantidadProducto(self.id_pedido, self.id_tablaPd, "aumentar")
        self.reload_data_table2()

    def action_disminuir(self):
        controller.cambiarCantidadProducto(self.id_pedido, self.id_tablaPd, "disminuir")
        self.reload_data_table2()

    """" ================================ FILTROS TABLA TOTAL PRODUCTOS =================================== """

    def action_cafeteria(self):
        self.filtrar_data_table1("categoria",3)

    def action_cocina(self):
        self.filtrar_data_table1("categoria",1)

    def action_bebidas(self):
        self.filtrar_data_table1("categoria",4)

    def action_helados(self):
        self.filtrar_data_table1("categoria",2)

    """ ============================================================================= TABLA TOTAL PRODUCTOS ============================================="""

    def load_productos_table1(self, parent, tipo=None, valor=None):
        """
        Carga la información de la base de datos en la tabla.
        Obtiene desde la base de datos a traves del controlador
        la información completa de la tabla.
        Crea un model para adjuntar los datos a la grilla y luego
        lo retorna para utilizarlo en setSourceModel.
        """

        if(tipo == "categoria"):
            if(valor == 1):
                productos = controller.getProductoCategoria(1)
            if(valor == 2):
                productos = controller.getProductoCategoria(2)
            if(valor == 3):
                productos = controller.getProductoCategoria(3)
            if(valor == 4):
                productos = controller.getProductoCategoria(4)

        if(tipo == None and valor == None):
            productos = controller.getProductoStatus(1)

        row = len(productos)

        model = QtGui.QStandardItemModel(row, len(self.__header_table__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)

        for i, data in enumerate(productos):
            row = [data.id_producto, data.nombre, str(data.precio_bruto).split(".")[0]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 5:
                    model.setData(index, self.__type_productos__[field])
                else:
                    model.setData(index, field)

        modelSel = self.ui.tableView_total_productos.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table1)

        return model

    def reload_data_table1(self):
        self.set_model_table1()
        self.set_source_model_table1(self.load_productos_table1(self))

    def filtrar_data_table1(self,tipo,valor):
        self.set_model_table1()
        self.set_source_model_table1(self.load_productos_table1(self,tipo,valor))

    def cell_selected_table1(self, index, indexp):
        model = self.ui.tableView_total_productos.model()
        index = self.ui.tableView_total_productos.currentIndex()
        self.id_tablaP = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        self.nombre_tablaP = model.index(index.row(), 1, QtCore.QModelIndex()).data()
        self.precio_tablaP = model.index(index.row(), 2, QtCore.QModelIndex()).data()

    def set_model_table1(self):
        """Define el módelo de la grilla para trabajarla."""
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.ui.tableView_total_productos.setModel(self.proxyModel)
        

    def set_source_model_table1(self, model):
        """
        Actualiza constantemente el origen de los datos para siempre tenerlos
        al día así pudiendo buscar y mostrar solo algunos datos.
        Además llama a las funciones que rellenan los comboBox de filtrado y
        asigna el tamaño de las columnas a las grillas respectivas.
        """
        self.proxyModel.setSourceModel(model)

        self.ui.tableView_total_productos.horizontalHeader().setResizeMode(
            1, self.ui.tableView_total_productos.horizontalHeader().Stretch)


        # Designamos los header de la grilla y sus respectivos anchos
        for col, h in enumerate(self.__header_table__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableView_total_productos.setColumnWidth(col, h[1])

        self.ui.tableView_total_productos.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_total_productos.setColumnHidden(0, True)

    """ ======================================================================= TABLA PRODUCTOS PEDIDOS ============================================================ """

    def load_productos_table2(self, parent):
        """
        Carga la información de la base de datos en la tabla.
        Obtiene desde la base de datos a traves del controlador
        la información completa de la tabla.
        Crea un model para adjuntar los datos a la grilla y luego
        lo retorna para utilizarlo en setSourceModel.
        """
        #self.typeModelClass = parent

        productos = controller.getProductosPedido(self.id_pedido)
        row = len(productos)

        model = QtGui.QStandardItemModel(row, len(self.__header_table2__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)
        subtotal = 0

        for i, data in enumerate(productos):
            row = [data.id_producto, controller.getProductoId(data.id_producto)[0].nombre, data.cantidad, str(data.precio_venta).split(".")[0]]
            subtotal = subtotal + (long(data.precio_venta)*data.cantidad)
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 5:
                    model.setData(index, self.__type_productos__[field])
                else:
                    model.setData(index, field)

        self.ui.lcdNumber_subtotal.display(subtotal)
        self.ui.lcdNumber_propina.display(subtotal*0.1)
        self.ui.lcdNumber_total.display(subtotal*1.1)

        modelSel = self.ui.tableView_pedido.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table2)

        return model

    def reload_data_table2(self):
        self.set_model_table2()
        self.set_source_model_table2(self.load_productos_table2(self))

    def cell_selected_table2(self, index, indexp):
        model = self.ui.tableView_pedido.model()
        index = self.ui.tableView_pedido.currentIndex()
        self.id_tablaPd = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        self.precio_tablaPd = model.index(index.row(), 3, QtCore.QModelIndex()).data()
        #self.ui.lcdNumber_subtotal.display(self.id)

    def set_model_table2(self):
        """Define el módelo de la grilla para trabajarla."""
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        
        self.ui.tableView_pedido.setModel(self.proxyModel)

    def set_source_model_table2(self, model):
        """
        Actualiza constantemente el origen de los datos para siempre tenerlos
        al día así pudiendo buscar y mostrar solo algunos datos.
        Además llama a las funciones que rellenan los comboBox de filtrado y
        asigna el tamaño de las columnas a las grillas respectivas.
        """
        self.proxyModel.setSourceModel(model)

        self.ui.tableView_pedido.horizontalHeader().setResizeMode(
            1, self.ui.tableView_pedido.horizontalHeader().Stretch)

        # Designamos los header de la grilla y sus respectivos anchos
        for col, h in enumerate(self.__header_table2__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableView_pedido.setColumnWidth(col, h[1])

        self.ui.tableView_pedido.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_pedido.setColumnHidden(0, True)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FormularioVenta()
    myapp.show()
    sys.exit(app.exec_())
