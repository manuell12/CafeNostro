#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Café Nostro.
Archivo de la vista principal que concentra practicamente todas las 
funcionalidades.
"""
import sys
from PySide import QtCore, QtGui
from main_window import Ui_MainWindow
from admin_usuarios.view_admin_user import AdminUsers
from admin_productos.view_admin_producto import AdminProductos
from ventas.view_admin_venta import AdminVentas
from ventas.view_formulario_venta import FormularioVenta
from ventas.view_mesas_venta import MesasVenta
import ventas.controller_venta as controller_venta
import admin_usuarios.controller_admin_user as controller
from estadisticas.view_estadistica import Estadistica


class MainWindow(QtGui.QMainWindow):
    """
    Clase de la ventana principal.
    El widget central (centralWidget) de la ventana ira cambiando
    respecto a que es lo que el usuario desea hacer.
    """

    venta_directa_en_curso = False
    num_mesas = 17

    def __init__(self, tipo=None, rut=None):
        'Constructor de la clase'
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.rut = rut
        self.tipo = tipo
        self.set_signals()
        self.showMaximized()
        self.config_user()

        self.setVisible(False) # Se oculta la ventana principal mientras se cargan los componentes.

        # Se crea un QProgressDialog para notificar al usuario sobre las cargas del programa.
        progress = QtGui.QProgressDialog("Cargando modulos...", "", 0, self.num_mesas+5)
        progress.setWindowTitle("Cargando...")
        progress.setWindowFlags(QtCore.Qt.WindowTitleHint)
        label = QtGui.QLabel()
        pixmap = QtGui.QPixmap('images/cafe_nostro_load_modulos.png')
        label.setPixmap(pixmap)
        progress.setLabel(label)
        progress.setCancelButton(None)
        progress.show()

        progress.setValue(0)
        self.ui.stackedWidget.addWidget(AdminUsers()) #2
        progress.setValue(1)
        self.ui.stackedWidget.addWidget(AdminProductos()) #3
        progress.setValue(2)
        self.ui.stackedWidget.addWidget(FormularioVenta(self.ui,self.rut,"0")) #4
        progress.setValue(3)
        self.ui.stackedWidget.addWidget(AdminVentas(self.ui)) #5
        progress.setValue(4)
        self.ui.stackedWidget.addWidget(MesasVenta(self,self.num_mesas,self.rut)) #6
        progress.setValue(5)

        pixmap = QtGui.QPixmap('images/cafe_nostro_load_mesas.png')
        label.setPixmap(pixmap)

        for i in range(1,self.num_mesas+1): #7 = primera mesa
            self.ui.stackedWidget.addWidget(FormularioVenta(self.ui,self.rut,str(i)))
            progress.setValue(i+5)

        self.ui.stackedWidget.addWidget(Estadistica()) # self.num_mesas+5
        progress.setValue(self.num_mesas+5)
        self.setVisible(True)

    def config_user(self):
        self.nombre = unicode(controller.getUsuarioRut(self.rut)[0].nombre)+" "+unicode(controller.getUsuarioRut(self.rut)[0].apellido)
        if(controller.getUsuarioRut(self.rut)[0].nombre == "root"):
            self.nombre = "ROOT"
        self.ui.label_usuario.setText(u"<font color='black' size='5'><b>"+self.nombre+"</b></font>")
        if(self.tipo != None):
            if(self.tipo == 1):
                self.ui.actionUsuarios.setEnabled(False)
                self.ui.actionProductos.setEnabled(False)
                self.ui.actionVentas.setEnabled(False)

    def set_signals(self):
        'Setea los triggers que se usaran para cambiar la interfaz'
        self.ui.actionVentas.triggered.connect(self.admin_ventas)
        self.ui.actionUsuarios.triggered.connect(self.admin_users)
        self.ui.actionProductos.triggered.connect(self.admin_productos)
        self.ui.actionEstadisticas.triggered.connect(self.admin_estadisticas)

        self.ui.pushButton_compra_directa.clicked.connect(self.formulario_venta_directa)
        self.ui.pushButton_mesas.clicked.connect(self.mesas_venta)
        self.ui.stackedWidget.currentChanged.connect(self.stackedWidget_changed)

    def stackedWidget_changed(self,index):
        for i in range(7,self.num_mesas+8):
            try:
                id_pedido = self.ui.stackedWidget.widget(i).id_pedido
                pedido = controller_venta.getPedido(id_pedido)
                if(pedido[0].en_curso == 0):
                    self.ui.stackedWidget.widget(i).set_ocupado(False)
                else:
                    self.ui.stackedWidget.widget(i).set_ocupado(True)
            except:
                pass

    def admin_estadisticas(self):
        'Cambia a la interfaz de venta por mesas'
        self.ui.stackedWidget.setCurrentIndex(self.num_mesas+7)
        self.ui.stackedWidget.widget(self.num_mesas+7).actualizar_productos()

    def mesas_venta(self):
        'Cambia a la interfaz de venta por mesas'
        self.ui.stackedWidget.setCurrentIndex(6)

    def admin_users(self):
        'Cambia a la interfaz de administración de usuarios'
        self.ui.stackedWidget.setCurrentIndex(2)

    def admin_productos(self):
        'Cambia a la interfaz de administración de productos'
        self.ui.stackedWidget.setCurrentIndex(3)

    def formulario_venta_directa(self):
        'Cambia a la interfaz de formulario de venta directa'
        self.ui.stackedWidget.setCurrentIndex(4)

    def admin_ventas(self):
        'Cambia a la interfaz de editar ventas de productos'
        self.ui.stackedWidget.setCurrentIndex(5)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
