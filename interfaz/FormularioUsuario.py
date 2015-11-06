# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import FormularioUsuario_ui
import controller_admin_user

class FormularioUsuario(QtGui.QDialog):
	reloadT = QtCore.Signal()
	identificador = False
	__type_users__ = (
		(u"Administrador"),
		(u"Garzón")
	)
	def __init__(self, id=None):
		super(FormularioUsuario, self).__init__()
		self.ui = FormularioUsuario_ui.Ui_FormularioUsuario()
		self.ui.setupUi(self)
		self.show()
		for num,name in enumerate(self.__type_users__):
			self.ui.comboBox_tipo.addItem(name, num)
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
				self.nombre = row[1]
				self.ui.lineEdit_nombre.setText(self.nombre)
				self.apellido = row[2]
				self.ui.lineEdit_apellido.setText(self.apellido)
				self.rut = row[3]
				self.ui.lineEdit_rut.setText(self.rut)
				self.tipo = row[5]
				self.ui.comboBox_tipo.setCurrentIndex(int(self.tipo))

	def accept(self):
		self.nombre = str(self.ui.lineEdit_nombre.text())
		self.apellido = str(self.ui.lineEdit_apellido.text())
		self.rut = str(self.ui.lineEdit_rut.text())
		self.clave = str(self.ui.lineEdit_clave.text())
		self.tipo = int(self.ui.comboBox_tipo.currentIndex())
		self.status = None
		if(self.identificador):
			controller_admin_user.UpdateDataUsuario(self.id, self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
			self.setVisible(False)
		else:
			controller_admin_user.AddDataUsuario(self.nombre, self.apellido, self.rut, self.clave, self.tipo, self.status)
			self.setVisible(False)
		self.reloadT.emit()

def run():
	app = QtGui.QApplication(sys.argv)
	main = FormularioUsuario()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
