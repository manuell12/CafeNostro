# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_venta.ui'
#
# Created: Thu Nov 26 11:11:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdminVentas(object):
    def setupUi(self, AdminVentas):
        AdminVentas.setObjectName("AdminVentas")
        AdminVentas.resize(612, 407)
        self.verticalLayout = QtGui.QVBoxLayout(AdminVentas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AdminVentas)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView_ventas = QtGui.QTableView(AdminVentas)
        self.tableView_ventas.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tableView_ventas.setMouseTracking(True)
        self.tableView_ventas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_ventas.setTabKeyNavigation(False)
        self.tableView_ventas.setProperty("showDropIndicator", False)
        self.tableView_ventas.setDragDropOverwriteMode(False)
        self.tableView_ventas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView_ventas.setObjectName("tableView_ventas")
        self.tableView_ventas.horizontalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.tableView_ventas)
        self.frame = QtGui.QFrame(AdminVentas)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_editar = QtGui.QPushButton(self.frame)
        self.pushButton_editar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout.addWidget(self.pushButton_editar)
        self.pushButton_eliminar = QtGui.QPushButton(self.frame)
        self.pushButton_eliminar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.horizontalLayout.addWidget(self.pushButton_eliminar)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(AdminVentas)
        QtCore.QMetaObject.connectSlotsByName(AdminVentas)

    def retranslateUi(self, AdminVentas):
        AdminVentas.setWindowTitle(QtGui.QApplication.translate("AdminVentas", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdminVentas", "Ventas realizadas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_editar.setText(QtGui.QApplication.translate("AdminVentas", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_eliminar.setText(QtGui.QApplication.translate("AdminVentas", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))

