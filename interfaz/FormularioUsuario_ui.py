# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormularioUsuario.ui'
#
# Created: Thu Nov 05 01:22:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormularioUsuario(object):
    def setupUi(self, FormularioUsuario):
        FormularioUsuario.setObjectName("FormularioUsuario")
        FormularioUsuario.setEnabled(True)
        FormularioUsuario.resize(385, 180)
        self.verticalLayout_3 = QtGui.QVBoxLayout(FormularioUsuario)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(FormularioUsuario)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.verticalLayout_2.addWidget(self.lineEdit_nombre)
        self.lineEdit_apellido = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.verticalLayout_2.addWidget(self.lineEdit_apellido)
        self.lineEdit_clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_clave.setObjectName("lineEdit_clave")
        self.verticalLayout_2.addWidget(self.lineEdit_clave)
        self.lineEdit_rut = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_rut.setObjectName("lineEdit_rut")
        self.verticalLayout_2.addWidget(self.lineEdit_rut)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(FormularioUsuario)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(FormularioUsuario)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), FormularioUsuario.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), FormularioUsuario.reject)
        QtCore.QMetaObject.connectSlotsByName(FormularioUsuario)

    def retranslateUi(self, FormularioUsuario):
        FormularioUsuario.setWindowTitle(QtGui.QApplication.translate("FormularioUsuario", "Formulario Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("FormularioUsuario", "Datos de Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormularioUsuario", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormularioUsuario", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FormularioUsuario", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormularioUsuario", "Rut", None, QtGui.QApplication.UnicodeUTF8))

