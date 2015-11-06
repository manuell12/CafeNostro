# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Nov 05 15:06:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(228, 145)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 197, 107))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_5)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_user = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_user)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_pass = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_pass)
        self.pushButton_login = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_login.setObjectName("pushButton_login")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_login)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Cafe Nostro", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_login.setText(QtGui.QApplication.translate("Form", "Ingresar", None, QtGui.QApplication.UnicodeUTF8))

