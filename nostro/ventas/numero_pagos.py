# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numero_pagos.ui'
#
# Created: Sat Dec 12 12:23:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NumeroPagos(object):
    def setupUi(self, NumeroPagos):
        NumeroPagos.setObjectName("NumeroPagos")
        NumeroPagos.resize(477, 490)
        NumeroPagos.setMinimumSize(QtCore.QSize(477, 490))
        self.verticalLayout_3 = QtGui.QVBoxLayout(NumeroPagos)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(NumeroPagos)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.spinBox_numero_pagos = QtGui.QSpinBox(NumeroPagos)
        self.spinBox_numero_pagos.setObjectName("spinBox_numero_pagos")
        self.horizontalLayout_4.addWidget(self.spinBox_numero_pagos)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tableWidget_resumen = QtGui.QTableWidget(NumeroPagos)
        self.tableWidget_resumen.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_resumen.setObjectName("tableWidget_resumen")
        self.tableWidget_resumen.setColumnCount(0)
        self.tableWidget_resumen.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget_resumen)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(NumeroPagos)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_price = QtGui.QLabel(NumeroPagos)
        self.label_price.setObjectName("label_price")
        self.horizontalLayout.addWidget(self.label_price)
        self.lcdNumber_subtotal = QtGui.QLCDNumber(NumeroPagos)
        self.lcdNumber_subtotal.setMinimumSize(QtCore.QSize(76, 0))
        self.lcdNumber_subtotal.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_subtotal.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber_subtotal.setSmallDecimalPoint(True)
        self.lcdNumber_subtotal.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_subtotal.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_subtotal.setProperty("value", 0.0)
        self.lcdNumber_subtotal.setObjectName("lcdNumber_subtotal")
        self.horizontalLayout.addWidget(self.lcdNumber_subtotal)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.groupBox = QtGui.QGroupBox(NumeroPagos)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_numero_pagos = QtGui.QVBoxLayout()
        self.verticalLayout_numero_pagos.setObjectName("verticalLayout_numero_pagos")
        self.verticalLayout.addLayout(self.verticalLayout_numero_pagos)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.pushButton_pagar = QtGui.QPushButton(NumeroPagos)
        self.pushButton_pagar.setObjectName("pushButton_pagar")
        self.verticalLayout_3.addWidget(self.pushButton_pagar)

        self.retranslateUi(NumeroPagos)
        QtCore.QMetaObject.connectSlotsByName(NumeroPagos)

    def retranslateUi(self, NumeroPagos):
        NumeroPagos.setWindowTitle(QtGui.QApplication.translate("NumeroPagos", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NumeroPagos", "Ingresa número de pagos:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NumeroPagos", "Subtotal:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_price.setText(QtGui.QApplication.translate("NumeroPagos", "<html><head/><body><p><span style=\" font-size:20pt;\">$</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pagar.setText(QtGui.QApplication.translate("NumeroPagos", "Pagar", None, QtGui.QApplication.UnicodeUTF8))

