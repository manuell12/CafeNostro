# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormularioUsuario.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormularioUsuario(object):
    def setupUi(self, FormularioUsuario):
        FormularioUsuario.setObjectName(_fromUtf8("FormularioUsuario"))
        FormularioUsuario.setEnabled(True)
        FormularioUsuario.resize(385, 180)
        self.verticalLayout_3 = QtGui.QVBoxLayout(FormularioUsuario)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(FormularioUsuario)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nombre.setObjectName(_fromUtf8("lineEdit_nombre"))
        self.verticalLayout_2.addWidget(self.lineEdit_nombre)
        self.lineEdit_apellido = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_apellido.setObjectName(_fromUtf8("lineEdit_apellido"))
        self.verticalLayout_2.addWidget(self.lineEdit_apellido)
        self.lineEdit_clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_clave.setObjectName(_fromUtf8("lineEdit_clave"))
        self.verticalLayout_2.addWidget(self.lineEdit_clave)
        self.lineEdit_rut = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_rut.setObjectName(_fromUtf8("lineEdit_rut"))
        self.verticalLayout_2.addWidget(self.lineEdit_rut)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(FormularioUsuario)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(FormularioUsuario)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FormularioUsuario.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FormularioUsuario.reject)
        QtCore.QMetaObject.connectSlotsByName(FormularioUsuario)

    def retranslateUi(self, FormularioUsuario):
        FormularioUsuario.setWindowTitle(_translate("FormularioUsuario", "Formulario Usuario", None))
        self.groupBox.setTitle(_translate("FormularioUsuario", "Datos de Usuario", None))
        self.label.setText(_translate("FormularioUsuario", "Nombre", None))
        self.label_2.setText(_translate("FormularioUsuario", "Apellido", None))
        self.label_4.setText(_translate("FormularioUsuario", "Contraseña", None))
        self.label_3.setText(_translate("FormularioUsuario", "Rut", None))

