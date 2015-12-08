# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Dec 07 21:08:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 462)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_compra_directa = QtGui.QPushButton(self.groupBox)
        self.pushButton_compra_directa.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_compra_directa.setObjectName("pushButton_compra_directa")
        self.horizontalLayout.addWidget(self.pushButton_compra_directa)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pushButton_mesas = QtGui.QPushButton(self.groupBox)
        self.pushButton_mesas.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_mesas.setObjectName("pushButton_mesas")
        self.horizontalLayout.addWidget(self.pushButton_mesas)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_usuario = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_usuario.setFont(font)
        self.label_usuario.setObjectName("label_usuario")
        self.horizontalLayout.addWidget(self.label_usuario)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdministraci_n = QtGui.QMenu(self.menubar)
        self.menuAdministraci_n.setObjectName("menuAdministraci_n")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.actionUsuarios = QtGui.QAction(MainWindow)
        self.actionUsuarios.setObjectName("actionUsuarios")
        self.actionProductos = QtGui.QAction(MainWindow)
        self.actionProductos.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionProductos.setObjectName("actionProductos")
        self.actionRealizar_Venta = QtGui.QAction(MainWindow)
        self.actionRealizar_Venta.setObjectName("actionRealizar_Venta")
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCambiar_Usuario = QtGui.QAction(MainWindow)
        self.actionCambiar_Usuario.setObjectName("actionCambiar_Usuario")
        self.actionVentas = QtGui.QAction(MainWindow)
        self.actionVentas.setObjectName("actionVentas")
        self.menuAdministraci_n.addAction(self.actionUsuarios)
        self.menuAdministraci_n.addAction(self.actionProductos)
        self.menuAdministraci_n.addAction(self.actionVentas)
        self.menuArchivo.addAction(self.actionCambiar_Usuario)
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAdministraci_n.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CaféNostro", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_compra_directa.setText(QtGui.QApplication.translate("MainWindow", "Compra Directa", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_mesas.setText(QtGui.QApplication.translate("MainWindow", "Pedido por Mesas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_usuario.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setStatusTip(QtGui.QApplication.translate("MainWindow", "Sección administrativa de la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAdministraci_n.setTitle(QtGui.QApplication.translate("MainWindow", "&Administración", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "&Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setText(QtGui.QApplication.translate("MainWindow", "&Usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de usuarios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUsuarios.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setText(QtGui.QApplication.translate("MainWindow", "&Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana de administración de productos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProductos.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setText(QtGui.QApplication.translate("MainWindow", "&Realizar Venta", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setStatusTip(QtGui.QApplication.translate("MainWindow", "Ingresa a la ventana donde se venden los productos del local", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRealizar_Venta.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setStatusTip(QtGui.QApplication.translate("MainWindow", "Cierra la aplicación", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSalir.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_Usuario.setText(QtGui.QApplication.translate("MainWindow", "Cambiar Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCambiar_Usuario.setStatusTip(QtGui.QApplication.translate("MainWindow", "Regresa a la ventan Login para poder cambiar el usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVentas.setText(QtGui.QApplication.translate("MainWindow", "&Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVentas.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+4", None, QtGui.QApplication.UnicodeUTF8))

