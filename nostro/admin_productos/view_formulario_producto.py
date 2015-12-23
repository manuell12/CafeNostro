#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_producto
import controller_admin_producto


class FormularioProducto(QtGui.QDialog):
    """
    Clase FormularioProducto que permite al usuario ingresar datos tanto para
    un crear nuevo producto como para modificar un producto existente.
    """
    reloadT = QtCore.Signal()
    identificador = False
    codigo = ""

    types = controller_admin_producto.getNombresCategorias()
    __type_productos__ = ["----"]
    for data in types:
        __type_productos__.append(data.nombre)

    def __init__(self, id=None):
        super(FormularioProducto, self).__init__()
        self.ui = formulario_producto.Ui_FormularioProducto()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.setModal(True)
        self.show()
        self.connect_actions()
        for num, name in enumerate(self.__type_productos__):
            self.ui.comboBox_id_categoria.addItem(name, num)
        if(id == None):
            self.id = 0
            self.identificador = False
            self.setWindowTitle("Nuevo Producto")
            self.show()
        else:
            self.id = id
            self.identificador = True
            self.setWindowTitle("Editar Producto")
            producto = controller_admin_producto.getProductoId(id)
            for row in producto:
                self.nombre = row.nombre
                self.ui.lineEdit_nombre.setText(self.nombre)
                self.codigo = row.codigo
                self.ui.lineEdit_codigo.setText(self.codigo)
                self.descripcion = row.descripcion
                self.ui.lineEdit_descripcion.setText(self.descripcion)
                self.precio_bruto = int(row.precio_bruto)
                self.ui.lineEdit_precio_neto.setText(
                    str(self.precio_bruto).split(".")[0])
                self.id_categoria = row.id_categoria
                self.ui.comboBox_id_categoria.setCurrentIndex(
                    int(self.id_categoria))

    def connect_actions(self):
        """
        Método que conecta los slots de los widgets de la interfaz grafica 
        con las funciones de FormularioProducto.
        """
        self.ui.lineEdit_nombre.textChanged.connect(
            self.lineEdit_nombre_changed)
        self.ui.lineEdit_codigo.textChanged.connect(
            self.lineEdit_codigo_changed)
        self.ui.lineEdit_precio_neto.textChanged.connect(
            self.lineEdit_precio_neto_changed)
        self.ui.comboBox_id_categoria.currentIndexChanged.connect(
            self.comboBox_id_categoria_changed)

    def lineEdit_nombre_changed(self, text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_nombre'. Valida que el campo esté correctamente escrito.
        """
        controller_admin_producto.validarNombreF(
            self.ui.label_error_nombre, text)

    def lineEdit_codigo_changed(self, text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_codigo'. Valida que el campo esté correctamente escrito.
        """
        text_upper = text.upper()
        self.ui.lineEdit_codigo.setText(text_upper)
        controller_admin_producto.validarCodigoF(
            self.ui.label_error_codigo, text_upper, self.codigo)

    def lineEdit_precio_neto_changed(self, text):
        """
        Método que es llamado cuando el usuario cambia el contenido del QLabel
        'lineEdit_precio_neto'. Valida que el campo esté correctamente escrito.
        """
        controller_admin_producto.validarPrecioNetoF(
            self.ui.label_error_precio, text)

    def comboBox_id_categoria_changed(self, index):
        """
        Método que es llamado cuando el usuario cambia la seleccion del 
        QComboBox 'comboBox_id_categoria'. 
        Valida que el campo esté correctamente escrito.
        """
        if(index != 0):
            self.ui.label_error_categoria.setText(
                u"<font color='green'><b>Selección correcta.</b></font>")
        else:
            self.ui.label_error_categoria.setText(
                u"<font color='red'><b>Debe seleccionar un tipo.</b></font>")

    def accept(self):
        """
        Método que es llamado cuando el usuario presiona en el boton 'OK'.
        Guarda los cambios realizados sobre un producto existente o
        crea un nuevo producto con los datos ingresados.
        """
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.descripcion = unicode(self.ui.lineEdit_descripcion.toPlainText())        
        self.precio_bruto = unicode(self.ui.lineEdit_precio_neto.text())
        self.precio_neto = unicode(float(self.precio_bruto)*0.81)
        self.id_categoria = int(self.ui.comboBox_id_categoria.currentIndex())
        self.status = 1
        self.codigo = self.ui.lineEdit_codigo.text()
        if(self.identificador):  # Editar Producto
            self.status = controller_admin_producto.getProductoId(self.id)[0].status
            validar = controller_admin_producto.validarDatos(
                self.ui.label_error_nombre.text(),
                self.ui.label_error_codigo.text(),
                self.ui.label_error_precio.text(),
                self.ui.label_error_categoria.text())
            if(validar):
                controller_admin_producto.UpdateDataProducto(
                    self.id, 
                    self.nombre, 
                    self.descripcion, 
                    self.precio_neto, 
                    self.precio_bruto, 
                    self.status, 
                    self.id_categoria, 
                    self.codigo)
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setWindowTitle("Correcto")
                msgBox.setText("Producto editado correctamente.")
                msgBox.exec_()
                self.setVisible(False)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Critical)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Revise los campos obligatorios.")
                msgBox.exec_()
        else:
            validar = controller_admin_producto.validarDatos(
                self.ui.label_error_nombre.text(),
                self.ui.label_error_codigo.text(),
                self.ui.label_error_precio.text(),
                self.ui.label_error_categoria.text())
            if(validar):
                controller_admin_producto.AddDataProducto(
                    self.nombre, 
                    self.descripcion, 
                    self.precio_neto, 
                    self.precio_bruto, 
                    self.status, 
                    self.id_categoria, 
                    self.codigo)
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setWindowTitle("Correcto")
                msgBox.setText("Producto creado correctamente.")
                msgBox.exec_()
                self.setVisible(False)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Critical)
                msgBox.setWindowTitle("Error")
                msgBox.setText("Revise los campos obligatorios.")
                msgBox.exec_()
        self.reloadT.emit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioProducto()
    sys.exit(app.exec_())
