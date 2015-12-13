#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from mesas_venta import Ui_MesasVenta
from ventas.view_formulario_venta import FormularioVenta
import ventas.controller_venta as controller_venta


class MesasVenta(QtGui.QWidget):
    editable = False
    identificador = 0 # 0: borrar mesas, 1: unir mesas, 2: separar mesas
    buttons_disabled = list()
    buttons_enabled = list()

    def __init__(self,main,num_mesas,rut):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MesasVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.main = main
        self.num_mesas = num_mesas
        self.rut = rut
        self.ui.pushButton_aceptar.setVisible(False)
        self.create_buttons()
        self.connect_signals()

    def connect_signals(self):
        self.ui.pushButton_agregar.clicked.connect(self.agregar_mesa)
        self.ui.pushButton_borrar.clicked.connect(self.borrar_mesa)
        self.ui.pushButton_aceptar.clicked.connect(self.aceptar)
        self.ui.pushButton_unir.clicked.connect(self.action_button_unir_mesas)
        self.ui.pushButton_habilitar.clicked.connect(self.action_button_habilitar_mesas)

    def action_button_unir_mesas(self):
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Seleccione las mesas que desea unir.")
        self.editable = True
        for button in self.list_mesas:
            button.setCheckable(True)
        self.identificador = 1

    def action_button_habilitar_mesas(self):
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Seleccione la/las mesa(s) que desea habilitar.")
        self.editable = True
        self.buttons_disabled = list()
        self.buttons_enabled = list()
        for button in self.list_mesas:
            button.setCheckable(True)
            if(not button.isEnabled()):
                self.buttons_disabled.append(button)
            button.setEnabled(True)
        self.identificador = 2

    def unir_mesas(self, buttons_mesas):
        texto = ""
        num_mesa = buttons_mesas[0].mesa # número de la mesa a la que se van a unir las demás
        buttons_mesas[0].unido = True # asignamos la mesa como "unido"

        pedidos_mesas = list()
        for i,button in enumerate(buttons_mesas):
            if (i == 0):
                texto = str(button.mesa)
            else:
                texto = texto + ", " + str(button.mesa)
        for i,button in enumerate(buttons_mesas):
            pedidos_mesas.append(self.main.ui.stackedWidget.widget(button.mesa+6).id_pedido) # guardamos en la lista "pedidos_mesas", el id_pedido de cada mesa.    
            if (i == 0):
                button.setText("Mesas: "+texto)
            else:
                buttons_mesas[0].unido_a.append(button)
                button.setEnabled(False)
        productos = list() 
        for i,pedido in enumerate(pedidos_mesas):
            if(i != 0):
                productos = productos + controller_venta.getProductosPedido(int(pedido))
        for producto in productos:
            controller_venta.addDataVentaProducto(
                pedidos_mesas[0], producto.id_producto, producto.precio_venta)

        self.main.ui.stackedWidget.widget(num_mesa+6).reload_data_table2()

    def aceptar(self):
        for button in self.list_mesas:
            self.main.ui.stackedWidget.widget(button.mesa+6).button = button

        if(self.identificador == 0): # borrar mesa
            for button in self.list_mesas:
                num_mesa = int(button.text()[-2:])
                if (button.isChecked() == True):
                    button.setEnabled(False)
                button.setCheckable(False)
        elif(self.identificador == 1): # unir mesas
            mesas_a_unir = list() # lista de botones a unir
            for button in self.list_mesas:
                num_mesa = int(button.text()[-2:])
                if (button.isChecked() == True):
                    mesas_a_unir.append(button)
                button.setCheckable(False)
            self.unir_mesas(mesas_a_unir)
        else: # habilitar mesa
            buttons_checked = list()
            for button in self.list_mesas:
                if(button.isChecked()):
                    buttons_checked.append(button)
                    id_pedido = controller_venta.addDataPedido(button.mesa)
                    self.main.ui.stackedWidget.widget(button.mesa+6).id_pedido = id_pedido
                    self.main.ui.stackedWidget.widget(button.mesa+6).reload_data_table2()
                    for button_all in self.list_mesas:
                        # print button,button_all.unido_a
                        if(button in button_all.unido_a):
                            button_all.setText("Mesa "+str(button_all.mesa))
                button.setCheckable(False)

            for button in self.buttons_disabled:
                button.setEnabled(False)
            for button in buttons_checked:
                button.setEnabled(True)
            for button in buttons_checked:
                self.main.stackedWidget_changed(button.mesa+6)
                self.main.stackedWidget_changed(6)
        self.editable = False
        self.ui.label_info.setText("")
        self.ui.pushButton_aceptar.setVisible(False)
        
        self.ui.pushButton_unir.setCheckable(False)
        self.ui.pushButton_unir.setChecked(False)
        self.ui.pushButton_unir.setFocus()
        self.ui.pushButton_habilitar.setCheckable(False)
        self.ui.pushButton_habilitar.setChecked(False)
        self.ui.pushButton_habilitar.setFocus()
        self.ui.pushButton_borrar.setCheckable(False)
        self.ui.pushButton_borrar.setChecked(False)
        self.ui.pushButton_borrar.setFocus()

    def agregar_mesa(self):
        num_mesa = len(self.list_mesas)+1
        
        pushButton_mesa = controller_venta.PushButtonMesa("Mesa "+str(num_mesa),False)
        pushButton_mesa.mesa = num_mesa
        pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
        pushButton_mesa.clicked.connect(self.button_pressed)
        
        self.list_mesas.append(pushButton_mesa)

        self.ui.gridLayout_mesas.addWidget(pushButton_mesa,self.row,self.column)
        self.main.ui.stackedWidget.addWidget(FormularioVenta(self.main.ui,self.rut,num_mesa))
        self.main.ui.stackedWidget.widget(pushButton_mesa.mesa+6).button = pushButton_mesa
        self.column = self.column + 1
        if(num_mesa % 7 == 0):
            self.column = 0
            self.row = self.row +1

    def borrar_mesa(self):
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Selecciona la/las mesa(s) que desea borrar.")
        self.editable = True
        for button in self.list_mesas:
            button.setCheckable(True)
        self.identificador = 0

    def create_buttons(self):
        self.list_mesas = list()
        self.row = 0
        self.column = 0
        for mesa in range(self.num_mesas+1):
            if (mesa != 0):
                pushButton_mesa = controller_venta.PushButtonMesa("Mesa "+str(mesa),False)
                pushButton_mesa.mesa = mesa

                self.list_mesas.append(pushButton_mesa)

                pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
                pushButton_mesa.clicked.connect(self.button_pressed)
                self.ui.gridLayout_mesas.addWidget(pushButton_mesa,self.row,self.column)
                self.column = self.column + 1
            if (mesa % 7 == 0):
                self.row = self.row + 1
                self.column = 0

    def update_buttons(self):
        self.row = 0
        self.column = 0
        lista = list()
        self.clearLayout(self.ui.gridLayout_mesas)
        for i,button in enumerate(self.list_mesas,1):
            mesa = button.mesa
            texto = button.text()
            pushButton_mesa = controller_venta.PushButtonMesa(texto,button.ocupado,button.habilitado)
            pushButton_mesa.mesa = mesa
            self.main.ui.stackedWidget.widget(pushButton_mesa.mesa+6).button = pushButton_mesa

            lista.append(pushButton_mesa)

            pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
            pushButton_mesa.clicked.connect(self.button_pressed)
            self.ui.gridLayout_mesas.addWidget(pushButton_mesa,self.row,self.column)

            self.column = self.column + 1
            if (i % 7 == 0):
                self.row = self.row + 1
                self.column = 0
        self.list_mesas = lista

    def button_pressed(self):
        button_mesa = self.sender()
        num_mesa = button_mesa.mesa
        if (self.editable):
            pass
        else:
            self.main.ui.stackedWidget.setCurrentIndex(num_mesa+6)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())