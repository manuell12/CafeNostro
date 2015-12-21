# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Dec 19 04:44:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(343, 349)
        Dialog.setMinimumSize(QtCore.QSize(343, 349))
        Dialog.setMouseTracking(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_pass = QtGui.QLineEdit(Dialog)
        self.lineEdit_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_pass)
        self.pushButton_login = QtGui.QPushButton(Dialog)
        self.pushButton_login.setObjectName("pushButton_login")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButton_login)
        self.lineEdit_user = QtGui.QLineEdit(Dialog)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_usuario = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(14)
        self.label_usuario.setFont(font)
        self.label_usuario.setObjectName("label_usuario")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_usuario)
        self.label_pass = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(12)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_pass)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem4)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_salir = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_salir.sizePolicy().hasHeightForWidth())
        self.pushButton_salir.setSizePolicy(sizePolicy)
        self.pushButton_salir.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_salir.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_salir.setObjectName("pushButton_salir")
        self.verticalLayout.addWidget(self.pushButton_salir)
        self.gridLayout.addLayout(self.verticalLayout, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_salir, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_user, self.lineEdit_pass)
        Dialog.setTabOrder(self.lineEdit_pass, self.pushButton_login)
        Dialog.setTabOrder(self.pushButton_login, self.pushButton_salir)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Cafe Nostro", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_login.setText(QtGui.QApplication.translate("Dialog", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_usuario.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Usuario</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pass.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Contraseña</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_salir.setText(QtGui.QApplication.translate("Dialog", "Salir", None, QtGui.QApplication.UnicodeUTF8))

