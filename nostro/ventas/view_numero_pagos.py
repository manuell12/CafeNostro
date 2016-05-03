#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from numero_pagos import Ui_NumeroPagos
import ventas.controller_venta as controller
import admin_productos.controller_admin_producto as controller_admin_producto
import os,time

class NumeroPagos(QtGui.QDialog):

    __header_table__ = (u"ID",
                        u"Código",
                        u"Nombre",
                        u"Precio bruto",
                        u"Pago",
                        u"¿Pagar?")

    def __init__(self, pedido, ventaForm):
        'Constructor de la clase'
        super(NumeroPagos, self).__init__()
        self.ui = Ui_NumeroPagos()
        self.ui.setupUi(self)
        self.id_pedido = pedido
        self.ventaForm = ventaForm
        self.show()
        self.ui.spinBox_numero_pagos.setRange(1,20)
        self.n_pagos = self.ui.spinBox_numero_pagos.value()
        self.ui.tableWidget_resumen.setColumnCount(6)

        self.ui.tableWidget_resumen.cellPressed.connect(
            self.tabla_cell_pressed)
        self.ui.spinBox_numero_pagos.valueChanged.connect(
            self.spinBox_numero_pagos_changed)
        self.ui.pushButton_pagar.clicked.connect(self.action_pagar)

        self.crear_pagos()

        self.load_data_table()

    def crear_pagos(self):
        """
        Método que crea la parte gráfica alojada en 'verticalLayout_numero_pagos'.
        Agrega 9 QLabel, 1 QLineEdit y un QComboBox por cada pago que se 
        vaya a realizar y los almacena en variables globales (listas).
        """
        __type_pay__ = ((u"EFECTIVO"),
                        (u"TARJETA"))

        self.label_pagos = list()
        self.label_pagos_propina = list()
        self.combobox_tipo_pagos = list()

        for i in range(self.n_pagos):

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

            label = QtGui.QLabel("Pago " + str(i + 1) + ": ")
            label_sep = QtGui.QLabel("    ")
            label_aux_1 = QtGui.QLabel("Subtotal:")
            label_aux_1a = QtGui.QLabel("$")
            lineEdit_pagos = QtGui.QLineEdit()
            label_sep1 = QtGui.QLabel("    ")
            label_aux_2 = QtGui.QLabel("Propina:")
            label_aux_2a = QtGui.QLabel("$")
            label_pagos_propina = QtGui.QLabel()
            label_sep2 = QtGui.QLabel("    ")

            self.label_pagos.append(lineEdit_pagos)
            self.label_pagos_propina.append(label_pagos_propina)
            self.combobox_tipo_pagos.append(combobox)

            horizontalLayout = QtGui.QHBoxLayout()
            horizontalLayout.addWidget(label)
            horizontalLayout.addWidget(label_sep)
            horizontalLayout.addWidget(label_aux_1)
            horizontalLayout.addWidget(label_aux_1a)
            horizontalLayout.addWidget(lineEdit_pagos)
            horizontalLayout.addWidget(label_sep1)
            horizontalLayout.addWidget(label_aux_2)
            horizontalLayout.addWidget(label_aux_2a)
            horizontalLayout.addWidget(label_pagos_propina)
            horizontalLayout.addWidget(label_sep2)
            horizontalLayout.addWidget(combobox)

            self.ui.verticalLayout_numero_pagos.addLayout(horizontalLayout)

    def spinBox_numero_pagos_changed(self,index):
        """
        Método llamado cuando el usuario modifica el numero de pagos que va 
        a realizar.
        Se actualiza la variable global que mantiene el número de pagos y
        la vista.
        """
        self.n_pagos = self.ui.spinBox_numero_pagos.value()

        self.clearLayout(self.ui.verticalLayout_numero_pagos)
        self.crear_pagos()
        self.reload_data_table()

    def clearLayout(self, layout):
        """
        Método genérico que elimina todos los QWidgets almacenados en un 
        layout.
        """
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def tabla_cell_pressed(self,row,column):
        """
        Método llamado cuando el usuario presiona en la tabla.
        Si el usuario presiona en la columna 5 (columna '¿Pagar?'),
        se cambia el estado del producto en el cual presionó.
        """
        print "row:",row,"column:",column
        if(column == 5):
            estado = self.ui.tableWidget_resumen.cellWidget(row,5).estado
            if(estado == 0):
                self.ui.tableWidget_resumen.cellWidget(row,5).estado = 1
            if(estado == 1):
                self.ui.tableWidget_resumen.cellWidget(row,5).estado = 0
                self.list_combobox[row].setCurrentIndex(0)
            self.reload_data_table()

    def load_data_table(self,re=False):
        """
        Método que obtiene los productos actuales del pedido de forma repetida,
        es decir, se obtiene cada producto (objeto) n veces repetido, donde n
        es la cantidad de veces que se compró y los carga en la tabla.
        Si 're' es True, realiza funciones para actualizar la tabla y mantener
        los valores modificados por el usuario.
        """
        __check_icons__ = [(QtGui.QPixmap(
                            os.getcwd() + "/admin_productos/icons/red_check.png")),
                           (QtGui.QPixmap(
                            os.getcwd() + "/admin_productos/icons/green_check.png"))]
        self.productos = controller.getProductosPedidoRepetidosPorCantidad(
            self.id_pedido)
        self.cantidad_productos = len(self.productos)
        if(not re):
            self.ui.tableWidget_resumen.setHorizontalHeaderLabels(
                self.__header_table__)
            self.ui.tableWidget_resumen.setRowCount(
                self.cantidad_productos)

        __type_pay__ = ["NINGUNO"]

        for pago in range(1,self.n_pagos+1):
            __type_pay__.append("Pago "+str(pago))

        self.list_combobox = list()
        self.list_precio = list()

        for i, data in enumerate(self.productos):
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
            estado = 1
            if(re):
                index = self.ui.tableWidget_resumen.cellWidget(
                    i,4).currentIndex()
                combobox.setCurrentIndex(index)
                estado = self.ui.tableWidget_resumen.cellWidget(
                    i,5).estado
            else:
                combobox.setCurrentIndex(1)
            combobox.currentIndexChanged.connect(self.combobox_changed)

            label_pixmap = controller.LabelPago(__check_icons__,estado)

            self.list_precio.append(int(str(data.precio_venta).split(".")[0]))
            self.list_combobox.append(combobox)
            row = [QtGui.QTableWidgetItem(str(data.id_producto)),
                   QtGui.QTableWidgetItem(
                    controller.getProductoId(data.id_producto)[0].codigo),
                   QtGui.QTableWidgetItem(
                    controller.getProductoId(data.id_producto)[0].nombre),
                   QtGui.QTableWidgetItem(
                    controller_admin_producto.monetaryFormat(
                        str(data.precio_venta).split(".")[0])),
                   combobox,
                   label_pixmap]
            for j, cell in enumerate(row):
                if(j == 4 or j == 5):
                    self.ui.tableWidget_resumen.setCellWidget(i,j,cell)
                else:
                    self.ui.tableWidget_resumen.setItem(i,j,cell)

        self.ui.tableWidget_resumen.setColumnHidden(0, True)
        self.ui.tableWidget_resumen.resizeColumnsToContents()
        self.ui.tableWidget_resumen.horizontalHeader().setResizeMode(
            2, self.ui.tableWidget_resumen.horizontalHeader().Stretch)

        self.combobox_changed(0)

    def reload_data_table(self):
        """
        Método que actualiza la vista de la tabla tableWidget_resumen.
        """
        self.load_data_table(True)

    def combobox_changed(self,index):
        """
        Método que es llamado cuando el usuario modifica al menos un combobox
        de la tabla tableWidget_resumen.
        Calcula la cantidad total y la propina corresponiente a cada pago que
        se haya definido.
        """
        lista = list()
        subtotal = 0
        for i,combobox in enumerate(self.list_combobox,1):
            lista.append(combobox.currentIndex()-1)

            if(combobox.currentIndex() == 0 and self.ui.tableWidget_resumen.cellWidget(i-1,5).estado == 1):
                self.ui.tableWidget_resumen.cellWidget(i-1,5).estado = 0
                self.reload_data_table()

            if(combobox.currentIndex() != 0 and self.ui.tableWidget_resumen.cellWidget(i-1,5).estado == 0):
                self.ui.tableWidget_resumen.cellWidget(i-1,5).estado = 1
                self.reload_data_table() 

        lista_suma = list()
        for i in range(0,self.n_pagos):
            suma = 0
            for j in range(0,self.cantidad_productos):
                if(lista[j] == i):
                    suma = suma + self.list_precio[j]
            lista_suma.append(suma)

        for i,suma in enumerate(lista_suma):
            subtotal = subtotal + suma
            self.label_pagos[i].setText(str(suma))
            self.label_pagos_propina[i].setText(str(suma*0.1))

        self.ui.lcdNumber_subtotal.display(subtotal)
        self.ventaForm.subtotal = subtotal
        self.ventaForm.propina = subtotal * 0.1
        self.ventaForm.total = subtotal * 1.1

    def action_pagar(self):
        """
        Método que es llamado cuando el usuario presiona en el 
        boton 'Pagar/Cerrar Venta'.

        Cierra la mesa en caso de que se hayan pagado todos los productos.
        En caso contrario, elimina del pedido los productos que se hayan 
        pagado, los agrega a una venta y a un pedido nuevos y 
        vuelve al formulario de venta con los productos que no se pagaron.
        """
        lista_estados = list()
        total_productos_pagados = True
        for i in range(len(self.list_combobox)):
            if(self.ui.tableWidget_resumen.cellWidget(i,5).estado == 0):
                total_productos_pagados = False
            lista_estados.append(self.ui.tableWidget_resumen.cellWidget(i,5).estado)

        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setStandardButtons(
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setWindowTitle(u"Advertencia")
        msgBox.setText(
            u"Confirme para realizar venta")
        press = msgBox.exec_()
        if press == QtGui.QMessageBox.Ok:
            if(total_productos_pagados):
                pass
            else:

                num_documento_old = self.ventaForm.num_documento
                id_pedido_new = controller.addDataPedido(self.ventaForm.mesa)
                for row,estado in enumerate(lista_estados):
                    if(estado == 1):
                        controller.cambiarCantidadProducto(
                            self.id_pedido, 
                            self.productos[row].id_producto,
                            "disminuir")
                        controller.addDataVentaProducto(
                            id_pedido_new, 
                            self.productos[row].id_producto, 
                            self.productos[row].precio_venta)
                self.ventaForm.id_pedido = id_pedido_new
                id_pedido_old = self.id_pedido
                self.id_pedido = id_pedido_new

            self.ventaForm.agregarVenta()

            for i, line_precio in enumerate(self.label_pagos):
                total_pago = int(line_precio.text())
                if(self.combobox_tipo_pagos[i].currentIndex() == 0): 
                    efectivo = int(line_precio.text())
                    tarjeta = 0
                else:
                    efectivo = 0
                    tarjeta = int(line_precio.text())
                id_pedido = int(self.id_pedido)
                propina = int(line_precio.text())*0.1
                id_venta = controller.getVentaPedidoId(id_pedido)[
                    0].id_venta
                controller.addDataPago(
                    total_pago, efectivo, tarjeta, propina, id_venta)
                self.close()
            self.ventaForm.main.stackedWidget.widget(5).reload_data_table()

            if(total_productos_pagados):
                controller.finalizarPedido(self.id_pedido)
                self.ventaForm.crear_pedido = True
                self.ventaForm.crear_venta = True
                self.ventaForm.vaciar_table2()
            else:
                controller.finalizarPedido(id_pedido_new)

                self.ventaForm.num_documento = num_documento_old
                self.ventaForm.id_pedido = id_pedido_old
                
                self.ventaForm.reload_data_table2()
        else:
            return False