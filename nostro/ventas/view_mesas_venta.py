#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from mesas_venta import Ui_MesasVenta
from ventas.view_formulario_venta import FormularioVenta
import ventas.controller_venta as controller_venta
import admin_empresa.controller_empresa as controller_empresa


class MesasVenta(QtGui.QWidget):
    """
    Clase MesasVenta que muestra una interfaz gráfica de las mesas que existen
    en el local y realiza funciones para agregar, borrar, unir y separar mesas.
    """
    editable = False
    identificador = 0 # 0: borrar mesas, 1: unir mesas, 2: habilitar
    buttons_disabled = list()
    buttons_enabled = list()

    # Index del QStackedWidget donde se encuentra la primera mesa
    pos_primera_mesa = 8 

    # Restamos uno porque la primera mesa empieza desde 1 y no desde 0
    pos_primera_mesa = pos_primera_mesa - 1 

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
        """
        Método que conecta las funciones de la clase con los eventos
        que genere el usuario al interactuar con los QWidgets de la vista.
        """
        self.ui.pushButton_agregar.clicked.connect(self.agregar_mesa)
        self.ui.pushButton_borrar.clicked.connect(self.borrar_mesa)
        self.ui.pushButton_aceptar.clicked.connect(self.aceptar)
        self.ui.pushButton_unir.clicked.connect(self.action_button_unir_mesas)
        self.ui.pushButton_habilitar.clicked.connect(self.action_button_habilitar_mesas)

    def borrar_mesa(self):
        """
        Método que es llamado cuando el usuario presiona en el boton 'borrar'.
        Cambia a un estado en el cual se pueden seleccionar mesas al presionar.
        """
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Selecciona la/las mesa(s) que desea borrar.")
        self.editable = True
        for button in self.list_mesas:
            button.setCheckable(True)
        self.identificador = 0

    def action_button_unir_mesas(self):
        """
        Método que es llamado cuando el usuario presiona en el boton 'unir'.
        Cambia a un estado en el cual se pueden seleccionar mesas al presionar.
        """
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Seleccione las mesas que desea unir.")
        self.editable = True
        for button in self.list_mesas:
            button.setCheckable(True)
        self.identificador = 1

    def action_button_habilitar_mesas(self):
        """
        Método que es llamado cuando el usuario presiona en el boton 
        'habilitar'.
        Cambia a un estado en el cual se pueden seleccionar mesas al presionar.
        """
        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.ui.pushButton_aceptar.setVisible(True)
        self.ui.label_info.setText("Seleccione la/las mesa(s) que desea habilitar.")
        self.editable = True
        for button in self.list_mesas:
            button.setCheckable(True)
            button.setEnabled(True)
        self.identificador = 2

    def unir_mesas(self, buttons_mesas):
        """
        Método que recibe como atributo una lista de PushButtonMesa.
        Une los pedidos de cada una de las mesas a las que corresponden
        los botones de la lista y los muestra en la mesa a la que
        esta asignada el PRIMER boton de la lista.
        """
        texto = ""
        num_mesa = buttons_mesas[0].mesa # número de la mesa a la que se van a unir las demás
        buttons_mesas[0].unido = True # asignamos la mesa como "unido"
        try:
            id_pedido = self.main.ui.stackedWidget.widget(
                buttons_mesas[0].mesa+self.pos_primera_mesa).id_pedido
        except:
            form_venta = self.main.ui.stackedWidget.widget(
                buttons_mesas[0].mesa+self.pos_primera_mesa)
            form_venta.id_pedido = controller_venta.addDataPedido(
                form_venta.mesa)
            form_venta.crear_pedido = False

        pedidos_mesas = list()
        for i,button in enumerate(buttons_mesas):
            if (i == 0):
                texto = str(button.mesa)
            else:
                texto = texto + ", " + str(button.mesa)
        for i,button in enumerate(buttons_mesas):
            if (i == 0):
                pedidos_mesas.append(self.main.ui.stackedWidget.widget(
                    button.mesa+self.pos_primera_mesa).id_pedido)
                button.setText("Mesas: "+texto)
                button.ocupado = True
            else:
                if(button.ocupado):
                    pedidos_mesas.append(self.main.ui.stackedWidget.widget(
                        button.mesa+self.pos_primera_mesa).id_pedido) 
                    if(i > 0):
                        controller_venta.finalizarPedido(
                            self.main.ui.stackedWidget.widget(
                                button.mesa+self.pos_primera_mesa).id_pedido)
                        self.main.ui.stackedWidget.widget(
                            button.mesa+
                            self.pos_primera_mesa).crear_pedido = True
                        button.ocupado = False
                        self.main.ui.stackedWidget.widget(
                            button.mesa+self.pos_primera_mesa).vaciar_table2()
                else:
                    pedidos_mesas.append("NULL")
                buttons_mesas[0].unido_a.append(button)
                button.habilitado = False
        productos = list() 
        for i,pedido in enumerate(pedidos_mesas):
            if(i != 0):
                productos = (productos + 
                    controller_venta.getProductosPedido(pedido))
                controller_venta.deletePedido(pedido)
        for producto in productos:
            try:
                controller_venta.addDataVentaProducto(
                    pedidos_mesas[0], producto.id_producto, producto.precio_venta)
            except:
                pass
        if(len(productos)>0):
            self.main.ui.stackedWidget.widget(
                num_mesa+self.pos_primera_mesa).reload_data_table2()
        else:
            controller_venta.finalizarPedido(
                self.main.ui.stackedWidget.widget(
                    num_mesa+self.pos_primera_mesa).id_pedido)
            controller_venta.deletePedido(
                self.main.ui.stackedWidget.widget(
                    num_mesa+self.pos_primera_mesa).id_pedido)
            self.main.ui.stackedWidget.widget(
                num_mesa+self.pos_primera_mesa).crear_pedido = True
            self.main.ui.stackedWidget.widget(
                num_mesa+self.pos_primera_mesa).button.ocupado = False
            self.main.ui.stackedWidget.widget(
                num_mesa+self.pos_primera_mesa).vaciar_table2()

    def aceptar(self):
        """
        Método llamado cuando el usuario acepta la selección de mesas a:
            - Borrar: self.identificador = 0
            - Unir: self.identificador = 1
            - Habilitar: self.identificador = 2
        Realiza las tareas pertinentes en cada uno de los 3 casos y 
        luego vuelve al estado normal: button.setCheckable(False)
        """
        for button in self.list_mesas:
            self.main.ui.stackedWidget.widget(button.mesa+
                self.pos_primera_mesa).button = button

        if(self.identificador == 0): # borrar mesa
            for button in self.list_mesas:
                if (button.isChecked()):
                    button.habilitado = False
                button.setCheckable(False)
        elif(self.identificador == 1): # unir mesas
            mesas_a_unir = list() # lista de botones a unir
            for button in self.list_mesas:
                if (button.isChecked() == True):
                    mesas_a_unir.append(button)
                button.setCheckable(False)
            if(len(mesas_a_unir)!=0):
                self.unir_mesas(mesas_a_unir)
        else: # habilitar mesa
            for button in self.list_mesas:
                if(button.isChecked()):
                    button.habilitado = True
                button.setCheckable(False)

        self.update_buttons()

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
        """
        Método que agrega una mesa adicional al local.
        Crea una nueva instancia de PushButtonMesa y lo asocia a una nueva
        instancia de FormularioVenta.
        """
        num_mesa = controller_empresa.getEmpresa(1)[0].num_mesas+1

        controller_empresa.editNumMesasEmpresa(num_mesa)
        
        pushButton_mesa = controller_venta.PushButtonMesa(
            "Mesa "+str(num_mesa),False)
        pushButton_mesa.mesa = num_mesa
        pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
        pushButton_mesa.clicked.connect(self.button_pressed)
        
        self.list_mesas.append(pushButton_mesa)

        self.ui.gridLayout_mesas.addWidget(
            pushButton_mesa,self.row,self.column)
        self.main.ui.stackedWidget.addWidget(
            FormularioVenta(self.main.ui,self.rut,num_mesa))
        self.main.ui.stackedWidget.widget(
            pushButton_mesa.mesa+
            self.pos_primera_mesa).button = pushButton_mesa
        self.column = self.column + 1
        if(num_mesa % 7 == 0):
            self.column = 0
            self.row = self.row +1

    def create_buttons(self):
        """
        Método que crea una instancia de PushButtonMesa por cada mesa que 
        este registrada en el local 'self.num_mesas' y la muestra en la vista.
        """
        self.list_mesas = list()
        self.row = 0
        self.column = 0
        for mesa in range(self.num_mesas+1):
            if (mesa != 0):
                pushButton_mesa = controller_venta.PushButtonMesa(
                    "Mesa "+str(mesa),False)
                pushButton_mesa.mesa = mesa

                self.list_mesas.append(pushButton_mesa)

                pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
                pushButton_mesa.clicked.connect(self.button_pressed)
                self.ui.gridLayout_mesas.addWidget(
                    pushButton_mesa,self.row,self.column)
                self.column = self.column + 1
            if (mesa % 7 == 0):
                self.row = self.row + 1
                self.column = 0

    def update_buttons(self):
        """
        Limpia el layout donde se muestran las mesas y crea nuevas instancias
        de PushButtonMesa por cada mesa del local manteniendo las
        configuraciones de cada una.
        """
        self.row = 0
        self.column = 0
        lista = list()
        self.clearLayout(self.ui.gridLayout_mesas)
        for i,button in enumerate(self.list_mesas,1):
            mesa = button.mesa
            texto = button.text()
            pushButton_mesa = controller_venta.PushButtonMesa(
                texto,button.ocupado,button.habilitado)
            pushButton_mesa.mesa = mesa
            self.main.ui.stackedWidget.widget(pushButton_mesa.mesa+
                self.pos_primera_mesa).button = pushButton_mesa

            lista.append(pushButton_mesa)

            pushButton_mesa.setMinimumSize(QtCore.QSize(120, 60))
            pushButton_mesa.clicked.connect(self.button_pressed)
            self.ui.gridLayout_mesas.addWidget(pushButton_mesa,
                self.row,
                self.column)

            self.column = self.column + 1
            if (i % 7 == 0):
                self.row = self.row + 1
                self.column = 0
        self.list_mesas = lista

    def button_pressed(self):
        """
        Método que es llamado cuando el usuario presiona en algun 
        PushButtonMesa, cambia el indice del QStackedWidget de la ventana 
        principal al FormularioVenta que corresponde el boton presionado.
        """
        button_mesa = self.sender()
        num_mesa = button_mesa.mesa
        if (self.editable):
            pass
        else:
            self.main.ui.stackedWidget.setCurrentIndex(num_mesa+
                self.pos_primera_mesa)

    def clearLayout(self, layout):
        """
        Método generico para borrar todos los widgets de un layout.
        """
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())