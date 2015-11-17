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


class MainWindow(QtGui.QMainWindow):
    """
    Clase de la ventana principal.
    El widget central (centralWidget) de la ventana ira cambiando
    respecto a que es lo que el usuario desea hacer.
    """

    def __init__(self, tipo=None):
        'Constructor de la clase'
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        self.showMaximized()
        self.show()
        if(tipo != None):
            if(tipo == 1):
                self.ui.actionUsuarios.setEnabled(False)
                self.ui.actionProductos.setEnabled(False)

    def set_signals(self):
        'Setea los triggers que se usaran para cambiar la interfaz'
        self.ui.actionRealizar_Venta.triggered.connect(self.venta)
        self.ui.actionUsuarios.triggered.connect(self.admin_users)
        self.ui.actionProductos.triggered.connect(self.admin_productos)

    def venta(self):
        'Cambia a la interfaz de venta de producto'
        pass

    def admin_users(self):
        'Cambia a la interfaz de administración de usuarios'
        self.setCentralWidget(AdminUsers())

    def admin_productos(self):
        'Cambia a la interfaz de administración de productos'
        self.setCentralWidget(AdminProductos())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
