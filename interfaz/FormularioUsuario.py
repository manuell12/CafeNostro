# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import FormularioUsuario_ui
import controller_admin_user

class FormularioUsuario(QtGui.QDialog):
	reloadT = QtCore.Signal()
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
				self.nombre = row['nombre']
				self.ui.lineEdit_nombre.setText(self.nombre)
				self.apellido = row['apellido']
				self.ui.lineEdit_apellido.setText(self.apellido)
				self.rut = row['rut']
				self.ui.lineEdit_rut.setText(self.rut)
				self.tipo = row['tipo']
				self.ui.lineEdit_tipo.setText(self.tipo)
				self.status = row['status']
				self.ui.lineEdit_status.setText(self.status)

	def connect_actions(self):
		self.accept.connect(self.action_btn_aceptar)
	def action_btn_aceptar(self):
		self.nombre = str(self.ui.lineEdit_nombre.text())
		self.apellido = str(self.ui.lineEdit_apellido.text())
		self.rut = str(self.ui.lineEdit_rut.text())
		self.clave = str(self.ui.lineEdit_clave.text())
		self.tipo = str(self.ui.lineEdit_tipo.text())
		self.status = str(self.ui.lineEdit_apellido.status())
		if(identificador):
			controller_admin_user.AddDataUsuario(self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
		else:
			controller_admin_user.UpdateDataUsuario(self.id, self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
		self.reloadT.emit()

def run():
	app = QtGui.QApplication(sys.argv)
	main = FormularioUsuario()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
