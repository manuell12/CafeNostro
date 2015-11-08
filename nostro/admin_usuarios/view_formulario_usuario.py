#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_usuario
import controller_admin_user


class FormularioUsuario(QtGui.QDialog):

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
        for num, name in enumerate(self.__type_users__):
            self.ui.comboBox_tipo.addItem(name, num)
        if(id == None):
            self.id = 0
            self.identificador = False
            self.setWindowTitle("Nuevo Usuario")
            self.show()
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
                self.ui.lineEdit_clave.setEnabled(False)

    def accept(self):
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.apellido = unicode(self.ui.lineEdit_apellido.text())
        self.rut = self.ui.lineEdit_rut.text()
        self.clave = unicode(self.ui.lineEdit_clave.text())
        self.verif = unicode(self.ui.lineEdit_verif.text())
        self.tipo = int(self.ui.comboBox_tipo.currentIndex())
        self.status = None
        if(self.identificador):  # Editar Usuario
            controller_admin_user.UpdateDataUsuario(
                self.id, self.nombre, self.apellido, self.rut, self.password, self.tipo, self.status)
            self.setVisible(False)
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
