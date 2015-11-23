#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_producto
import controller_admin_producto


class FormularioProducto(QtGui.QDialog):

    reloadT = QtCore.Signal()
    identificador = False

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
                self.descripcion = row.descripcion
                self.ui.lineEdit_descripcion.setText(self.descripcion)
                self.precio_bruto = int(row.precio_bruto)
                self.ui.lineEdit_precio_neto.setText(str(self.precio_bruto).split(".")[0])
                self.id_categoria = row.id_categoria
                self.ui.comboBox_id_categoria.setCurrentIndex(
                    int(self.id_categoria))

    def connect_actions(self):
        self.ui.lineEdit_nombre.textChanged.connect(
            self.lineEdit_nombre_changed)
        self.ui.lineEdit_precio_neto.textChanged.connect(
            self.lineEdit_precio_neto_changed)
        self.ui.comboBox_id_categoria.currentIndexChanged.connect(
            self.comboBox_id_categoria_changed)

    def lineEdit_nombre_changed(self, text):
        controller_admin_producto.validarNombreF(
            self.ui.label_error_nombre, text)

    def lineEdit_precio_neto_changed(self, text):
        controller_admin_producto.validarPrecioNetoF(
            self.ui.label_error_precio, text)

    def comboBox_id_categoria_changed(self, index):
        if(index != 0):
            self.ui.label_error_categoria.setText(
                u"<font color='green'><b>Seleccion correcta.</b></font>")
        else:
            self.ui.label_error_categoria.setText(
                u"<font color='red'><b>Debe seleccionar un tipo.</b></font>")

    def accept(self):
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.descripcion = unicode(self.ui.lineEdit_descripcion.toPlainText())        
        self.precio_bruto = unicode(self.ui.lineEdit_precio_neto.text())
        self.precio_neto = unicode(float(self.precio_bruto)*0.81)
        self.id_categoria = int(self.ui.comboBox_id_categoria.currentIndex())
        self.status = 1
        if(self.identificador):  # Editar Producto
            validar = controller_admin_producto.validarDatos(
                self.ui.label_error_nombre.text(),
                self.ui.label_error_precio.text(),
                self.ui.label_error_categoria.text())
            if(validar):
                controller_admin_producto.UpdateDataProducto(
                    self.id, self.nombre, self.descripcion, self.precio_neto, self.precio_bruto, self.status, self.id_categoria)
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setWindowTitle("Correcto")
                msgBox.setText("Producto editado correctamente.")
                msgBox.exec_()
                self.setVisible(False)
        else:
            validar = controller_admin_producto.validarDatos(
                self.ui.label_error_nombre.text(),
                self.ui.label_error_precio.text(),
                self.ui.label_error_categoria.text())
            if(validar):
                controller_admin_producto.AddDataProducto(
                    self.nombre, self.descripcion, self.precio_neto, self.precio_bruto, self.status, self.id_categoria)
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setWindowTitle("Correcto")
                msgBox.setText("Producto creado correctamente.")
                msgBox.exec_()
                self.setVisible(False)
        self.reloadT.emit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioProducto()
    sys.exit(app.exec_())
