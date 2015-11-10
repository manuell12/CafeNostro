#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import formulario_producto
import controller_admin_producto


class FormularioProducto(QtGui.QDialog):

    reloadT = QtCore.Signal()
    identificador = False
    __type_productos__ = ((u"------"),
                      (u"Comida"),
                      (u"Helado"),
                      (u"Café"),
                      (u"Bebida"))

    def __init__(self, id=None):
        super(FormularioProducto, self).__init__()
        self.ui = formulario_producto.Ui_FormularioProducto()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowTitleHint)
        self.setModal(True)
        self.show()
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
                self.nombre = row[1]
                self.ui.lineEdit_nombre.setText(self.nombre)
                self.descripcion = row[2]
                self.ui.lineEdit_descripcion.setText(self.descripcion)
                self.precio_neto = str(row[4])
                self.ui.lineEdit_precio_neto.setText(self.precio_neto)
                self.id_categoria = row[6]
                self.ui.comboBox_id_categoria.setCurrentIndex(int(self.id_categoria))

    def accept(self):
        self.nombre = unicode(self.ui.lineEdit_nombre.text())
        self.descripcion = unicode(self.ui.lineEdit_descripcion.text())
        self.tipo = self.__type_productos__[int(self.ui.comboBox_id_categoria.currentIndex())]
        self.precio_neto = unicode(self.ui.lineEdit_precio_neto.text())
        self.id_categoria = int(self.ui.comboBox_id_categoria.currentIndex())
        self.status = 1
        if(self.identificador):  # Editar Producto
            
            controller_admin_producto.UpdateDataProducto(
                self.id, self.nombre, self.descripcion, self.tipo, self.precio_neto, self.status, self.id_categoria)
            self.setVisible(False)
        else:
            controller_admin_producto.AddDataProducto(
                self.nombre, self.descripcion, self.tipo, self.precio_neto, self.status, self.id_categoria)
            self.setVisible(False)
        self.reloadT.emit()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = FormularioProducto()
    sys.exit(app.exec_())
