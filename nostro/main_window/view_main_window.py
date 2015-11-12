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
from view_admin_user import AdminUsers
from view_admin_producto import AdminProductos


class MainWindow(QtGui.QMainWindow):
    closed = QtCore.Signal()

    def __init__(self,tipo=None):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_signals()
        self.show()
        if(tipo != None):
            if(tipo == 1):
                self.ui.actionUsuarios.setEnabled(False)
                self.ui.actionProductos.setEnabled(False)
    def set_signals(self):
        QtGui.QAction.connect(self.ui.actionUsuarios,
                              QtCore.SIGNAL("triggered()"), self.admin_users)
        QtGui.QAction.connect(self.ui.actionProductos,
                              QtCore.SIGNAL("triggered()"), self.admin_productos)

    def admin_users(self):
        admin_user = AdminUsers().exec_()
        self.setVisible(True)

    def admin_productos(self):
        admin_producto = AdminProductos().exec_()
        self.setVisible(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
