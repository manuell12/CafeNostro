# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_producto.ui'
#
# Created: Sat Dec 19 05:02:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdminProductos(object):
    def setupUi(self, AdminProductos):
        AdminProductos.setObjectName("AdminProductos")
        AdminProductos.resize(634, 471)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(AdminProductos)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtGui.QGroupBox(AdminProductos)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableProductos = QtGui.QTableWidget(self.groupBox)
        self.tableProductos.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tableProductos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableProductos.setTabKeyNavigation(False)
        self.tableProductos.setProperty("showDropIndicator", False)
        self.tableProductos.setDragDropOverwriteMode(False)
        self.tableProductos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableProductos.setObjectName("tableProductos")
        self.tableProductos.setColumnCount(0)
        self.tableProductos.setRowCount(0)
        self.tableProductos.horizontalHeader().setDefaultSectionSize(20)
        self.tableProductos.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.tableProductos)
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.estado_button = QtGui.QPushButton(self.frame)
        self.estado_button.setMinimumSize(QtCore.QSize(100, 50))
        self.estado_button.setObjectName("estado_button")
        self.horizontalLayout.addWidget(self.estado_button)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.nuevo_button = QtGui.QPushButton(self.frame)
        self.nuevo_button.setMinimumSize(QtCore.QSize(100, 50))
        self.nuevo_button.setObjectName("nuevo_button")
        self.horizontalLayout.addWidget(self.nuevo_button)
        self.editar_button = QtGui.QPushButton(self.frame)
        self.editar_button.setMinimumSize(QtCore.QSize(100, 50))
        self.editar_button.setObjectName("editar_button")
        self.horizontalLayout.addWidget(self.editar_button)
        self.eliminar_button = QtGui.QPushButton(self.frame)
        self.eliminar_button.setMinimumSize(QtCore.QSize(100, 50))
        self.eliminar_button.setObjectName("eliminar_button")
        self.horizontalLayout.addWidget(self.eliminar_button)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(AdminProductos)
        QtCore.QMetaObject.connectSlotsByName(AdminProductos)

    def retranslateUi(self, AdminProductos):
        AdminProductos.setWindowTitle(QtGui.QApplication.translate("AdminProductos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdminProductos", "Productos registrados", None, QtGui.QApplication.UnicodeUTF8))
        self.tableProductos.setSortingEnabled(True)
        self.estado_button.setText(QtGui.QApplication.translate("AdminProductos", "Cambiar estado", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevo_button.setText(QtGui.QApplication.translate("AdminProductos", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_button.setText(QtGui.QApplication.translate("AdminProductos", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_button.setText(QtGui.QApplication.translate("AdminProductos", "E&liminar", None, QtGui.QApplication.UnicodeUTF8))

