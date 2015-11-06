#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Café Nostro.
Archivo de la vista principal que concentra practicamente todas las funcionalidades.
"""
from PySide import QtCore, QtGui
from admin_user import Ui_AdminUsers
import controller_admin_user
import sys
import FormularioUsuario


class AdminUsers(QtGui.QDialog):

	__header_table__ = (
		(u"ID",20),
		(u"Nombres", 200),
		(u"Apellidos", 200),
		(u"Rut", 120),
		(u"Tipo", 100)
	)

	__type_users__ = (
		(u"Administrador"),
		(u"Garzón")
	)

	def __init__(self):
		"""Constructor de la clase"""
		super(AdminUsers, self).__init__()
		self.ui = Ui_AdminUsers()
		self.ui.setupUi(self)
		self.ui.tableUsers.verticalHeader().setVisible(False)
		self.set_model_table()
		self.set_source_model(self.load_users(self))
		self.connect_actions()
		self.ui.tableUsers.setColumnHidden(0,True)
		self.show()


	def connect_actions(self):
		"""conectar botones con su respectiva accion"""
		self.ui.editar_button.clicked.connect(self.action_btn_editar)
		self.ui.nuevo_button.clicked.connect(self.action_btn_nuevo)

	def reload_data_table(self):
		self.set_source_model(self.load_users(self))

	def action_btn_nuevo(self):
		"""Metodo para lanzar el formulario de creacion del nuevo usuario"""
		self.nuevoUsuarioWindow = FormularioUsuario.FormularioUsuario()
		self.nuevoUsuarioWindow.reloadT.connect(self.reload_data_table)
		self.nuevoUsuarioWindow.exec_()

	def action_btn_editar(self):
		index = self.ui.tableUsers.currentIndex()
		if index.row() == -1: #No se ha seleccionado producto
			msgBox = QtGui.QMessageBox()
			msgBox.setWindowTitle("Error")
			msgBox.setText("Debe seleccionar un usuario.")
			msgBox.exec_()
			return False
		else:
			self.editUsuarioWindow = FormularioUsuario.FormularioUsuario(self.id)
			self.editUsuarioWindow.reloadT.connect(self.reload_data_table)
			self.editUsuarioWindow.exec_()

	def load_users(self, parent):
		"""
		Carga la información de la base de datos en la tabla.
		Obtiene desde la base de datos a traves del controlador
		la información completa de la tabla.
		Crea un model para adjuntar los datos a la grilla y luego
		lo retorna para utilizarlo en setSourceModel.
		"""
		self.typeModelClass = parent

		usuarios = controller_admin_user.usuarios()
		row = len(usuarios)

		model = QtGui.QStandardItemModel(row, len(self.__header_table__))
		#model = QtGui.QStandardItemModel(row, len(self.headerTabla), parent)

		for i, data in enumerate(usuarios):
			row = [data[0], data[1], data[2], data[3], data[5]]
			for j, field in enumerate(row):
				index = model.index(i, j, QtCore.QModelIndex())
				if j is 4:
					# print self.__type_users__[field]
					model.setData(index, self.__type_users__[field])
				else:
					model.setData(index, field)

		modelSel = self.ui.tableUsers.selectionModel()
		modelSel.currentChanged.connect(self.tabla_cell_selected)

		return model

	def tabla_cell_selected(self,index,indexp):
		model = self.ui.tableUsers.model()
		index = self.ui.tableUsers.currentIndex()
		self.id = model.index(index.row(), 0, QtCore.QModelIndex()).data()


	def set_model_table(self):
		"""Define el módelo de la grilla para trabajarla."""
		self.proxyModel = QtGui.QSortFilterProxyModel()
		self.proxyModel.setDynamicSortFilter(True)

		self.ui.tableUsers.setModel(self.proxyModel)

	def set_source_model(self, model):
		"""
		Actualiza constantemente el origen de los datos para siempre tenerlos
		al día así pudiendo buscar y mostrar solo algunos datos.
		Además llama a las funciones que rellenan los comboBox de filtrado y
		asigna el tamaño de las columnas a las grillas respectivas.
		"""
		self.proxyModel.setSourceModel(model)

		# Designamos los header de la grilla y sus respectivos anchos
		for col, h in enumerate(self.__header_table__):
			model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
			self.ui.tableUsers.setColumnWidth(col, h[1])

		self.ui.tableUsers.sortByColumn(0, QtCore.Qt.AscendingOrder)
