#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from numero_pagos import Ui_NumeroPagos
import ventas.controller_venta as controller
import admin_productos.controller_admin_producto as controller_admin_producto

class NumeroPagos(QtGui.QDialog):

    __header_table__ = (u"ID",
                        u"Código",
                        u"Nombre",
                        u"Precio bruto",
                        u"Pago")

    def __init__(self, pedido, ventaForm, subtotal):
        'Constructor de la clase'
        super(NumeroPagos, self).__init__()
        self.ui = Ui_NumeroPagos()
        self.ui.setupUi(self)
        self.id_pedido = pedido
        self.ventaForm = ventaForm
        self.subtotal = subtotal
        self.ui.lcdNumber_subtotal.display(subtotal)
        self.ui.lcdNumber_propina.display(subtotal * 0.1)
        self.ui.lcdNumber_total.display(subtotal * 1.1)
        self.show()
        self.ui.spinBox_numero_pagos.setRange(1,20)
        self.n_pagos = self.ui.spinBox_numero_pagos.value()
        self.ui.spinBox_numero_pagos.valueChanged.connect(self.spinBox_numero_pagos_changed)
        self.ui.pushButton_pagar.clicked.connect(self.action_pagar)

        self.label_pagos = list()

        for i in range(self.n_pagos):
            label = QtGui.QLabel("Pago " + str(i + 1) + ": ")
            label_pagos = QtGui.QLabel()
            self.label_pagos.append(label_pagos)
            horizontalLayout = QtGui.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(label_pagos)
            self.ui.verticalLayout_numero_pagos.addLayout(horizontalLayout)

        self.load_data_table()

    def spinBox_numero_pagos_changed(self,index):
        self.n_pagos = self.ui.spinBox_numero_pagos.value()

        self.clearLayout(self.ui.verticalLayout_numero_pagos)
        self.label_pagos = list()
        
        for i in range(self.n_pagos):
            label = QtGui.QLabel("Pago " + str(i + 1) + ": ")
            label_pagos = QtGui.QLabel()
            self.label_pagos.append(label_pagos)
            horizontalLayout = QtGui.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(label_pagos)
            self.ui.verticalLayout_numero_pagos.addLayout(horizontalLayout)

        self.reload_data_table()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def tabla_cell_changed(self, currentRow, currentColumn, previousRow, previousColumn):
        item = self.ui.tableWidget_resumen.item(currentRow,0)
        try:
            self.id = item.text()
        except:
            pass

    def load_data_table(self):
        self.ui.tableWidget_resumen.sortItems(0, QtCore.Qt.AscendingOrder)
        self.ui.tableWidget_resumen.setColumnCount(5)
        self.ui.tableWidget_resumen.setHorizontalHeaderLabels(self.__header_table__)

        productos = controller.getProductosPedido(self.id_pedido)
        self.cantidad_productos = len(productos)
        self.ui.tableWidget_resumen.setRowCount(self.cantidad_productos)

        __type_pay__ = list()

        for pago in range(1,self.n_pagos+1):
            __type_pay__.append("Pago "+str(pago))

        self.list_combobox = list()
        self.list_precio = list()

        for i, data in enumerate(productos):
            model = QtGui.QStandardItemModel()
            for text in __type_pay__:
                text_item = QtGui.QStandardItem(text)
                text_item.setSizeHint(QtCore.QSize(100, 50))
                text_item.setTextAlignment(QtCore.Qt.AlignHCenter)
                text_item.setTextAlignment(QtCore.Qt.AlignVCenter)
                model.appendRow(text_item)
            view = QtGui.QTreeView()
            view.header().hide()
            view.setRootIsDecorated(False)
            combobox = QtGui.QComboBox()
            combobox.setView(view)
            combobox.setModel(model)
            combobox.currentIndexChanged.connect(self.combobox_changed)

            self.list_precio.append(int(str(data.precio_venta).split(".")[0]))
            self.list_combobox.append(combobox)
            row = [QtGui.QTableWidgetItem(str(data.id_producto)),
                   QtGui.QTableWidgetItem(controller.getProductoId(data.id_producto)[0].codigo),
                   QtGui.QTableWidgetItem(controller.getProductoId(data.id_producto)[0].nombre),
                   QtGui.QTableWidgetItem(controller_admin_producto.monetaryFormat(str(data.precio_venta).split(".")[0])),
                   combobox]
            for j, cell in enumerate(row):
                if(j == 4):
                    self.ui.tableWidget_resumen.setCellWidget(i,j,cell)
                else:
                    self.ui.tableWidget_resumen.setItem(i,j,cell)

        self.ui.tableWidget_resumen.sortItems(0, QtCore.Qt.DescendingOrder)
        self.ui.tableWidget_resumen.setColumnHidden(0, True)
        self.ui.tableWidget_resumen.resizeColumnsToContents()
        self.ui.tableWidget_resumen.resizeColumnsToContents()
        self.ui.tableWidget_resumen.horizontalHeader().setResizeMode(
            2, self.ui.tableWidget_resumen.horizontalHeader().Stretch)

        self.combobox_changed(0)

    def reload_data_table(self):
        self.ui.tableWidget_resumen.setRowCount(0)
        self.load_data_table()

    def combobox_changed(self,index):
        lista = list()
        for i,combobox in enumerate(self.list_combobox,1):
            lista.append(combobox.currentIndex())

        lista_suma = list()
        for i in range(0,self.n_pagos):
            suma = 0
            for j in range(0,self.cantidad_productos):
                if(lista[j] == i):
                    suma = suma + self.list_precio[j]
            lista_suma.append(suma)

        for i,suma in enumerate(lista_suma):
            self.label_pagos[i].setText(str(suma))

    def action_pagar(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setStandardButtons(
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setWindowTitle(u"Advertencia")
        msgBox.setText(
            u"Confirme para realizar venta")
        press = msgBox.exec_()
        if press == QtGui.QMessageBox.Ok:
            self.ventaForm.agregarVenta()
            for i, precio in enumerate(self.list_precio):
                if(i != 0):
                    total_pago = precio
                    efectivo = precio
                    tarjeta = 0
                    id_pedido = int(self.id_pedido)
                    propina = self.ui.lcdNumber_propina.value()
                    id_venta = controller.getVentaPedidoId(id_pedido)[
                        0].id_venta
                    controller.addDataPago(
                        total_pago, efectivo, tarjeta, propina, id_venta)
                    self.close()
            self.ventaForm.main.stackedWidget.widget(5).reload_data_table()
            self.ventaForm.id_pedido = controller.addDataPedido(self.ventaForm.mesa)
            self.ventaForm.reload_data_table2()
        else:
            return False