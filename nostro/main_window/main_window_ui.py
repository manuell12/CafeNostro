# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\danie\Documents\Proyecto Taller\CafeNostro\nostro\main_window\main_window.ui'
#
# Created: Tue Nov 10 00:08:16 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdministraci_n = QtGui.QMenu(self.menubar)
        self.menuAdministraci_n.setObjectName("menuAdministraci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUsuarios = QtGui.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionProductos = QtGui.QAction(MainWindow)
        self.actionProductos.setObjectName("actionProductos")
        self.menuAdministraci_n.addAction(self.actionUsuarios)
        self.menuAdministraci_n.addAction(self.actionProductos)
        self.menubar.addAction(self.menuAdministraci_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionUsuarios, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CaféNostro", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setTitle(QtGui.QApplication.translate("MainWindow", "&Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setText(QtGui.QApplication.translate("MainWindow", "&Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setText(QtGui.QApplication.translate("MainWindow", "Productos", None, QtGui.QApplication.UnicodeUTF8))

