# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui'
#
# Created: Sat Nov 14 01:26:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
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
        self.menuVenta = QtGui.QMenu(self.menubar)
        self.menuVenta.setObjectName("menuVenta")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUsuarios = QtGui.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionProductos = QtGui.QAction(MainWindow)
        self.actionProductos.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionProductos.setObjectName("actionProductos")
        self.actionRealizar_Venta = QtGui.QAction(MainWindow)
        self.actionRealizar_Venta.setObjectName("actionRealizar_Venta")
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCambiar_Usuario = QtGui.QAction(MainWindow)
        self.actionCambiar_Usuario.setObjectName("actionCambiar_Usuario")
        self.menuAdministraci_n.addAction(self.actionUsuarios)
        self.menuAdministraci_n.addAction(self.actionProductos)
        self.menuVenta.addAction(self.actionRealizar_Venta)
        self.menuArchivo.addAction(self.actionCambiar_Usuario)
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVenta.menuAction())
        self.menubar.addAction(self.menuAdministraci_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CaféNostro", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setStatusTip(QtGui.QApplication.translate("MainWindow", "Sección administrativa de la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setTitle(QtGui.QApplication.translate("MainWindow", "&Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVenta.setStatusTip(QtGui.QApplication.translate("MainWindow", "Sección venta de la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVenta.setTitle(QtGui.QApplication.translate("MainWindow", "&Venta", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setText(QtGui.QApplication.translate("MainWindow", "&Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setText(QtGui.QApplication.translate("MainWindow", "&Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de productos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setText(QtGui.QApplication.translate("MainWindow", "&Realizar Venta", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana donde se venden los productos del local", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cierra la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_Usuario.setText(QtGui.QApplication.translate("MainWindow", "Cambiar Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_Usuario.setStatusTip(QtGui.QApplication.translate("MainWindow", "Regresa a la ventan Login para poder cambiar el usuario", None, QtGui.QApplication.UnicodeUTF8))

