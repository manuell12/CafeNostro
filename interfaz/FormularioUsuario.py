# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import FormularioUsuario_ui
import controller_admin_user

class FormularioUsuario(QtGui.QDialog):
	identificador = False
	def __init__(self, id=None):
		super(FormularioUsuario, self).__init__()
		self.ui = FormularioUsuario_ui.Ui_Dialog()
		self.ui.setupUi(self)
		self.show()
		if(id==None):
			self.id=0
			self.identificador = False
			self.setWindowTitle("Nuevo Usuario")
			self.show()
		else:
			self.id=id
			self.identificador = True
			self.setWindowTitle("Editar Usuario")
			usuario = controller_admin_user.getUsuarioId(id)
			for row in usuario:
				self.ui.lineEdit_nombre.setText(row['nombre'])
				self.ui.lineEdit_apellido.setText(row['apellido'])
				self.ui.lineEdit_rut.setText(row['rut'])
				self.ui.lineEdit_clave.setEnabled(False)

def run():
	app = QtGui.QApplication(sys.argv)
	main = FormularioUsuario()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
