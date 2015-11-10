# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\danie\Documents\Proyecto Taller\CafeNostro\nostro\admin_productos\formulario_producto.ui'
#
# Created: Tue Nov 10 01:02:41 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormularioProducto(object):
    def setupUi(self, FormularioProducto):
        FormularioProducto.setObjectName("FormularioProducto")
        FormularioProducto.setEnabled(True)
        FormularioProducto.resize(384, 182)
        self.verticalLayout_3 = QtGui.QVBoxLayout(FormularioProducto)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(FormularioProducto)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_verif = QtGui.QLabel(self.groupBox)
        self.label_verif.setObjectName("label_verif")
        self.verticalLayout.addWidget(self.label_verif)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.verticalLayout_2.addWidget(self.lineEdit_nombre)
        self.lineEdit_descripcion = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_descripcion.setObjectName("lineEdit_descripcion")
        self.verticalLayout_2.addWidget(self.lineEdit_descripcion)
        self.lineEdit_precio_neto = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_precio_neto.setObjectName("lineEdit_precio_neto")
        self.verticalLayout_2.addWidget(self.lineEdit_precio_neto)
        self.comboBox_id_categoria = QtGui.QComboBox(self.groupBox)
        self.comboBox_id_categoria.setObjectName("comboBox_id_categoria")
        self.verticalLayout_2.addWidget(self.comboBox_id_categoria)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
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

    def retranslateUi(self, FormularioProducto):
        FormularioProducto.setWindowTitle(QtGui.QApplication.translate("FormularioProducto", "Formulario Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FormularioProducto", "Datos de Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormularioProducto", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormularioProducto", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_verif.setText(QtGui.QApplication.translate("FormularioProducto", "Precio neto", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FormularioProducto", "Categoria", None, QtGui.QApplication.UnicodeUTF8))

