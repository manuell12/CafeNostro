# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario_venta.ui'
#
# Created: Tue Dec 08 15:31:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormularioVenta(object):
    def setupUi(self, FormularioVenta):
        FormularioVenta.setObjectName("FormularioVenta")
        FormularioVenta.resize(719, 507)
        self.verticalLayout_6 = QtGui.QVBoxLayout(FormularioVenta)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtGui.QGroupBox(FormularioVenta)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_buscar_codigo = QtGui.QLabel(self.groupBox)
        self.label_buscar_codigo.setObjectName("label_buscar_codigo")
        self.horizontalLayout_5.addWidget(self.label_buscar_codigo)
        self.lineEdit_buscar_codigo = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_buscar_codigo.setObjectName("lineEdit_buscar_codigo")
        self.horizontalLayout_5.addWidget(self.lineEdit_buscar_codigo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableView_total_productos = QtGui.QTableView(self.groupBox)
        self.tableView_total_productos.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableView_total_productos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_total_productos.setAlternatingRowColors(True)
        self.tableView_total_productos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView_total_productos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView_total_productos.setShowGrid(True)
        self.tableView_total_productos.setCornerButtonEnabled(False)
        self.tableView_total_productos.setObjectName("tableView_total_productos")
        self.tableView_total_productos.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableView_total_productos)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_filtrar_cocina = QtGui.QPushButton(self.groupBox)
        self.pushButton_filtrar_cocina.setMinimumSize(QtCore.QSize(101, 41))
        self.pushButton_filtrar_cocina.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_filtrar_cocina.setObjectName("pushButton_filtrar_cocina")
        self.gridLayout.addWidget(self.pushButton_filtrar_cocina, 0, 1, 1, 1)
        self.pushButton_filtrar_cafeteria = QtGui.QPushButton(self.groupBox)
        self.pushButton_filtrar_cafeteria.setMinimumSize(QtCore.QSize(101, 41))
        self.pushButton_filtrar_cafeteria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_filtrar_cafeteria.setObjectName("pushButton_filtrar_cafeteria")
        self.gridLayout.addWidget(self.pushButton_filtrar_cafeteria, 0, 0, 1, 1)
        self.pushButton_filtrar_bebidas = QtGui.QPushButton(self.groupBox)
        self.pushButton_filtrar_bebidas.setMinimumSize(QtCore.QSize(101, 41))
        self.pushButton_filtrar_bebidas.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_filtrar_bebidas.setObjectName("pushButton_filtrar_bebidas")
        self.gridLayout.addWidget(self.pushButton_filtrar_bebidas, 1, 0, 1, 1)
        self.pushButton_filtrar_helados = QtGui.QPushButton(self.groupBox)
        self.pushButton_filtrar_helados.setMinimumSize(QtCore.QSize(101, 41))
        self.pushButton_filtrar_helados.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_filtrar_helados.setObjectName("pushButton_filtrar_helados")
        self.gridLayout.addWidget(self.pushButton_filtrar_helados, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton_aumentar_cantidad = QtGui.QPushButton(self.groupBox)
        self.pushButton_aumentar_cantidad.setMinimumSize(QtCore.QSize(60, 41))
        self.pushButton_aumentar_cantidad.setMaximumSize(QtCore.QSize(60, 41))
        self.pushButton_aumentar_cantidad.setObjectName("pushButton_aumentar_cantidad")
        self.verticalLayout_3.addWidget(self.pushButton_aumentar_cantidad)
        self.pushButton_disminuir_cantidad = QtGui.QPushButton(self.groupBox)
        self.pushButton_disminuir_cantidad.setMinimumSize(QtCore.QSize(60, 41))
        self.pushButton_disminuir_cantidad.setMaximumSize(QtCore.QSize(60, 41))
        self.pushButton_disminuir_cantidad.setObjectName("pushButton_disminuir_cantidad")
        self.verticalLayout_3.addWidget(self.pushButton_disminuir_cantidad)
        self.pushButton_eliminar = QtGui.QPushButton(self.groupBox)
        self.pushButton_eliminar.setMinimumSize(QtCore.QSize(60, 41))
        self.pushButton_eliminar.setMaximumSize(QtCore.QSize(60, 51))
        self.pushButton_eliminar.setObjectName("pushButton_eliminar")
        self.verticalLayout_3.addWidget(self.pushButton_eliminar)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(74, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lcdNumber_subtotal = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_subtotal.setMinimumSize(QtCore.QSize(76, 0))
        self.lcdNumber_subtotal.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_subtotal.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumber_subtotal.setSmallDecimalPoint(True)
        self.lcdNumber_subtotal.setMode(QtGui.QLCDNumber.Dec)
        self.lcdNumber_subtotal.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_subtotal.setProperty("value", 0.0)
        self.lcdNumber_subtotal.setObjectName("lcdNumber_subtotal")
        self.horizontalLayout.addWidget(self.lcdNumber_subtotal)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_numero_pagos = QtGui.QLabel(self.groupBox)
        self.label_numero_pagos.setObjectName("label_numero_pagos")
        self.horizontalLayout.addWidget(self.label_numero_pagos)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(74, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lcdNumber_propina = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_propina.setMinimumSize(QtCore.QSize(76, 0))
        self.lcdNumber_propina.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_propina.setSmallDecimalPoint(True)
        self.lcdNumber_propina.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_propina.setObjectName("lcdNumber_propina")
        self.horizontalLayout_2.addWidget(self.lcdNumber_propina)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(74, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lcdNumber_total = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_total.setMinimumSize(QtCore.QSize(76, 0))
        self.lcdNumber_total.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumber_total.setSmallDecimalPoint(True)
        self.lcdNumber_total.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_total.setObjectName("lcdNumber_total")
        self.horizontalLayout_3.addWidget(self.lcdNumber_total)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.tableView_pedido = QtGui.QTableView(self.groupBox)
        self.tableView_pedido.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView_pedido.setAlternatingRowColors(True)
        self.tableView_pedido.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView_pedido.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView_pedido.setCornerButtonEnabled(False)
        self.tableView_pedido.setObjectName("tableView_pedido")
        self.tableView_pedido.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableView_pedido, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 3, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem4)
        self.pushButton_agregar = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_agregar.sizePolicy().hasHeightForWidth())
        self.pushButton_agregar.setSizePolicy(sizePolicy)
        self.pushButton_agregar.setMinimumSize(QtCore.QSize(71, 71))
        self.pushButton_agregar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_agregar.setObjectName("pushButton_agregar")
        self.verticalLayout_5.addWidget(self.pushButton_agregar)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem6)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.comboBox_tipo_pago = QtGui.QComboBox(self.groupBox)
        self.comboBox_tipo_pago.setMinimumSize(QtCore.QSize(121, 40))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_tipo_pago.setFont(font)
        self.comboBox_tipo_pago.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_tipo_pago.setIconSize(QtCore.QSize(16, 40))
        self.comboBox_tipo_pago.setObjectName("comboBox_tipo_pago")
        self.horizontalLayout_6.addWidget(self.comboBox_tipo_pago)
        self.pushButton_opciones = QtGui.QPushButton(self.groupBox)
        self.pushButton_opciones.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_opciones.setObjectName("pushButton_opciones")
        self.horizontalLayout_6.addWidget(self.pushButton_opciones)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.pushButton_imprimir_comandas = QtGui.QPushButton(self.groupBox)
        self.pushButton_imprimir_comandas.setMinimumSize(QtCore.QSize(111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_imprimir_comandas.setFont(font)
        self.pushButton_imprimir_comandas.setObjectName("pushButton_imprimir_comandas")
        self.horizontalLayout_4.addWidget(self.pushButton_imprimir_comandas)
        self.pushButton_cerrar_venta = QtGui.QPushButton(self.groupBox)
        self.pushButton_cerrar_venta.setMinimumSize(QtCore.QSize(100, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.pushButton_cerrar_venta.setFont(font)
        self.pushButton_cerrar_venta.setObjectName("pushButton_cerrar_venta")
        self.horizontalLayout_4.addWidget(self.pushButton_cerrar_venta)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox)

        self.retranslateUi(FormularioVenta)
        QtCore.QMetaObject.connectSlotsByName(FormularioVenta)

    def retranslateUi(self, FormularioVenta):
        FormularioVenta.setWindowTitle(QtGui.QApplication.translate("FormularioVenta", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FormularioVenta", "Formulario de Venta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_buscar_codigo.setText(QtGui.QApplication.translate("FormularioVenta", "Buscar producto por código:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtrar_cocina.setText(QtGui.QApplication.translate("FormularioVenta", "Cocina", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtrar_cafeteria.setText(QtGui.QApplication.translate("FormularioVenta", "Cafeteria", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtrar_bebidas.setText(QtGui.QApplication.translate("FormularioVenta", "Bebidas", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_filtrar_helados.setText(QtGui.QApplication.translate("FormularioVenta", "Helados", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormularioVenta", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_aumentar_cantidad.setText(QtGui.QApplication.translate("FormularioVenta", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_disminuir_cantidad.setText(QtGui.QApplication.translate("FormularioVenta", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_eliminar.setText(QtGui.QApplication.translate("FormularioVenta", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormularioVenta", "Subtotal:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("FormularioVenta", "<html><head/><body><p>Número de pagos: </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_numero_pagos.setText(QtGui.QApplication.translate("FormularioVenta", "01", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FormularioVenta", "Propina (10%):", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormularioVenta", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_agregar.setText(QtGui.QApplication.translate("FormularioVenta", "AGREGAR\n"
"-->", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_opciones.setText(QtGui.QApplication.translate("FormularioVenta", "Mas opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_imprimir_comandas.setText(QtGui.QApplication.translate("FormularioVenta", "Imprimir Comanda", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cerrar_venta.setText(QtGui.QApplication.translate("FormularioVenta", "Pagar", None, QtGui.QApplication.UnicodeUTF8))

