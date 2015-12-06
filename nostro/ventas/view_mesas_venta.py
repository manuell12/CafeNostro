#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from mesas_venta import Ui_MesasVenta
from ventas.view_formulario_venta import FormularioVenta
import ventas.controller_venta as controller_venta


class MesasVenta(QtGui.QWidget):

    def __init__(self,main,num_mesas,rut):
        'Constructor de la clase'
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MesasVenta()
        self.ui.setupUi(self)
        self.setFocus()
        self.main = main
        self.num_mesas = num_mesas
        self.rut = rut
        self.create_buttons()
        self.connect_signals()

    def connect_signals(self):
        self.ui.pushButton_agregar.clicked.connect(self.agregar_mesa)

    def agregar_mesa(self):
        num_mesa = len(self.list_mesas)+1
        
        pushButton_mesa = QtGui.QPushButton("Mesa "+str(num_mesa))
        pushButton_mesa.setMinimumSize(QtCore.QSize(100, 60))
        pushButton_mesa.clicked.connect(self.button_pressed)
        self.list_mesas.append(pushButton_mesa)

        self.ui.gridLayout_mesas.addWidget(pushButton_mesa,self.row,self.column)
        self.main.stackedWidget.addWidget(FormularioVenta(self.main,self.rut,num_mesa))
        self.column = self.column + 1
        if(num_mesa % 7 == 0):
            self.column = 0
            self.row = self.row +1

    def create_buttons(self):
        self.list_mesas = list()
        self.row = 0
        self.column = 0
        for mesa in range(self.num_mesas+1):
            if (mesa != 0):
                if (mesa < 10):
                    pushButton_mesa = QtGui.QPushButton("Mesa 0"+str(mesa))
                else:
                    pushButton_mesa = QtGui.QPushButton("Mesa "+str(mesa))

                self.list_mesas.append(pushButton_mesa)

                pushButton_mesa.setMinimumSize(QtCore.QSize(100, 60))
                pushButton_mesa.clicked.connect(self.button_pressed)
                self.ui.gridLayout_mesas.addWidget(pushButton_mesa,self.row,self.column)
                self.column = self.column + 1
            if (mesa % 7 == 0):
                self.row = self.row + 1
                self.column = 0

    def button_pressed(self):
        button_mesa = self.sender()
        num_mesa = int(button_mesa.text()[-2:])
        print str(num_mesa)
        self.main.stackedWidget.setCurrentIndex(num_mesa+6)