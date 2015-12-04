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
                        (u"Código", 50),
                        (u"Nombre", 400),
                        (u"Precio bruto", 100))

    __header_table2__ = ((u"ID", 20),
                         (u"Código", 50),
                         (u"Nombre", 300),
                         (u"Cantidad", 100),
                         (u"Precio bruto", 100))

    id_tablaP = 0
    id_tablaPd = 0

    def __init__(self, main, rut_usuario, mesa):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_FormularioVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.connect_actions()
        self.main = main
        self.mesa = mesa
        self.id_pedido = controller.addDataPedido(self.mesa)
        self.rut_usuario = rut_usuario

        self.load_model_total_productos(controller.getProductoStatus(1))
        self.reload_data_table2()
        self.set_combobox_tipo_pago()

    def set_combobox_tipo_pago(self):
        __type_pay__ = ((u"EFECTIVO"),
                        (u"TARJETA"))

        model = QtGui.QStandardItemModel()
        for text in __type_pay__:
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

    def connect_actions(self):
        self.ui.pushButton_agregar.clicked.connect(self.action_agregar)
        self.ui.pushButton_eliminar.clicked.connect(self.action_eliminar)
        self.ui.pushButton_opciones.clicked.connect(self.action_opciones)
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
        productos = controller.getProductoCategoria(3)
        self.load_model_total_productos(productos)

    def action_cocina(self):
        productos = controller.getProductoCategoria(1)
        self.load_model_total_productos(productos)

    def action_bebidas(self):
        productos = controller.getProductoCategoria(4)
        self.load_model_total_productos(productos)

    def action_helados(self):
        productos = controller.getProductoCategoria(2)
        self.load_model_total_productos(productos)

    def lineEdit_buscar_codigo_changed(self, text):
        productos = controller.getProductoCodigo(text)
        self.load_model_total_productos(productos)

    """ ============================================================================= TABLA TOTAL PRODUCTOS ============================================="""

    def cell_selected_table1(self, index, indexp):
        model = self.ui.tableView_total_productos.model().sourceModel()
        self.id_tablaP = int(model.item(index.row(), 0).text())
        self.nombre_tablaP = model.item(index.row(), 2).text()
        self.precio_tablaP = model.item(index.row(), 3).text()
        precio = self.precio_tablaP.split(".")
        self.precio_tablaP = ""
        for i in range(len(precio)):
            self.precio_tablaP = self.precio_tablaP + precio[i]

    def load_model_total_productos(self, data=""):
        model = controller.TotalProductosModel()
        self.ui.tableView_total_productos.setModel(model)
        model.load_data(data, self.__header_table__)

        self.set_columns_total_productos()

    def set_columns_total_productos(self):
        self.ui.tableView_total_productos.horizontalHeader().setResizeMode(
            2, self.ui.tableView_total_productos.horizontalHeader().Stretch)

        for col, h in enumerate(self.__header_table__):
            self.ui.tableView_total_productos.setColumnWidth(col, h[1])

        self.ui.tableView_total_productos.sortByColumn(
            0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_total_productos.setColumnHidden(0, True)

        modelSel = self.ui.tableView_total_productos.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table1)

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
            # self.edit = False
            # print("Edit False")
            # self.ui.pushButton_imprimir_comandas.setEnabled(True)
            # self.ui.pushButton_cerrar_venta.setText("Cerrar Venta")
            productos = controller.getProductosPedido(self.id_pedido)
            # print(productos)
        else:
            # print(pedido)
            self.edit = True
            #print("Edit True")
            # self.ui.pushButton_imprimir_comandas.setEnabled(False)
            #self.ui.pushButton_cerrar_venta.setText("Guardar Cambios")
            productos = controller.getProductosPedido(pedido)
            self.id_pedido = pedido
            # print(productos)
        row = len(productos)
        # print("Total productos: {}".format(row))

        model = QtGui.QStandardItemModel(row, len(self.__header_table2__))
        # model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)
        subtotal = 0

        for i, data in enumerate(productos):
            row = [data.id_producto, controller.getProductoId(data.id_producto)[0].codigo, controller.getProductoId(data.id_producto)[
                0].nombre, data.cantidad, c.monetaryFormat(str(data.precio_venta).split(".")[0])]
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
            index.row(), 4, QtCore.QModelIndex()).data()
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
            2, self.ui.tableView_pedido.horizontalHeader().Stretch)

        # Designamos los header de la grilla y sus respectivos anchos
        for col, h in enumerate(self.__header_table2__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableView_pedido.setColumnWidth(col, h[1])

        self.ui.tableView_pedido.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_pedido.setColumnHidden(0, True)

    """ ===================================================================== NUMERO DE PAGOS ============================================================ """

    def action_opciones(self):
        self.n_pagos = self.ui.label_numero_pagos.text()
        self.nPagosDialog = self.createPagosWindow(1)
        self.nPagosDialog.exec_()

    def action_numero_pagos(self):
        self.n_pagos = int(self.lineEdit_pagos[0].text())
        aux = self.lineEdit_pagos[0]
        self.clearLayout(self.groupBox.layout())
        self.lineEdit_pagos = list()
        self.lineEdit_pagos.append(aux)

        for i in range(self.n_pagos):
            label = QtGui.QLabel("Pago " + str(i + 1) + ": ")
            line_edit = QtGui.QLineEdit()
            self.lineEdit_pagos.append(line_edit)
            horizontalLayout = QtGui.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(line_edit)
            self.verticalLayout2.addLayout(horizontalLayout)

        for i, lineEdit in enumerate(self.lineEdit_pagos):
            if(i == 0):
                lineEdit.setText(str(self.n_pagos))
            else:
                lineEdit.setText(
                    str(int(self.ui.lcdNumber_total.value() / self.n_pagos)))

    def action_guardar_pagos(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setStandardButtons(
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setWindowTitle(u"Advertencia")
        msgBox.setText(
            u"Confirme para realizar venta")
        press = msgBox.exec_()
        if press == QtGui.QMessageBox.Ok:
            self.agregarVenta()
            for i, lineEdit in enumerate(self.lineEdit_pagos):
                if(i != 0):
                    total_pago = int(lineEdit.text())
                    efectivo = int(lineEdit.text())
                    tarjeta = 0
                    id_pedido = int(self.id_pedido)
                    propina = self.ui.lcdNumber_propina.value()
                    id_venta = controller.getVentaPedidoId(id_pedido)[
                        0].id_venta
                    controller.addDataPago(
                        total_pago, efectivo, tarjeta, propina, id_venta)
                    self.nPagosDialog.close()
            self.main.stackedWidget.widget(5).reload_data_table()
            self.id_pedido = controller.addDataPedido(self.mesa)
            self.reload_data_table2()
        else:
            return False

    def createPagosWindow(self, pagos):
        self.n_pagos = pagos
        w = QtGui.QDialog()
        w.resize(400, 100)
        w.setWindowTitle("Gestionar pagos")

        self.groupBox = QtGui.QGroupBox()
        self.groupBox.setTitle("Pagos")

        verticalLayout1 = QtGui.QVBoxLayout()

        label = QtGui.QLabel(u"Número de pagos: ")
        lineEdit_numero_pagos = QtGui.QLineEdit(str(self.n_pagos))
        pushButton_numero_pagos = QtGui.QPushButton("Aceptar")
        pushButton_guardar_pagos = QtGui.QPushButton("Pagar")
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(label)
        horizontalLayout.addWidget(lineEdit_numero_pagos)
        horizontalLayout.addWidget(pushButton_numero_pagos)
        verticalLayout1.addLayout(horizontalLayout)

        self.verticalLayout2 = QtGui.QVBoxLayout(self.groupBox)

        self.lineEdit_pagos = list()
        self.lineEdit_pagos.append(lineEdit_numero_pagos)

        for i in range(self.n_pagos):
            label = QtGui.QLabel("Pago " + str(i + 1) + ": ")
            line_edit = QtGui.QLineEdit()
            self.lineEdit_pagos.append(line_edit)
            horizontalLayout = QtGui.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(line_edit)
            self.verticalLayout2.addLayout(horizontalLayout)

        self.lineEdit_pagos[1].setText(
            str(int(self.ui.lcdNumber_total.value())))

        mainVLayout = QtGui.QVBoxLayout()
        mainVLayout.addLayout(verticalLayout1)
        mainVLayout.addWidget(self.groupBox)
        mainVLayout.addWidget(pushButton_guardar_pagos)

        mainHLayout = QtGui.QHBoxLayout()
        mainHLayout.addLayout(mainVLayout)

        w.setLayout(mainHLayout)

        pushButton_numero_pagos.clicked.connect(self.action_numero_pagos)
        pushButton_guardar_pagos.clicked.connect(self.action_guardar_pagos)
        return w

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    """ ======================================================================= CERRAR VENTA ============================================================ """

    def action_cerrar_venta(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setStandardButtons(
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setWindowTitle(u"Advertencia")
        msgBox.setText(
            u"Confirme para realizar venta")
        press = msgBox.exec_()
        if press == QtGui.QMessageBox.Ok:
            try:
                if self.edit is True:
                    self.editarVenta()
                else:
                    self.agregarVenta()
                    self.agregarPedido()
                    self.main.stackedWidget.widget(5).reload_data_table()
                    self.id_pedido = controller.addDataPedido(self.mesa)
                    self.reload_data_table2()
            except:
                self.agregarVenta()
                self.agregarPedido()
                self.main.stackedWidget.widget(5).reload_data_table()
                self.id_pedido = controller.addDataPedido(self.mesa)
                self.reload_data_table2()
        else:
            return False

    def agregarVenta(self):
        y = int(time.strftime("%Y"))
        m = int(time.strftime("%m"))
        d = int(time.strftime("%d"))
        fecha = datetime.date(y, m, d)
        try:
            num_documento = controller.getVentas()[-1].num_documento + 1
        except:
            num_documento = 0
        if(self.mesa == "0"):
            tipo = "directa"
        else:
            tipo = "pedido por mesa"
# =======
#         fecha = datetime.date(y, m, d)
#         num_documento = len(controller.getVentas())
#         tipo = "directa"
# >>>>>>> EditarVenta
        total_pago = self.ui.lcdNumber_total.value()
        id_pedido = int(self.id_pedido)
        id_usuario = int(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].id_usuario)
        controller.addDataVenta(fecha, num_documento,
                                tipo, total_pago, id_usuario, id_pedido)

    def editarVenta(self):
        print("-----Editar Venta-----")
        y = int(time.strftime("%Y"))
        m = int(time.strftime("%m"))
        d = int(time.strftime("%d"))
        fecha = datetime.date(y, m, d)
        # num_documento = len(controller.getVentas())
        # tipo = "directa"
        total_pago = self.ui.lcdNumber_total.value()
        id_venta = controller.getIdVenta(int(self.id_pedido))
        id_usuario = int(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].id_usuario)

        controller.editDataVenta(id_venta, fecha, total_pago, id_usuario)

    def agregarPedido(self):
        total_pago = self.ui.lcdNumber_total.value()
        if(int(self.ui.comboBox_tipo_pago.currentIndex()) == 0):  # efectivo
            efectivo = total_pago
            tarjeta = 0
        else:
            tarjeta = total_pago
            efectivo = 0
        propina = self.ui.lcdNumber_propina.value()
        id_venta = controller.getVentaPedidoId(id_pedido)[0].id_venta
        controller.addDataPago(total_pago, efectivo,
                               tarjeta, propina, id_venta)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FormularioVenta()
    myapp.show()
    sys.exit(app.exec_())
