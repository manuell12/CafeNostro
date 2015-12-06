# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mesas_venta.ui'
#
# Created: Sun Dec 06 16:23:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MesasVenta(object):
    def setupUi(self, MesasVenta):
        MesasVenta.setObjectName("MesasVenta")
        MesasVenta.resize(610, 446)
        self.horizontalLayout = QtGui.QHBoxLayout(MesasVenta)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(MesasVenta)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(162, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 258, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(162, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.gridLayout_mesas = QtGui.QGridLayout()
        self.gridLayout_mesas.setSpacing(20)
        self.gridLayout_mesas.setObjectName("gridLayout_mesas")
        self.gridLayout.addLayout(self.gridLayout_mesas, 3, 1, 1, 1)
        self.label_info = QtGui.QLabel(self.groupBox)
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.gridLayout.addWidget(self.label_info, 1, 1, 1, 1)
        self.pushButton_aceptar = QtGui.QPushButton(self.groupBox)
        self.pushButton_aceptar.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_aceptar.setObjectName("pushButton_aceptar")
        self.gridLayout.addWidget(self.pushButton_aceptar, 1, 3, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(MesasVenta)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_agregar = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_agregar.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_agregar.setCheckable(False)
        self.pushButton_agregar.setObjectName("pushButton_agregar")
        self.verticalLayout.addWidget(self.pushButton_agregar)
        self.pushButton_borrar = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_borrar.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_borrar.setObjectName("pushButton_borrar")
        self.verticalLayout.addWidget(self.pushButton_borrar)
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_unir = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_unir.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_unir.setObjectName("pushButton_unir")
        self.verticalLayout.addWidget(self.pushButton_unir)
        self.pushButton_separar = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_separar.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_separar.setObjectName("pushButton_separar")
        self.verticalLayout.addWidget(self.pushButton_separar)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(MesasVenta)
        QtCore.QMetaObject.connectSlotsByName(MesasVenta)

    def retranslateUi(self, MesasVenta):
        MesasVenta.setWindowTitle(QtGui.QApplication.translate("MesasVenta", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MesasVenta", "Mesas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_aceptar.setText(QtGui.QApplication.translate("MesasVenta", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MesasVenta", "Configuracion", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_agregar.setText(QtGui.QApplication.translate("MesasVenta", "Agregar Mesa", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_borrar.setText(QtGui.QApplication.translate("MesasVenta", "Borrar Mesa", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_unir.setText(QtGui.QApplication.translate("MesasVenta", "Unir Mesas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_separar.setText(QtGui.QApplication.translate("MesasVenta", "Separar Mesas", None, QtGui.QApplication.UnicodeUTF8))

