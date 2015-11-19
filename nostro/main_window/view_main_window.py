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
from ventas.view_formulario_venta import FormularioVenta


class MainWindow(QtGui.QMainWindow):
    """
    Clase de la ventana principal.
    El widget central (centralWidget) de la ventana ira cambiando
    respecto a que es lo que el usuario desea hacer.
    """

    venta_directa_en_curso = False

    def __init__(self, tipo=None, rut=None):
        'Constructor de la clase'
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        self.showMaximized()
        self.show()
        self.ui.stackedWidget.addWidget(AdminUsers()) #2
        self.ui.stackedWidget.addWidget(AdminProductos()) #3
        self.rut = rut
        if(tipo != None):
            if(tipo == 1):
                self.ui.actionUsuarios.setEnabled(False)
                self.ui.actionProductos.setEnabled(False)

    def set_signals(self):
        'Setea los triggers que se usaran para cambiar la interfaz'
        self.ui.actionRealizar_Venta.triggered.connect(self.venta)
        self.ui.actionUsuarios.triggered.connect(self.admin_users)
        self.ui.actionProductos.triggered.connect(self.admin_productos)
        self.ui.pushButton_compra_directa.clicked.connect(self.formulario_venta_directa)

    def venta(self):
        'Cambia a la interfaz de venta de producto'
        pass

    def formulario_venta_directa(self):
        'Cambia a la interfaz de formulario de venta directa'
        mesa = "0"
        if(not self.venta_directa_en_curso):
            self.ui.stackedWidget.addWidget(FormularioVenta(self.rut,mesa)) #4
            self.venta_directa_en_curso = True
        self.ui.stackedWidget.setCurrentIndex(4)

    def admin_users(self):
        'Cambia a la interfaz de administración de usuarios'
        self.ui.stackedWidget.setCurrentIndex(2)

    def admin_productos(self):
        'Cambia a la interfaz de administración de productos'
        self.ui.stackedWidget.setCurrentIndex(3)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
