# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\admin_users.ui'
#
# Created: Fri Nov 13 23:42:50 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AdminUsers(object):
    def setupUi(self, AdminUsers):
        AdminUsers.setObjectName("AdminUsers")
        AdminUsers.resize(612, 407)
        self.verticalLayout = QtGui.QVBoxLayout(AdminUsers)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(AdminUsers)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableUsers = QtGui.QTableView(AdminUsers)
        self.tableUsers.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.tableUsers.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableUsers.setTabKeyNavigation(False)
        self.tableUsers.setProperty("showDropIndicator", False)
        self.tableUsers.setDragDropOverwriteMode(False)
        self.tableUsers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.horizontalHeader().setMinimumSectionSize(20)
        self.verticalLayout.addWidget(self.tableUsers)
        self.frame = QtGui.QFrame(AdminUsers)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nuevo_button = QtGui.QPushButton(self.frame)
        self.nuevo_button.setObjectName("nuevo_button")
        self.horizontalLayout.addWidget(self.nuevo_button)
        self.editar_button = QtGui.QPushButton(self.frame)
        self.editar_button.setObjectName("editar_button")
        self.horizontalLayout.addWidget(self.editar_button)
        self.eliminar_button = QtGui.QPushButton(self.frame)
        self.eliminar_button.setObjectName("eliminar_button")
        self.horizontalLayout.addWidget(self.eliminar_button)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(AdminUsers)
        QtCore.QMetaObject.connectSlotsByName(AdminUsers)

    def retranslateUi(self, AdminUsers):
        AdminUsers.setWindowTitle(QtGui.QApplication.translate("AdminUsers", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AdminUsers", "Usuarios registrados", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevo_button.setText(QtGui.QApplication.translate("AdminUsers", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.editar_button.setText(QtGui.QApplication.translate("AdminUsers", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_button.setText(QtGui.QApplication.translate("AdminUsers", "E&liminar", None, QtGui.QApplication.UnicodeUTF8))

