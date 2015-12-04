#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from formulario_venta import Ui_FormularioVenta
import sys
import controller_venta as controller
import admin_productos.controller_admin_producto as c
import admin_usuarios.controller_admin_user as controller_admin_user
from ventas.view_admin_venta import AdminVentas
import datetime
import time


class FormularioVenta(QtGui.QWidget):

    __header_table__ = ((u"ID", 20),
                        (u"Nombre", 400),
                        (u"Precio bruto", 100))

    __header_table2__ = ((u"ID", 20),
                         (u"Nombre", 300),
                         (u"Cantidad", 100),
                         (u"Precio bruto", 100))

    __type_pay__ = ((u"EFECTIVO"),
                    (u"TARJETA"))
    id_tablaP = 0
    id_tablaPd = 0

    def __init__(self, rut_usuario, mesa):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_FormularioVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.connect_actions()
        if(mesa == "0"):
            self.id_pedido = controller.addDataPedido(mesa)
        self.rut_usuario = rut_usuario

        self.reload_data_table1()
        self.reload_data_table2()

        model = QtGui.QStandardItemModel()
        for text in self.__type_pay__:
            text_item = QtGui.QStandardItem(text)
            text_item.setSizeHint(QtCore.QSize(100, 50))
            text_item.setTextAlignment(QtCore.Qt.AlignHCenter)
            text_item.setTextAlignment(QtCore.Qt.AlignVCenter)
            model.appendRow([text_item])
        view = QtGui.QTreeView()
        view.header().hide()
        view.setRootIsDecorated(False)
        self.ui.comboBox_tipo_pago.setView(view)
        self.ui.comboBox_tipo_pago.setModel(model)
        self.ui.comboBox_tipo_pago.setEditable(True)
        self.ui.comboBox_tipo_pago.lineEdit().setAlignment(QtCore.Qt.AlignHCenter)
        self.ui.comboBox_tipo_pago.setEditable(False)

    def connect_actions(self):
        self.ui.pushButton_agregar.clicked.connect(self.action_agregar)
        self.ui.pushButton_eliminar.clicked.connect(self.action_eliminar)
        self.ui.pushButton_aumentar_cantidad.clicked.connect(
            self.action_aumentar)
        self.ui.pushButton_disminuir_cantidad.clicked.connect(
            self.action_disminuir)
        self.ui.pushButton_filtrar_cafeteria.clicked.connect(
            self.action_cafeteria)
        self.ui.pushButton_filtrar_cocina.clicked.connect(self.action_cocina)
        self.ui.pushButton_filtrar_bebidas.clicked.connect(self.action_bebidas)
        self.ui.pushButton_filtrar_helados.clicked.connect(self.action_helados)
        self.ui.pushButton_cerrar_venta.clicked.connect(
            self.action_cerrar_venta)
        self.ui.lineEdit_buscar_codigo.textChanged.connect(
            self.lineEdit_buscar_codigo_changed)

    def action_agregar(self):
        controller.addDataVentaProducto(
            self.id_pedido, self.id_tablaP, self.precio_tablaP)
        self.reload_data_table2()
        self.ui.tableView_total_productos.setFocus()

    def action_eliminar(self):
        controller.deleteProducto(self.id_pedido, self.id_tablaPd)
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()

    def action_aumentar(self):
        controller.cambiarCantidadProducto(
            self.id_pedido, self.id_tablaPd, "aumentar")
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()

    def action_disminuir(self):
        controller.cambiarCantidadProducto(
            self.id_pedido, self.id_tablaPd, "disminuir")
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()

    """" ================================ FILTROS TABLA TOTAL PRODUCTOS =================================== """

    def action_cafeteria(self):
        self.filtrar_data_table1("categoria", 3)

    def action_cocina(self):
        self.filtrar_data_table1("categoria", 1)

    def action_bebidas(self):
        self.filtrar_data_table1("categoria", 4)

    def action_helados(self):
        self.filtrar_data_table1("categoria", 2)

    def lineEdit_buscar_codigo_changed(self, text):
        self.filtrar_data_table1("codigo", text)

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
        if(tipo == "codigo"):
            productos = controller.getProductoCodigo(valor)

        if(tipo == None and valor == None):
            productos = controller.getProductoStatus(1)

        row = len(productos)

        model = QtGui.QStandardItemModel(row, len(self.__header_table__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)

        for i, data in enumerate(productos):
            row = [data.id_producto, data.nombre, c.monetaryFormat(
                str(data.precio_bruto).split(".")[0])]
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

    def filtrar_data_table1(self, tipo, valor):
        self.set_model_table1()
        self.set_source_model_table1(
            self.load_productos_table1(self, tipo, valor))

    def cell_selected_table1(self, index, indexp):
        model = self.ui.tableView_total_productos.model()
        index = self.ui.tableView_total_productos.currentIndex()
        self.id_tablaP = model.index(
            index.row(), 0, QtCore.QModelIndex()).data()
        self.nombre_tablaP = model.index(
            index.row(), 1, QtCore.QModelIndex()).data()
        self.precio_tablaP = model.index(
            index.row(), 2, QtCore.QModelIndex()).data()
        precio = self.precio_tablaP.split(".")
        self.precio_tablaP = ""
        for i in range(len(precio)):
            self.precio_tablaP = self.precio_tablaP + precio[i]

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

        self.ui.tableView_total_productos.sortByColumn(
            0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_total_productos.setColumnHidden(0, True)

    """ ======================================================================= TABLA PRODUCTOS PEDIDOS ============================================================ """

    def load_productos_table2(self, pedido=None):
        """
        Carga la información de la base de datos en la tabla.
        Obtiene desde la base de datos a traves del controlador
        la información completa de la tabla.
        Crea un model para adjuntar los datos a la grilla y luego
        lo retorna para utilizarlo en setSourceModel.
        """
        # self.typeModelClass = parent
        # print("load_productos_table2 pedido: {}".format(pedido))
        if pedido is None:
            productos = controller.getProductosPedido(self.id_pedido)
            # print(productos)
        else:
            # print(pedido)
            productos = controller.getProductosPedido(pedido)
            self.id_pedido = pedido
            # print(productos)
        row = len(productos)
        # print("Total productos: {}".format(row))

        model = QtGui.QStandardItemModel(row, len(self.__header_table2__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)
        subtotal = 0

        for i, data in enumerate(productos):
            print(type(controller.getProductoId(data.id_producto)[
                0].nombre))
            row = [data.id_producto, (controller.getProductoId(data.id_producto)[
                0].nombre), data.cantidad, c.monetaryFormat(str(data.precio_venta).split(".")[0])]
            subtotal = subtotal + (long(data.precio_venta) * data.cantidad)
            for j, field in enumerate(row):
                print(row)
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 5:
                    model.setData(index, self.__type_productos__[field])
                else:
                    model.setData(index, field)

        self.ui.lcdNumber_subtotal.setDecMode()
        self.ui.lcdNumber_propina.setDecMode()
        self.ui.lcdNumber_total.setDecMode()
        self.ui.lcdNumber_subtotal.display(subtotal)
        self.ui.lcdNumber_propina.display(subtotal * 0.1)
        self.ui.lcdNumber_total.display(subtotal * 1.1)

        modelSel = self.ui.tableView_pedido.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table2)

        if pedido is None:
            return model
        else:
            self.set_source_model_table2(model)

    def reload_data_table2(self):        
        self.set_model_table2()
        self.set_source_model_table2(
            self.load_productos_table2())  # table2(self)

    def cell_selected_table2(self, index, indexp):
        model = self.ui.tableView_pedido.model()
        index = self.ui.tableView_pedido.currentIndex()
        self.row_tablaPd = index.row()
        self.id_tablaPd = model.index(
            index.row(), 0, QtCore.QModelIndex()).data()
        self.precio_tablaPd = model.index(
            index.row(), 3, QtCore.QModelIndex()).data()
        # self.ui.lcdNumber_subtotal.display(self.id)

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

    """ ======================================================================= CERRAR VENTA ============================================================ """

    def action_cerrar_venta(self):
        self.agregarVenta()

    def agregarVenta(self):
        y = int(time.strftime("%Y"))
        m = int(time.strftime("%m"))
        d = int(time.strftime("%d"))
        fecha = datetime.date(y, m, d)
        num_documento = len(controller.getVentas())
        tipo = "directa"
        total_pago = self.ui.lcdNumber_total.value()
        id_pedido = int(self.id_pedido)
        id_usuario = int(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].id_usuario)
        controller.addDataVenta(fecha, num_documento,
                                tipo, total_pago, id_usuario, id_pedido)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FormularioVenta()
    myapp.show()
    sys.exit(app.exec_())
