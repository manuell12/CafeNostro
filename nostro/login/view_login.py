#!/usr/bin/python
# encoding: utf-8
"""
Muestra la ventana de login para identificarse en el sistema.
"""
import sys
from PySide import QtCore, QtGui
from mainwindow_login import Ui_Dialog
from main_window.view_main_window import MainWindow
import controller_login
import model_login


class Login(QtGui.QDialog):

    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)

        self.setSignals()
        self.centerWindow()
        self.show()

    def centerWindow(self):
        'Funcion que centra la interfaz grafica en la pantalla del usuario.'
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setSignals(self):
        'Señales (listenner) de los elementos del formulario'
        self.ui.pushButton_login.clicked.connect(self.loginAdmin)

    def loginAdmin(self):
        'Metodo que ingresa un usuario'
        # validamos los campos
        valido = self.ui.lineEdit_user.text().lstrip()
        valido1 = self.ui.lineEdit_pass.text().lstrip()
        if(len(valido) is 0 or len(valido1) is 0):
            self.errorMessage(u"""Revise los campos obligatorios.""")
        else:
            mensaje = controller_login.obtenerUsuario(
                self.ui.lineEdit_user.text(), self.ui.lineEdit_pass.text())
            if mensaje is None:
                self.errorMessage(u"""Error inesperado, intente nuevamente.""")
            else:
                if mensaje == True:
                    # self.correctMessage(u"""Ingreso valido""")
                    self.close()
                    self.main = MainWindow(controller_login.obtenerTipoUsuario(
                        self.ui.lineEdit_user.text())[0][0],self.ui.lineEdit_user.text())
                    self.main.show()
                    # self.hide()
                    # self.setVisible(False)
                else:
                    self.errorMessage(u"Ingreso no valido")
            # self.reject()

    def errorMessage(self, message):
        """Función que despliega un mensaje de error.
        @param message"""
        QtGui.QMessageBox.warning(
            self,
            u"ERROR!",
            message)

    def correctMessage(self, message):
        """Función que despliega un mensaje de operacion correcta.
        @param message"""
        QtGui.QMessageBox.information(
            self,
            u"Operacion correcta",
            message)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Login()
    sys.exit(app.exec_())
