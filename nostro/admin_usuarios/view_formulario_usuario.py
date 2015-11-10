#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_usuario
import controller_admin_user
import cryptoraf as c


class FormularioUsuario(QtGui.QDialog):

    is_diferent_pass = False
    reloadT = QtCore.Signal()
    identificador = False
    __type_users__ = ((u"Administrador"),
                      (u"Garzón"))

    def __init__(self, id=None):
        super(FormularioUsuario, self).__init__()
        self.ui = formulario_usuario.Ui_FormularioUsuario()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.setModal(True)
        self.show()
        self.ui.lineEdit_clave.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.lineEdit_verif.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.lineEdit_clave_actual.setEchoMode(QtGui.QLineEdit.Password)
        self.connect_actions()
        for num, name in enumerate(self.__type_users__):
            self.ui.comboBox_tipo.addItem(name, num)
        if(id == None):
            self.id = 0
            self.identificador = False
            self.setWindowTitle("Nuevo Usuario")
            self.show()
            self.ui.pushButton_cambiar_c.setVisible(False)
            self.ui.label_cambiar_c.setVisible(False)
        else:
            self.id = id
            self.identificador = True
            self.setWindowTitle("Editar Usuario")
            usuario = controller_admin_user.getUsuarioId(id)
            for row in usuario:
                self.nombre = row[1]
                self.ui.lineEdit_nombre.setText(self.nombre)
                self.apellido = row[2]
                self.ui.lineEdit_apellido.setText(self.apellido)
                self.rut = row[3]
                self.ui.lineEdit_rut.setText(self.rut)
                self.password = row[4]
                self.tipo = row[5]
                self.ui.comboBox_tipo.setCurrentIndex(int(self.tipo))
            self.ui.lineEdit_verif.setVisible(False)
            self.ui.label_verif.setVisible(False)
            self.ui.lineEdit_clave.setVisible(False)
            self.ui.label_clave.setVisible(False)
        self.ui.label_clave_actual.setVisible(False)
        self.ui.lineEdit_clave_actual.setVisible(False)

    def connect_actions(self):
        self.ui.pushButton_cambiar_c.clicked.connect(self.action_cambiar_c)

    def action_cambiar_c(self):
        self.ui.label_clave_actual.setVisible(True)
        self.ui.lineEdit_clave_actual.setVisible(True)
        self.ui.lineEdit_verif.setVisible(True)
        self.ui.label_verif.setVisible(True)
        self.ui.lineEdit_clave.setVisible(True)
        self.ui.label_clave.setVisible(True)
        self.ui.label_clave.setText(u"Contraseña nueva")
        self.ui.label_verif.setText(u"Repita contraseña nueva")
        self.is_diferent_pass = True

    def accept(self):
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.apellido = unicode(self.ui.lineEdit_apellido.text())
        self.rut = self.ui.lineEdit_rut.text()
        self.clave = unicode(self.ui.lineEdit_clave.text())
        self.verif = unicode(self.ui.lineEdit_verif.text())
        self.tipo = int(self.ui.comboBox_tipo.currentIndex())
        self.status = 1
        if(self.identificador):  # Editar Usuario
            if(not self.is_diferent_pass): # No Cambió Password
                self.clave = None
                controller_admin_user.UpdateDataUsuario(
                    self.id, self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
                self.setVisible(False)
            else:
                self.clave_ac = unicode(self.ui.lineEdit_clave_actual.text())
                crypt = c.CryptoRAF()
                clave_ingresada = crypt.encrypt(
                    self.clave_ac, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
                usuario = controller_admin_user.getUsuarioId(self.id)
                clave_real = usuario[0][4]
                if( clave_ingresada == clave_real):
                    if ( self.verif == self.clave):
                        controller_admin_user.UpdateDataUsuario(
                            self.id, self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
                        self.setVisible(False)
                    else:
                        self.errorMessageDialog = QtGui.QErrorMessage(self)
                        self.errorMessageDialog.setWindowTitle("ERROR")
                        self.errorMessageDialog.showMessage(
                            u"Las contraseñas (nueva) no coinciden")
                else:
                    self.errorMessageDialog = QtGui.QErrorMessage(self)
                    self.errorMessageDialog.setWindowTitle("ERROR")
                    self.errorMessageDialog.showMessage(
                        u"La contraseña actual no coincide con la ingresada")

        else:
            if self.verif == self.clave:
                controller_admin_user.AddDataUsuario(
                    self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
                self.setVisible(False)
            else:
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.setWindowTitle("ERROR")
                self.errorMessageDialog.showMessage(
                    u"Las contraseñas no coinciden")
        self.reloadT.emit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioUsuario()
    sys.exit(app.exec_())
