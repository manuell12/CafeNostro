# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Thu Nov 05 00:30:02 2015
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUsuarios = QtGui.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.menuAdministraci_n.addAction(self.actionUsuarios)
        self.menubar.addAction(self.menuAdministraci_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CaféNostro", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setTitle(QtGui.QApplication.translate("MainWindow", "&Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setText(QtGui.QApplication.translate("MainWindow", "&Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de usuarios", None, QtGui.QApplication.UnicodeUTF8))

