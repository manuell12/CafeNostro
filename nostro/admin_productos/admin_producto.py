# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\danie\Documents\Proyecto Taller\CafeNostro\nostro\admin_productos\admin_producto.ui'
#
# Created: Mon Nov 09 23:47:35 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdminProductos(object):
    def setupUi(self, AdminProductos):
        AdminProductos.setObjectName("AdminProductos")
        AdminProductos.resize(600, 400)
        AdminProductos.setMaximumSize(QtCore.QSize(600, 400))
        self.verticalLayout = QtGui.QVBoxLayout(AdminProductos)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AdminProductos)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableProductos = QtGui.QTableView(AdminProductos)
        self.tableProductos.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tableProductos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableProductos.setTabKeyNavigation(False)
        self.tableProductos.setProperty("showDropIndicator", False)
        self.tableProductos.setDragDropOverwriteMode(False)
        self.tableProductos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableProductos.setObjectName("tableProductos")
        self.tableProductos.horizontalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.tableProductos)
        self.frame = QtGui.QFrame(AdminProductos)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nuevo_button = QtGui.QPushButton(self.frame)
        self.nuevo_button.setObjectName("nuevo_button")
        self.horizontalLayout.addWidget(self.nuevo_button)
        self.editar_button = QtGui.QPushButton(self.frame)
        self.editar_button.setObjectName("editar_button")
        self.horizontalLayout.addWidget(self.editar_button)
        self.eliminar_button = QtGui.QPushButton(self.frame)
        self.eliminar_button.setObjectName("eliminar_button")
        self.horizontalLayout.addWidget(self.eliminar_button)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(AdminProductos)
        QtCore.QMetaObject.connectSlotsByName(AdminProductos)

    def retranslateUi(self, AdminProductos):
        AdminProductos.setWindowTitle(QtGui.QApplication.translate("AdminProductos", "Lista de Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdminProductos", "Productos registrados", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevo_button.setText(QtGui.QApplication.translate("AdminProductos", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_button.setText(QtGui.QApplication.translate("AdminProductos", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_button.setText(QtGui.QApplication.translate("AdminProductos", "E&liminar", None, QtGui.QApplication.UnicodeUTF8))

