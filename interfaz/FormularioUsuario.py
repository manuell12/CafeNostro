# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from FormularioUsuario_ui import Ui_FormularioUsuario

class FormularioUsuario(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui = Ui_FormularioUsuario()
		self.ui.setupUi(self)
		self.show()

def run():
	app = QtGui.QApplication(sys.argv)
	main = FormularioUsuario()
	sys.exit(app.exec_())

if __name__ == '__main__':
	run()
