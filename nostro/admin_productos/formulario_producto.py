# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulario_producto.ui'
#
# Created: Thu Nov 26 04:02:52 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormularioProducto(object):
    def setupUi(self, FormularioProducto):
        FormularioProducto.setObjectName("FormularioProducto")
        FormularioProducto.setEnabled(True)
        FormularioProducto.resize(586, 277)
        self.verticalLayout_3 = QtGui.QVBoxLayout(FormularioProducto)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(FormularioProducto)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_descripcion = QtGui.QTextEdit(self.groupBox)
        self.lineEdit_descripcion.setObjectName("lineEdit_descripcion")
        self.gridLayout.addWidget(self.lineEdit_descripcion, 2, 1, 1, 1)
        self.label_verif = QtGui.QLabel(self.groupBox)
        self.label_verif.setObjectName("label_verif")
        self.gridLayout.addWidget(self.label_verif, 3, 0, 1, 1)
        self.label_error_nombre = QtGui.QLabel(self.groupBox)
        self.label_error_nombre.setMinimumSize(QtCore.QSize(220, 20))
        self.label_error_nombre.setObjectName("label_error_nombre")
        self.gridLayout.addWidget(self.label_error_nombre, 0, 2, 1, 1)
        self.label_error_descripcion = QtGui.QLabel(self.groupBox)
        self.label_error_descripcion.setText("")
        self.label_error_descripcion.setObjectName("label_error_descripcion")
        self.gridLayout.addWidget(self.label_error_descripcion, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.gridLayout.addWidget(self.lineEdit_nombre, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_precio_neto = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_precio_neto.setObjectName("lineEdit_precio_neto")
        self.gridLayout.addWidget(self.lineEdit_precio_neto, 3, 1, 1, 1)
        self.label_error_precio = QtGui.QLabel(self.groupBox)
        self.label_error_precio.setMinimumSize(QtCore.QSize(177, 20))
        self.label_error_precio.setObjectName("label_error_precio")
        self.gridLayout.addWidget(self.label_error_precio, 3, 2, 1, 1)
        self.comboBox_id_categoria = QtGui.QComboBox(self.groupBox)
        self.comboBox_id_categoria.setObjectName("comboBox_id_categoria")
        self.gridLayout.addWidget(self.comboBox_id_categoria, 4, 1, 1, 1)
        self.label_error_categoria = QtGui.QLabel(self.groupBox)
        self.label_error_categoria.setMinimumSize(QtCore.QSize(177, 20))
        self.label_error_categoria.setObjectName("label_error_categoria")
        self.gridLayout.addWidget(self.label_error_categoria, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_codigo = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.gridLayout.addWidget(self.lineEdit_codigo, 1, 1, 1, 1)
        self.label_error_codigo = QtGui.QLabel(self.groupBox)
        self.label_error_codigo.setText("")
        self.label_error_codigo.setObjectName("label_error_codigo")
        self.gridLayout.addWidget(self.label_error_codigo, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(FormularioProducto)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(FormularioProducto)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), FormularioProducto.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), FormularioProducto.reject)
        QtCore.QMetaObject.connectSlotsByName(FormularioProducto)
        FormularioProducto.setTabOrder(self.lineEdit_nombre, self.lineEdit_descripcion)
        FormularioProducto.setTabOrder(self.lineEdit_descripcion, self.lineEdit_precio_neto)
        FormularioProducto.setTabOrder(self.lineEdit_precio_neto, self.comboBox_id_categoria)
        FormularioProducto.setTabOrder(self.comboBox_id_categoria, self.buttonBox)

    def retranslateUi(self, FormularioProducto):
        FormularioProducto.setWindowTitle(QtGui.QApplication.translate("FormularioProducto", "Formulario Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FormularioProducto", "Datos del producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_verif.setText(QtGui.QApplication.translate("FormularioProducto", "Precio neto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_nombre.setText(QtGui.QApplication.translate("FormularioProducto", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">No puede estar vacío</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormularioProducto", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FormularioProducto", "Categoría", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormularioProducto", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_precio.setText(QtGui.QApplication.translate("FormularioProducto", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Valor entre 0 y 99999</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_categoria.setText(QtGui.QApplication.translate("FormularioProducto", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Debe seleccionar una categoría</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormularioProducto", "Código", None, QtGui.QApplication.UnicodeUTF8))

