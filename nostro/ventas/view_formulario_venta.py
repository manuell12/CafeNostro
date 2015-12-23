#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from formulario_venta import Ui_FormularioVenta
import sys
import os
import controller_venta as controller
import admin_productos.controller_admin_producto as controller_admin_producto
import admin_usuarios.controller_admin_user as controller_admin_user
import admin_empresa.controller_empresa as controller_empresa
from ventas.view_admin_venta import AdminVentas
from ventas.view_numero_pagos import NumeroPagos
import datetime
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

import _winreg as winreg  
import subprocess

class FormularioVenta(QtGui.QWidget):
    """
    Clase FormularioVenta encargada tanto de mostrar en pantalla la información
    correspondiente a un pedido actual, como de realizar funciones de
    crear pedido, crear venta, crear pagos, editar venta, ofrecer mas opciones
    de pago e imprimir detalle.
    """

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
    crear_pedido = True
    crear_venta = True
    crear_documento = True

    def __init__(self, main, rut_usuario, mesa):
        """
        Constructor de la clase FormularioVenta.
        Asigna los atributos de la clase: main,rut_usuario,mesa
        Asigna un boton de la vista por mesas al formulario en caso de que no
        sea compra directa.
        En caso de ser compra directa, oculta la informacion referente a propina.
        """
        QtGui.QWidget.__init__(self)
        self.ui = Ui_FormularioVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.connect_actions()
        self.main = main
        self.mesa = mesa
        self.rut_usuario = rut_usuario
        
        if int(self.mesa) != 0: #asignar un boton a la mesa
            self.button = self.main.stackedWidget.widget(6).list_mesas[int(mesa)-1] 
        else:
            self.ui.lcdNumber_propina.setVisible(False)
            self.ui.lcdNumber_total.setVisible(False)
            self.ui.label.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_price_2.setVisible(False)
            self.ui.label_price_3.setVisible(False)

        pedido = controller.getPedidoActivoPorMesa(self.mesa)

        try:
            self.id_pedido = pedido[0].id_pedido
            self.crear_pedido = False
            self.reload_data_table2()
        except:
            pass

        self.load_model_total_productos(controller.getProductoStatus(1))
        self.set_combobox_tipo_pago()

    def set_combobox_tipo_pago(self):
        """
        Inicializa el QComboBox de la vista que muestra los tipos de pago
        (efectivo y tarjeta).
        """
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
        """
        Método que conecta las funciones de la clase con los eventos
        que genere el usuario al interactuar con los QWidgets de la vista.
        """
        self.ui.pushButton_agregar.clicked.connect(
            self.action_agregar)
        self.ui.pushButton_eliminar.clicked.connect(
            self.action_eliminar)
        self.ui.pushButton_opciones.clicked.connect(
            self.action_opciones)
        self.ui.pushButton_imprimir_comandas.clicked.connect(
            self.action_imprimir)

        self.ui.pushButton_aumentar_cantidad.clicked.connect(
            self.action_aumentar)
        self.ui.pushButton_disminuir_cantidad.clicked.connect(
            self.action_disminuir)

        self.ui.pushButton_filtrar_bebidas_calientes.clicked.connect(
            self.action_bebidas_calientes)
        self.ui.pushButton_filtrar_cocina.clicked.connect(
            self.action_cocina)
        self.ui.pushButton_filtrar_bebidas_frias.clicked.connect(
            self.action_bebidas_frias)
        self.ui.pushButton_filtrar_helados.clicked.connect(
            self.action_helados)
        self.ui.pushButton_filtrar_reposteria.clicked.connect(
            self.action_reposteria)
        self.ui.pushButton_filtrar_otros.clicked.connect(
            self.action_otros)

        self.ui.pushButton_cerrar_venta.clicked.connect(
            self.action_cerrar_venta)
        self.ui.lineEdit_buscar_codigo.textChanged.connect(
            self.lineEdit_buscar_codigo_changed)

    def set_ocupado(self, ocupado):
        """
        Método que recibe como parámetro un booleano.
        Asigna la mesa como ocupada (roja) si 'ocupado' == True.
        Asigna la mesa como libre (verde) si 'ocupado' == False.
        Actualiza la vista por mesas.
        """
        self.button.ocupado = ocupado
        self.main.stackedWidget.widget(6).update_buttons()

    def action_agregar(self):
        """
        Método llamado cuando el usuario presiona en el boton 'agregar'
        ubicado entre las tablas.
        Crea un pedido para la mesa actual (compra directa es mesa 0), en caso
        de que sea la primera vez que se agrega un producto a la mesa.
        """
        if(self.crear_pedido):
            self.id_pedido = controller.addDataPedido(self.mesa)
            self.crear_pedido = False
        controller.addDataVentaProducto(
            self.id_pedido, self.id_tablaP, self.precio_tablaP)
        self.reload_data_table2()
        self.ui.tableView_total_productos.setFocus()

    def action_eliminar(self):
        """
        Método llamado cuando el usuario presiona en el boton 'eliminar'
        ubicado a la derecha de la tabla de pedidos.
        """
        controller.deleteProducto(self.id_pedido, self.id_tablaPd)
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()

    def action_aumentar(self):
        """
        Método llamado cuando el usuario presiona en el boton '+'
        ubicado a la derecha de la tabla de pedidos.
        """
        controller.cambiarCantidadProducto(
            self.id_pedido, self.id_tablaPd, "aumentar")
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()

    def action_disminuir(self):
        """
        Método llamado cuando el usuario presiona en el boton '-'
        ubicado a la derecha de la tabla de pedidos.
        """
        controller.cambiarCantidadProducto(
            self.id_pedido, self.id_tablaPd, "disminuir")
        self.reload_data_table2()
        self.ui.tableView_pedido.selectRow(self.row_tablaPd)
        self.ui.tableView_pedido.setFocus()


    def action_cocina(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'cocina'
        """
        productos = controller.getProductoCategoria(1)
        self.load_model_total_productos(productos)

    def action_helados(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'helados'
        """
        productos = controller.getProductoCategoria(2)
        self.load_model_total_productos(productos)

    def action_bebidas_calientes(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'bebidas calientes'
        """
        productos = controller.getProductoCategoria(3)
        self.load_model_total_productos(productos)

    def action_bebidas_frias(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'bebidas frias'
        """
        productos = controller.getProductoCategoria(4)
        self.load_model_total_productos(productos)

    def action_reposteria(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'reposteria'
        """
        productos = controller.getProductoCategoria(5)
        self.load_model_total_productos(productos)

    def action_otros(self):
        """
        Método llamado cuando el usuario presiona en el boton de filtro
        'otros'
        """
        productos = controller.getProductoCategoria(6)
        self.load_model_total_productos(productos)

    def lineEdit_buscar_codigo_changed(self, text):
        """
        Método llamado cuando el usuario ingresa texto en el QLineEdit
        para buscar por código.
        """
        productos = controller.getProductoCodigo(text)
        self.load_model_total_productos(productos)


    def cell_selected_table1(self, index, indexp):
        """
        Método llamado cuando el usuario CAMBIA la seleccion de una fila 
        de la tabla de total productos (table1).
        Obtiene el id, el nombre y el precio del producto seleccionado.
        """
        model = self.ui.tableView_total_productos.model().sourceModel()
        self.id_tablaP = int(model.item(index.row(), 0).text())
        self.nombre_tablaP = model.item(index.row(), 2).text()
        self.precio_tablaP = model.item(index.row(), 3).text()
        precio = self.precio_tablaP.split(".")
        self.precio_tablaP = ""
        for i in range(len(precio)):
            self.precio_tablaP = self.precio_tablaP + precio[i]

    def load_model_total_productos(self, data=""):
        """
        Carga los datos entregados como parámetro 'data' en la tabla en
        una instancia de TotalProductosModel().
        Carga los Header de la tabla con el atributo de clase __header_table__.
        """
        model = controller.TotalProductosModel()
        self.ui.tableView_total_productos.setModel(model)
        model.load_data(data, self.__header_table__)

        self.set_columns_total_productos()

    def set_columns_total_productos(self):
        """
        Configura los anchos de las columnas de la tabla de total de productos.
        Realiza un ordenamiento ascendente de la columna 0 (id producto)
        Oculta la columna 0 de la vista.
        Conecta el SelectionModel de la tabla con la función 'cell_selected_table1'
        """
        self.ui.tableView_total_productos.horizontalHeader().setResizeMode(
            2, self.ui.tableView_total_productos.horizontalHeader().Stretch)

        for col, h in enumerate(self.__header_table__):
            self.ui.tableView_total_productos.setColumnWidth(col, h[1])

        self.ui.tableView_total_productos.sortByColumn(
            0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_total_productos.setColumnHidden(0, True)

        modelSel = self.ui.tableView_total_productos.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table1)


    def load_productos_table2(self, pedido=None):
        """
        Carga la información de la base de datos en la tabla de pedidos.
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
            row = [data.id_producto, 
                   controller.getProductoId(data.id_producto)[0].codigo,
                   controller.getProductoId(data.id_producto)[0].nombre,
                   data.cantidad,
                   controller_admin_producto.monetaryFormat(str(
                    data.precio_venta).split(".")[0])]

            subtotal = subtotal + (long(data.precio_venta) * data.cantidad)

            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                if j is 5:
                    model.setData(index, self.__type_productos__[field])
                else:
                    model.setData(index, field)

        self.subtotal = subtotal
        self.propina = subtotal * 0.1
        self.total = subtotal * 1.1

        self.ui.lcdNumber_subtotal.display(self.subtotal)
        self.ui.lcdNumber_propina.display(self.propina)
        self.ui.lcdNumber_total.display(self.total)

        modelSel = self.ui.tableView_pedido.selectionModel()
        modelSel.currentChanged.connect(self.cell_selected_table2)

        if pedido is None:
            return model
        else:
            self.set_source_model_table2(model)

    def reload_data_table2(self):
        """
        Actualiza la tabla de pedidos.
        """
        self.set_model_table2()
        self.set_source_model_table2(
            self.load_productos_table2())

    def cell_selected_table2(self, index, indexp):
        """
        Método llamado cuando el usuario CAMBIA la seleccion de una fila 
        de la tabla de pedidos (table2).
        Obtiene el id y el precio del producto seleccionado.
        """
        model = self.ui.tableView_pedido.model()
        index = self.ui.tableView_pedido.currentIndex()
        self.row_tablaPd = index.row()
        self.id_tablaPd = model.index(
            index.row(), 0, QtCore.QModelIndex()).data()
        self.precio_tablaPd = model.index(
            index.row(), 4, QtCore.QModelIndex()).data()
        # self.ui.lcdNumber_subtotal.display(self.id)

    def set_model_table2(self):
        """
        Define el módelo de la grilla para trabajar.
        """
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.ui.tableView_pedido.setModel(self.proxyModel)

    def set_source_model_table2(self, model):
        """
        Actualiza constantemente el origen de los datos para siempre tenerlos
        al día así pudiendo buscar y mostrar solo algunos datos.
        asigna el tamaño de las columnas a las grillas respectivas.
        """
        self.proxyModel.setSourceModel(model)

        self.ui.tableView_pedido.horizontalHeader().setResizeMode(
            2, self.ui.tableView_pedido.horizontalHeader().Stretch)

        for col, h in enumerate(self.__header_table2__):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tableView_pedido.setColumnWidth(col, h[1])

        self.ui.tableView_pedido.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.tableView_pedido.setColumnHidden(0, True)

    def vaciar_table2(self):
        """
        Método que crea un QSortFilterProxyModel vacío y lo carga en la tabla
        de pedidos. (reinicia la vista)
        """
        empty_model = QtGui.QSortFilterProxyModel()
        self.ui.tableView_pedido.setModel(empty_model)
        self.ui.lcdNumber_propina.display(0)
        self.ui.lcdNumber_subtotal.display(0)
        self.ui.lcdNumber_total.display(0)


    def action_opciones(self):
        """
        Método que se llama cuando el usuario apreta en el boton 'mas opciones'.
        Crea una instancia de NumeroPagos().
        """
        self.pagos = NumeroPagos(self.id_pedido,self)
        self.pagos.show()

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


    def action_cerrar_venta(self):
        """
        Método que se llama cuando el usuario apreta en el boton "cerrar venta".
        Guarda los datos de la venta en la base de datos 
        (si no se ha guardado en 'action_imprimir').
        Guarda los datos de un pago para todos los productos del pedido.
        Reinicia los datos de la mesa para generar un pedido totalmente nuevo.
        """
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setStandardButtons(
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        msgBox.setWindowTitle(u"Advertencia")
        msgBox.setText(
            u"Confirme para realizar venta.")
        press = msgBox.exec_()
        if press == QtGui.QMessageBox.Ok:
            try:
                if self.edit is True:
                    self.editarVenta()                    
                else:
                    if(self.crear_venta):
                        self.agregarVenta()
                        self.crear_venta = False
                    else:
                        self.editarVenta()
                    self.agregarPago()
                    # self.main.stackedWidget.widget(5).reload_data_table()
                    self.crear_pedido = True
                    self.crear_venta = True
                    self.crear_documento = True
                self.main.stackedWidget.widget(5).reload_data_table()
                self.vaciar_table2()
            except:
                if(self.crear_venta):
                    self.agregarVenta()
                    self.crear_venta = False
                else:
                    self.editarVenta()
                self.agregarPago()
                self.main.stackedWidget.widget(5).reload_data_table()
                self.crear_pedido = True
                self.crear_venta = True
                self.crear_documento = True
                self.vaciar_table2()

            self.habilitarMesasUnidas()
                
        else:
            return False

    def agregarVenta(self):
        """
        Método que registra el pedido actual como una venta y la guarda
        en la base de datos.
        """
        y = int(time.strftime("%Y"))
        m = int(time.strftime("%m"))
        d = int(time.strftime("%d"))
        fecha = datetime.date(y, m, d)
        self.crear_o_asignar_num_documento()

        if int(self.mesa) == 0:
            tipo = "directa"
            total_pago = self.subtotal
        else:
            tipo = "pedido por mesa"
            total_pago = self.total

        id_pedido = int(self.id_pedido)
        id_usuario = int(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].id_usuario)
        controller.addDataVenta(fecha, self.num_documento,
                                tipo, total_pago, id_usuario, id_pedido)

    def habilitarMesasUnidas(self):
        """
        Método que habilita las mesas que se encontraban unidas
        a la mesa actual. 
        Si no hay mesas unidas no hace nada.
        """
        try:
            self.button.setText("Mesa "+str(self.button.mesa))
            for button in self.button.unido_a:
                self.main.stackedWidget.widget(button.mesa+7).button.habilitado = True
                self.main.stackedWidget.widget(button.mesa+7).button.setText(
                    "Mesa "+str(button.mesa))
        except:
            pass

    def editarVenta(self):
        """
        Edita la fecha, el total de pago y el usuario encargado de la venta
        para el pedido actual.
        """
        print("-----Editar Venta-----")
        y = int(time.strftime("%Y"))
        m = int(time.strftime("%m"))
        d = int(time.strftime("%d"))
        fecha = datetime.date(y, m, d)
        if int(self.mesa) == 0:
            total_pago = self.subtotal
        else:
            total_pago = self.total
        id_venta = controller.getIdVenta(int(self.id_pedido))
        id_usuario = int(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].id_usuario)

        controller.editDataVenta(id_venta, fecha, total_pago, id_usuario)

    def agregarPago(self):
        """
        Agrega en un pago todos los productos del pedido actual.
        """
        if int(self.mesa) == 0:
            total_pago = self.subtotal
        else:
            total_pago = self.total
        if(int(self.ui.comboBox_tipo_pago.currentIndex()) == 0):  # efectivo
            efectivo = total_pago
            tarjeta = 0
        else:
            tarjeta = total_pago
            efectivo = 0
        propina = self.propina
        id_pedido = int(self.id_pedido)
        id_venta = controller.getVentaPedidoId(id_pedido)[0].id_venta
        controller.addDataPago(total_pago, efectivo,
                               tarjeta, propina, id_venta)
        controller.finalizarPedido(id_pedido)


    def crear_o_asignar_num_documento(self):
        """
        Asigna un número de documento UNICO para un pedido.
        """
        if(self.crear_documento):
            try: # Obtiene el numero del último documento y le suma una unidad.
                self.num_documento = controller.getVentas()[-1].num_documento + 1
            except: # Si no hay ventas registradas, comienza con 0
                self.num_documento = 0
            self.crear_documento = False

    def action_imprimir(self):
        """
        Método que se ejecuta cuando el usuario apreta en el 
        boton "imprimir detalle".
        Genera un canvas con los datos de la venta y 
        lo exporta como PDF a la carpeta nostro/docs
        """
        # Se crea una venta sólo si no se ha creado anteriormente.
        if(self.crear_venta):
            self.agregarVenta()
            self.crear_venta = False

        # Obtener Datos.
        nombre_usuario = str(controller_admin_user.getUsuarioRut(
            self.rut_usuario)[0].nombre).upper()+" "+str(
            controller_admin_user.getUsuarioRut(
                self.rut_usuario)[0].apellido).upper()
        fecha_hora = time.strftime("Fecha: %d-%m-%Y       Hora: %H:%M:%S")
        productos = controller.getProductosPedido(self.id_pedido)
        num_productos = len(productos)
        espacio_productos = num_productos*15
        empresa = controller_empresa.getEmpresa(1)[0]

        c = canvas.Canvas("docs/detalle_mesa_"+str(self.mesa)+"_documento_"+
            controller_admin_producto.zerosAtLeft(self.num_documento,8)+".pdf")
        ancho = 300
        alto = 390+espacio_productos
        c.setPageSize((ancho, alto+50))
        c.drawImage("images/logo_nombre.jpg",40,alto-30,220,66)
        c.drawString(10,alto-50,empresa.nombre.decode('cp1252'))
        c.drawString(10,alto-65,empresa.direccion.decode('cp1252'))
        c.drawString(10,alto-80,"FONO: "+empresa.fono)
        c.drawString(10,alto-110,fecha_hora)
        c.drawString(10,alto-125,"CREADOR: "+nombre_usuario.decode('cp1252'))
        c.drawString(10,alto-140,"NUM. CUENTA: "+
            controller_admin_producto.zerosAtLeft(self.num_documento,8))
        c.drawString(10,alto-155,
            "---------------------------------------------------------")
        if(int(self.mesa) == 0):
            c.drawString(10,alto-170,"COMPRA DIRECTA")
        else:
            c.drawString(10,alto-170,"MESA: "+str(self.mesa))
        c.drawString(10,alto-185,"CUENTA: "
            +controller_admin_producto.zerosAtLeft(self.num_documento,8))
        c.drawString(10,alto-200,
            "---------------------------------------------------------")
        alto_productos = alto-215
        for i,producto in enumerate(productos):
            c.drawString(10,alto_productos-15*i,str(producto.cantidad))
            c.drawString(30,alto_productos-15*i,str(
                controller.getProductoId(
                    producto.id_producto)[0].nombre).decode('cp1252'))
            c.drawString(230,alto_productos-15*i,"$")
            c.drawRightString(280,alto_productos-15*i,str(
                controller_admin_producto.monetaryFormat(
                    int(producto.precio_venta*producto.cantidad))))
            fin_alto_productos = alto_productos-15*i
        try:
            fin_alto_productos
        except:
            fin_alto_productos = alto_productos
        c.drawString(10,fin_alto_productos-15,
            "---------------------------------------------------------")
        fin_alto_productos = fin_alto_productos - 30

        c.drawString(120,fin_alto_productos-15,"CONSUMO: ")
        c.drawString(200,fin_alto_productos-15,"$")
        c.drawRightString(250,fin_alto_productos-15,str(
            controller_admin_producto.monetaryFormat(int(self.subtotal))))
        c.drawString(120,fin_alto_productos-30,"TOTAL: ")
        c.drawString(200,fin_alto_productos-30,"$")
        c.drawRightString(250,fin_alto_productos-30,str(
            controller_admin_producto.monetaryFormat(int(self.subtotal))))
        if(int(self.mesa) != 0):
            c.drawString(35,fin_alto_productos-60,"PROPINA SUGERIDA 10%: ")
            c.drawString(200,fin_alto_productos-60,"$")
            c.drawRightString(250,fin_alto_productos-60,str(
                controller_admin_producto.monetaryFormat(int(self.propina))))
            c.drawString(35,fin_alto_productos-75,"TOTAL + PROPINA: ")
            c.drawString(200,fin_alto_productos-75,"$")
            c.drawRightString(250,fin_alto_productos-75,str(
                controller_admin_producto.monetaryFormat(int(self.total))))

            c.drawString(10,fin_alto_productos-115,"Gracias por su visita.")
        else:
            c.drawString(10,fin_alto_productos-75,"Gracias por su visita.")


        c.save()

        self.imprimir_pdf(os.getcwd() + "/docs/detalle_mesa_"+str(self.mesa)+
            "_documento_"+controller_admin_producto.zerosAtLeft(
                self.num_documento,8)+".pdf")

    def imprimir_pdf(self,pdf):
        """
        Recibe como primer parámetro el URL de un PDF. Abre el PDF en Adobe 
        Acrobat Reader y lo imprime con la impresora predeterminada.
        Espera 5 segundos y cierra el proceso AcroRD32.exe.
        """
        AcroRD32Path = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT,
                                         'Software\\Adobe\\Acrobat\Exe')  
          
        acroread = AcroRD32Path  
        cmd= '{0} /N /T "{1}" ""'.format(acroread,pdf)  
        proc = subprocess.Popen(cmd)  
        time.sleep(5)  
        os.system("TASKKILL /F /IM AcroRD32.exe")  

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FormularioVenta()
    myapp.show()
    sys.exit(app.exec_())
