#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Café Nostro.
Archivo de la vista principal que concentra practicamente todas las 
funcionalidades.
"""
import sys
from PySide import QtCore, QtGui
from main_window import Ui_MainWindow
from admin_usuarios.view_admin_user import AdminUsers
from admin_productos.view_admin_producto import AdminProductos
from ventas.view_admin_venta import AdminVentas
from ventas.view_formulario_venta import FormularioVenta
import admin_usuarios.controller_admin_user as controller


class MainWindow(QtGui.QMainWindow):
    """
    Clase de la ventana principal.
    El widget central (centralWidget) de la ventana ira cambiando
    respecto a que es lo que el usuario desea hacer.
    """

    venta_directa_en_curso = False
    num_mesas = 5

    def __init__(self, tipo=None, rut=None):
        'Constructor de la clase'
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        self.showMaximized()
        self.show()
        self.rut = rut
        self.ui.stackedWidget.addWidget(AdminUsers()) #2
        self.ui.stackedWidget.addWidget(AdminProductos()) #3
        self.ui.stackedWidget.addWidget(FormularioVenta(self.ui,self.rut,"0")) #4
        self.ui.stackedWidget.addWidget(AdminVentas(self.ui)) #5
        for i in range(self.num_mesas+1): #6 = primera mesa
            self.ui.stackedWidget.addWidget(FormularioVenta(self.ui,self.rut,str(i)))

        # self.ui.stackedWidget.addWidget(FormularioVenta(self.rut,"0")) #4
        # self.ui.stackedWidget.addWidget(AdminVentas(self.ui)) #5    

        self.nombre = unicode(controller.getUsuarioRut(rut)[0].nombre)+" "+unicode(controller.getUsuarioRut(rut)[0].apellido)
        if(controller.getUsuarioRut(rut)[0].nombre == "root"):
            self.nombre = "ROOT"
        self.ui.label_usuario.setText(u"<font color='black' size='5'><b>"+self.nombre+"</b></font>")
        if(tipo != None):
            if(tipo == 1):
                self.ui.actionUsuarios.setEnabled(False)
                self.ui.actionProductos.setEnabled(False)
        self.set_combobox_mesas()

    def set_combobox_mesas(self):
        __mesas__ = [" Pedido por mesa"]
        for i in range(self.num_mesas):
            __mesas__.append("    Mesa:     "+str(i+1)) 
            model = QtGui.QStandardItemModel()
        for text in __mesas__:
            text_item = QtGui.QStandardItem(text)
            text_item.setSizeHint(QtCore.QSize(100, 50))
            text_item.setTextAlignment(QtCore.Qt.AlignHCenter)
            text_item.setTextAlignment(QtCore.Qt.AlignVCenter)
            model.appendRow([text_item])
        view = QtGui.QTreeView()
        view.header().hide()
        view.setRootIsDecorated(False)
        self.ui.comboBox_mesas.setView(view)
        self.ui.comboBox_mesas.setModel(model)

    def set_signals(self):
        'Setea los triggers que se usaran para cambiar la interfaz'
        self.ui.actionVentas.triggered.connect(self.admin_ventas)
        self.ui.actionUsuarios.triggered.connect(self.admin_users)
        self.ui.actionProductos.triggered.connect(self.admin_productos)
        self.ui.pushButton_compra_directa.clicked.connect(self.formulario_venta_directa)
        self.ui.pushButton_agregar_mesa.clicked.connect(self.action_agregar_mesa)
        self.ui.comboBox_mesas.currentIndexChanged.connect(self.comboBox_mesas_changed)

    def action_agregar_mesa(self):
        self.num_mesas = self.num_mesas+1
        self.ui.stackedWidget.addWidget(FormularioVenta(self.ui,self.rut,str(self.num_mesas)))
        self.set_combobox_mesas()

    def comboBox_mesas_changed(self,index):
        if(index == 0):
            pass
        else:
            self.ui.stackedWidget.setCurrentIndex(index+6)

    def admin_users(self):
        'Cambia a la interfaz de administración de usuarios'
        self.ui.comboBox_mesas.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(2)

    def admin_productos(self):
        'Cambia a la interfaz de administración de productos'
        self.ui.comboBox_mesas.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(3)

    def formulario_venta_directa(self):
        'Cambia a la interfaz de formulario de venta directa'
        self.ui.comboBox_mesas.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(4)

    def admin_ventas(self):
        'Cambia a la interfaz de editar ventas de productos'
        self.ui.comboBox_mesas.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(5)
# =======
#         """Cambia a la interfaz de venta de producto y la actualiza"""
#         self.ui.stackedWidget.setCurrentIndex(5)
#         self.ui.stackedWidget.currentWidget().reload_data_table()
#         # print self.ui.stackedWidget.count()
# >>>>>>> EditarVenta

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
