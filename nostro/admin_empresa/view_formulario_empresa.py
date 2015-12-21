#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_empresa
import controller_empresa


class FormularioEmpresa(QtGui.QDialog):

    def __init__(self,vista_mesas):
        super(FormularioEmpresa, self).__init__()
        self.ui = formulario_empresa.Ui_FormularioEmpresa()
        self.ui.setupUi(self)
        self.connect_actions()
        self.load_data()

        self.vista_mesas = vista_mesas
        self.ui.lineEdit_fono.setInputMask("999 9 999999")
        self.ui.lineEdit_nombre.setFocus()

    def load_data(self):
        empresa = controller_empresa.getEmpresa(1)[0]
        self.ui.lineEdit_nombre.setText(empresa.nombre)
        self.ui.lineEdit_rut.setText(empresa.rut)
        self.ui.lineEdit_direccion.setText(empresa.direccion)
        self.ui.lineEdit_ciudad.setText(empresa.ciudad)
        self.ui.lineEdit_giro.setText(empresa.giro)
        self.ui.lineEdit_fono.setText(empresa.fono)
        self.ui.lineEdit_email.setText(empresa.email)
        self.ui.spinBox_num_mesas.setValue(int(empresa.num_mesas))

    def connect_actions(self):
        """
        Método que conecta los slots de los widgets de la interfaz grafica con las funciones de FormularioProducto
        """
        self.ui.lineEdit_nombre.textChanged.connect(
            self.lineEdit_nombre_changed)
        self.ui.lineEdit_direccion.textChanged.connect(
            self.lineEdit_direccion_changed)
        self.ui.lineEdit_ciudad.textChanged.connect(
            self.lineEdit_ciudad_changed)
        self.ui.lineEdit_giro.textChanged.connect(
            self.lineEdit_giro_changed)

        self.ui.pushButton_guardar.pressed.connect(self.accept)

    def lineEdit_nombre_changed(self, text):
        controller_empresa.validarNombreF(
            self.ui.label_error_nombre, text)

    def lineEdit_direccion_changed(self, text):
        controller_empresa.validarDireccionF(
            self.ui.label_error_direccion, text)

    def lineEdit_ciudad_changed(self, text):
        controller_empresa.validarCiudadF(
            self.ui.label_error_ciudad, text)

    def lineEdit_giro_changed(self, text):
        controller_empresa.validarGiroF(
            self.ui.label_error_giro, text)

    def accept(self):
        nombre = unicode(self.ui.lineEdit_nombre.text())
        rut = unicode(self.ui.lineEdit_rut.text())
        direccion = unicode(self.ui.lineEdit_direccion.text())
        ciudad = unicode(self.ui.lineEdit_ciudad.text())
        giro = unicode(self.ui.lineEdit_giro.text())
        fono = unicode(self.ui.lineEdit_fono.text())
        email = unicode(self.ui.lineEdit_email.text())
        num_mesas = int(self.ui.spinBox_num_mesas.value())

        validar = controller_empresa.validarDatos(
            self.ui.label_error_nombre.text(),
            self.ui.label_error_direccion.text(),
            self.ui.label_error_ciudad.text(),
            self.ui.label_error_giro.text())
        if(validar):
            controller_empresa.updateDataEmpresa(
                nombre,rut,direccion,ciudad,giro,fono,email,num_mesas)
            self.vista_mesas.update_buttons()
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle("Correcto")
            msgBox.setText(u"Datos guardados correctamente. \n\nDebe reiniciar la aplicacion para que los cambios surgan efecto.")
            msgBox.exec_()
            self.setVisible(False)
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Critical)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Revise los campos obligatorios.")
            msgBox.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioEmpresa()
    sys.exit(app.exec_())
