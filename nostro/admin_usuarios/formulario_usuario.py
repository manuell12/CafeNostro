# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\danie\Documents\ProyectoTaller\CafeNostro\nostro\admin_usuarios\formulario_usuario_ui.ui'
#
# Created: Wed Nov 11 18:12:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormularioUsuario(object):
    def setupUi(self, FormularioUsuario):
        FormularioUsuario.setObjectName("FormularioUsuario")
        FormularioUsuario.setEnabled(True)
        FormularioUsuario.resize(579, 287)
        self.verticalLayout_3 = QtGui.QVBoxLayout(FormularioUsuario)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtGui.QGroupBox(FormularioUsuario)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_error_clave_actual = QtGui.QLabel(self.groupBox)
        self.label_error_clave_actual.setText("")
        self.label_error_clave_actual.setObjectName("label_error_clave_actual")
        self.gridLayout.addWidget(self.label_error_clave_actual, 3, 2, 1, 1)
        self.label_clave = QtGui.QLabel(self.groupBox)
        self.label_clave.setObjectName("label_clave")
        self.gridLayout.addWidget(self.label_clave, 4, 0, 1, 1)
        self.lineEdit_clave = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_clave.setObjectName("lineEdit_clave")
        self.gridLayout.addWidget(self.lineEdit_clave, 4, 1, 1, 1)
        self.label_error_clave = QtGui.QLabel(self.groupBox)
        self.label_error_clave.setText("")
        self.label_error_clave.setObjectName("label_error_clave")
        self.gridLayout.addWidget(self.label_error_clave, 4, 2, 1, 1)
        self.lineEdit_verif = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_verif.setObjectName("lineEdit_verif")
        self.gridLayout.addWidget(self.lineEdit_verif, 5, 1, 1, 1)
        self.label_verif = QtGui.QLabel(self.groupBox)
        self.label_verif.setObjectName("label_verif")
        self.gridLayout.addWidget(self.label_verif, 5, 0, 1, 1)
        self.comboBox_tipo = QtGui.QComboBox(self.groupBox)
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.gridLayout.addWidget(self.comboBox_tipo, 7, 1, 1, 1)
        self.lineEdit_rut = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_rut.setObjectName("lineEdit_rut")
        self.gridLayout.addWidget(self.lineEdit_rut, 6, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_error_tipo = QtGui.QLabel(self.groupBox)
        self.label_error_tipo.setObjectName("label_error_tipo")
        self.gridLayout.addWidget(self.label_error_tipo, 7, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_cambiar_c = QtGui.QLabel(self.groupBox)
        self.label_cambiar_c.setText("")
        self.label_cambiar_c.setObjectName("label_cambiar_c")
        self.gridLayout.addWidget(self.label_cambiar_c, 2, 0, 1, 1)
        self.lineEdit_nombre = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.gridLayout.addWidget(self.lineEdit_nombre, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_apellido = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.gridLayout.addWidget(self.lineEdit_apellido, 1, 1, 1, 1)
        self.label_error_nombre = QtGui.QLabel(self.groupBox)
        self.label_error_nombre.setObjectName("label_error_nombre")
        self.gridLayout.addWidget(self.label_error_nombre, 0, 2, 1, 1)
        self.lineEdit_clave_actual = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_clave_actual.setObjectName("lineEdit_clave_actual")
        self.gridLayout.addWidget(self.lineEdit_clave_actual, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_cambiar_c = QtGui.QPushButton(self.groupBox)
        self.pushButton_cambiar_c.setObjectName("pushButton_cambiar_c")
        self.gridLayout.addWidget(self.pushButton_cambiar_c, 2, 1, 1, 1)
        self.label_clave_actual = QtGui.QLabel(self.groupBox)
        self.label_clave_actual.setObjectName("label_clave_actual")
        self.gridLayout.addWidget(self.label_clave_actual, 3, 0, 1, 1)
        self.label_error_apellido = QtGui.QLabel(self.groupBox)
        self.label_error_apellido.setObjectName("label_error_apellido")
        self.gridLayout.addWidget(self.label_error_apellido, 1, 2, 1, 1)
        self.label_error_verif = QtGui.QLabel(self.groupBox)
        self.label_error_verif.setText("")
        self.label_error_verif.setObjectName("label_error_verif")
        self.gridLayout.addWidget(self.label_error_verif, 5, 2, 1, 1)
        self.label_error_rut = QtGui.QLabel(self.groupBox)
        self.label_error_rut.setText("")
        self.label_error_rut.setObjectName("label_error_rut")
        self.gridLayout.addWidget(self.label_error_rut, 6, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
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
        self.label_clave.setText(QtGui.QApplication.translate("FormularioUsuario", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label_verif.setText(QtGui.QApplication.translate("FormularioUsuario", "Repita contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FormularioUsuario", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_tipo.setText(QtGui.QApplication.translate("FormularioUsuario", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Debe seleccionar un tipo</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormularioUsuario", "Rut", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormularioUsuario", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_nombre.setText(QtGui.QApplication.translate("FormularioUsuario", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Debe tener sólo letras</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormularioUsuario", "Apellido", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cambiar_c.setText(QtGui.QApplication.translate("FormularioUsuario", "Cambiar Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.label_clave_actual.setText(QtGui.QApplication.translate("FormularioUsuario", "Contraseña actual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_error_apellido.setText(QtGui.QApplication.translate("FormularioUsuario", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">Debe tener sólo letras</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

