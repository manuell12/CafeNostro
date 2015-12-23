#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_usuario
import controller_admin_user
import cryptoraf as c


class FormularioUsuario(QtGui.QDialog):
    """
    Clase FormularioUsuario que permite al usuario del programa 
    ingresar datos tanto para un crear nuevo usuario como para modificar
    un usuario existente.
    """
    is_diferent_pass = False
    reloadT = QtCore.Signal()
    identificador = False
    __type_users__ = ((u"-----"),
                      (u"Administrador"),
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
                self.nombre = row.nombre
                self.ui.lineEdit_nombre.setText((self.nombre))
                self.apellido = (row.apellido)            
                self.ui.lineEdit_apellido.setText((self.apellido))
                self.rut = row.rut
                self.ui.lineEdit_rut.setText(self.rut)
                self.password = row.clave
                self.tipo = row.tipo
                self.ui.comboBox_tipo.setCurrentIndex(int(self.tipo)+1)
            self.ui.lineEdit_verif.setVisible(False)
            self.ui.label_verif.setVisible(False)
            self.ui.label_error_verif.setVisible(False)
            self.ui.lineEdit_clave.setVisible(False)
            self.ui.label_clave.setVisible(False)
            self.ui.label_error_clave.setVisible(False)
        self.ui.label_clave_actual.setVisible(False)
        self.ui.lineEdit_clave_actual.setVisible(False)
        self.ui.label_error_clave_actual.setVisible(False)

    def connect_actions(self):
        """
        Método que conecta los slots de los widgets de la interfaz grafica 
        con las funciones de FormularioProducto.
        """
        self.ui.pushButton_cambiar_c.clicked.connect(self.action_cambiar_c)

        self.ui.lineEdit_nombre.textChanged.connect(
            self.lineEdit_nombre_changed)
        self.ui.lineEdit_apellido.textChanged.connect(
            self.lineEdit_apellido_changed)
        self.ui.lineEdit_rut.textChanged.connect(
            self.lineEdit_rut_changed)
        self.ui.lineEdit_verif.textChanged.connect(
            self.lineEdit_pass_changed)
        self.ui.lineEdit_clave.textChanged.connect(
            self.lineEdit_pass_changed)
        self.ui.lineEdit_clave_actual.textChanged.connect(
            self.lineEdit_clave_actual_changed)
        self.ui.comboBox_tipo.currentIndexChanged.connect(
            self.comboBox_tipo_changed)

    def lineEdit_nombre_changed(self,text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_nombre'. Valida que el campo esté correctamente escrito.
        """
        controller_admin_user.validarNombreF(self.ui.label_error_nombre,text)

    def lineEdit_apellido_changed(self,text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_apellido'. Valida que el campo esté correctamente escrito.
        """
        controller_admin_user.validarApellidoF(self.ui.label_error_apellido,text)

    def lineEdit_rut_changed(self,text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_rut'. Valida que el campo esté correctamente escrito.
        """
        controller_admin_user.validarRutF(self.ui.label_error_rut,text)

    def lineEdit_pass_changed(self,text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_clave'. Valida que el campo esté correctamente escrito.
        """
        self.clave = unicode(self.ui.lineEdit_clave.text())
        self.verif = unicode(self.ui.lineEdit_verif.text())
        if(self.clave == self.verif):
            self.ui.label_error_verif.setText(
                u"<font color='green'><b>Contraseñas coinciden.</b></font>")
        else:
            self.ui.label_error_verif.setText(
                u"<font color='red'><b>Contraseñas no coinciden.</b></font>")

    def lineEdit_clave_actual_changed(self,text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_clave_actual'. Valida que el campo esté correctamente escrito.
        """
        self.clave_ac = unicode(self.ui.lineEdit_clave_actual.text())
        cr = c.CryptoRAF()
        clave_ingresada = cr.encrypt(
            self.clave_ac, "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
        usuario = controller_admin_user.getUsuarioId(self.id)
        clave_real = usuario[0].clave
        if(clave_ingresada == clave_real):
            self.ui.label_error_clave_actual.setText(
        u"<font color='green'><b>Contraseña ingresada correcta.</b></font>")
        else:
            self.ui.label_error_clave_actual.setText(
        u"<font color='red'><b>Contraseña ingresada incorrecta.</b></font>")

    def comboBox_tipo_changed(self,index):
        """
        Método que es llamado cuando el usuario cambia la seleccion 
        del QComboBox 'comboBox_tipo'. 
        Valida que el campo esté correctamente escrito.
        """
        if(index != 0):
            self.ui.label_error_tipo.setText(
                u"<font color='green'><b>Seleccion correcta.</b></font>")
        else:
            self.ui.label_error_tipo.setText(
                u"<font color='red'><b>Debe seleccionar un tipo.</b></font>")

    def action_cambiar_c(self):
        """
        Método que realiza los cambios gráficos necesarios para informar
        al usuario que puede cambiar la contraseña.
        """
        self.ui.label_clave_actual.setVisible(True)
        self.ui.lineEdit_clave_actual.setVisible(True)
        self.ui.label_error_clave_actual.setVisible(True)
        self.ui.lineEdit_verif.setVisible(True)
        self.ui.label_verif.setVisible(True)
        self.ui.label_error_verif.setVisible(True)
        self.ui.lineEdit_clave.setVisible(True)
        self.ui.label_clave.setVisible(True)
        self.ui.label_error_clave.setVisible(True)
        self.ui.pushButton_cambiar_c.setVisible(False)
        self.ui.label_cambiar_c.setVisible(False)
        self.ui.label_clave.setText(u"Contraseña nueva")
        self.ui.label_verif.setText(u"Repita contraseña nueva")
        self.is_diferent_pass = True

    def accept(self):
        """
        Método que es llamado cuando el usuario presiona en el boton 'OK'.
        Guarda los cambios realizados sobre un usuario existente o
        crea un nuevo usuario con los datos ingresados.
        """
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.apellido = unicode(self.ui.lineEdit_apellido.text())
        self.rut = self.ui.lineEdit_rut.text()
        self.clave = unicode(self.ui.lineEdit_clave.text())
        self.verif = unicode(self.ui.lineEdit_verif.text())
        self.tipo = int(self.ui.comboBox_tipo.currentIndex()-1)
        self.valido = False
        if(self.tipo == -1):
            self.valido = False
        self.status = 1
        if(self.identificador):  # Editar Usuario
            if(not self.is_diferent_pass): # No Cambió Password
                self.clave = None
                self.valido = controller_admin_user.validarDatos(
                    self.ui.label_error_nombre.text(),
                    self.ui.label_error_apellido.text(),
                    self.ui.label_error_rut.text(),
                    None,
                    None,
                    self.ui.label_error_tipo.text())
                if(self.valido):
                    controller_admin_user.UpdateDataUsuario(
                        self.id, 
                        self.nombre, 
                        self.apellido, 
                        self.rut, 
                        self.clave, 
                        self.tipo, 
                        self.status)
                    msgBox = QtGui.QMessageBox()
                    msgBox.setWindowTitle("Correcto")
                    msgBox.setText("Usuario editado correctamente.")
                    msgBox.exec_()
                    self.setVisible(False)
                else:
                    msgBox = QtGui.QMessageBox()
                    msgBox.setIcon(QtGui.QMessageBox.Critical)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Revise los campos obligatorios.")
                    msgBox.exec_()
            else:
                self.clave_ac = unicode(self.ui.lineEdit_clave_actual.text())
                crypt = c.CryptoRAF()
                clave_ingresada = crypt.encrypt(
                    self.clave_ac, 
                    "fhfs8sdfkjshuif7yr4021934234233ihsidf89sssx")
                usuario = controller_admin_user.getUsuarioId(self.id)
                clave_real = usuario[0].clave
                if( clave_ingresada == clave_real):
                    if ( self.verif == self.clave):
                        self.valido = controller_admin_user.validarDatos(
                            self.ui.label_error_nombre.text(),
                            self.ui.label_error_apellido.text(),
                            self.ui.label_error_rut.text(),
                            self.ui.label_error_verif.text(),
                            self.ui.label_error_clave_actual.text(),
                            self.ui.label_error_tipo.text())
                        if(self.valido):
                            controller_admin_user.UpdateDataUsuario(
                                self.id, 
                                self.nombre, 
                                self.apellido, 
                                self.rut, 
                                self.clave, 
                                self.tipo, 
                                self.status)
                            msgBox = QtGui.QMessageBox()
                            msgBox.setWindowTitle("Correcto")
                            msgBox.setText("Usuario editado correctamente.")
                            msgBox.exec_()
                            self.setVisible(False)
                        else:
                            msgBox = QtGui.QMessageBox()
                            msgBox.setIcon(QtGui.QMessageBox.Critical)
                            msgBox.setWindowTitle("Error")
                            msgBox.setText("Revise los campos obligatorios.")
                            msgBox.exec_()
        else:
            if self.verif == self.clave:
                self.valido = controller_admin_user.validarDatos(
                    self.ui.label_error_nombre.text(),
                    self.ui.label_error_apellido.text(),
                    self.ui.label_error_rut.text(),
                    self.ui.label_error_verif.text(),
                    None,
                    self.ui.label_error_tipo.text())
                if(self.valido):
                    controller_admin_user.AddDataUsuario(
                        self.nombre, 
                        self.apellido, 
                        self.rut, 
                        self.clave, 
                        self.tipo, 
                        self.status)
                    msgBox = QtGui.QMessageBox()
                    msgBox.setWindowTitle("Correcto")
                    msgBox.setText("Usuario creado correctamente.")
                    msgBox.exec_()
                    self.setVisible(False)
        self.reloadT.emit()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioUsuario()
    sys.exit(app.exec_())
