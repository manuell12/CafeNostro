#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from PySide import QtCore, QtGui
from model_estadistica import VentaProducto, Venta
from admin_productos.model_admin_producto import Producto
import admin_productos.controller_admin_producto as controller_admin_producto

def getProductosPedido(id_pedido):
    productos = VentaProducto()
    productos.id_pedido = id_pedido
    return VentaProducto.getProductosPedido(productos)

def getVentas():
    return Venta.all()

def getVentasPorFecha(fecha_inicio,fecha_fin):
    return Venta.getVentasPorFecha(fecha_inicio,fecha_fin)

class ProductoVenta(object):
    producto = Producto()
    fecha = ""
    precio = 0
    cantidad = 0
    def __init__(
            self,
            producto=Producto(),
            cantidad=0,
            precio=0,
            fecha=""):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = int(precio)
        self.fecha = fecha

class TotalProductosModel(QtGui.QSortFilterProxyModel):
    """
    Un QSortFilterProxyModel especializado que carga los datos dados en un modelo bidimensional QStandardItemModel.
    """

    def __init__(self, parent=None):
        super(TotalProductosModel, self).__init__(parent)
        self.setDynamicSortFilter(True)

    def load_data(self, datos, header):
        """
        Carga la información dada en un QStandardItemModel
        """
        row = len(datos)

        self.model = QtGui.QStandardItemModel(row, len(header))

        for i, data in enumerate(datos):
            row = [data.producto.codigo,data.producto.nombre,str(data.cantidad),str(data.precio),str(data.precio*data.cantidad),str(data.fecha)]
            for j, field in enumerate(row):
                item = QtGui.QStandardItem(field)
                self.model.setItem(i, j, item)

        for col, h in enumerate(header):
            self.model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])

        self.setSourceModel(self.model)


def crear_html(lista_productos,fecha_inicio,fecha_fin):
    """=======================================================OPTIMIZAR!!!!===================================================="""
    # Se crea un QProgressDialog para notificar al usuario sobre las cargas del programa.
    progress = QtGui.QProgressDialog("Cargando productos...", "", 0, len(lista_productos))
    progress.setWindowTitle("Cargando...")
    progress.setWindowFlags(QtCore.Qt.WindowTitleHint)
    progress.setCancelButton(None)
    progress.show()
    progress.setValue(0)

    distancia_dias = fecha_inicio.daysTo(fecha_fin)
    series = "series: ["
    date = fecha_inicio.addMonths(-1).toString("yyyy,MM,dd")
    for i,producto_venta in enumerate(lista_productos):
        progress.setValue(i)
        fecha = fecha_inicio
        series = series + '{name:" '+ str(producto_venta.producto.nombre).decode('cp1252')+' ", pointInterval: 24 * 3600 * 1000, pointStart: Date.UTC('+date+'),data:['

        for i in range(distancia_dias+1):
            encontro_producto = False
            ventas = getVentasPorFecha(fecha.toString("yyyy-MM-dd"),fecha.toString("yyyy-MM-dd"))
            lista_ProductoVenta = list()
            for venta in ventas:
                venta_productos = getProductosPedido(venta.id_pedido)
                for ventaProducto in venta_productos:
                    agregar = True
                    for producto in lista_ProductoVenta:
                        if(ventaProducto.id_producto == producto.producto.id_producto):
                            producto.cantidad = producto.cantidad + ventaProducto.cantidad
                            agregar = False
                    if(agregar):
                        objeto_producto_venta = ProductoVenta(
                            controller_admin_producto.getProductoId(ventaProducto.id_producto)[0],
                            ventaProducto.cantidad,
                            ventaProducto.precio_venta,
                            venta.fecha)
                        lista_ProductoVenta.append(objeto_producto_venta)
            for ventaProducto in lista_ProductoVenta:
                if(ventaProducto.producto.id_producto == producto_venta.producto.id_producto):
                    series = series + str(ventaProducto.cantidad) + ","
                    encontro_producto = True
            if(not encontro_producto):
                series = series + "0" + ","
            fecha = fecha.addDays(1)
        series = series[:-1] + "]"
        series = series + "},"
    progress.setValue(len(lista_productos))
    series = series[:-1] + "]"
    html = """
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Highcharts Example</title>

        <script type="text/javascript" src="js/jquery.min.js"></script><script type="text/javascript">$(function () {
    $('#chart-unit-product').highcharts({
        chart: {
            type: 'area',
            zoomType: 'x'
        },
        title: {
            text: 'Unidades Vendidas por Producto'
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
                day: '%e of %b'
            }
        },
        yAxis: {
            title: {
                text: 'Unidades'
            },
            min: 0
        },
        plotOptions: {
            line: {
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            },
            column: {
                animation: false
            }
        },
        tooltip: {
            crosshairs: [true],
            shared: true,
            formatter: function () {
                var ind = '<span style="font-size: 75%">' + Highcharts.dateFormat('%A, %b %e', this.x) + '</span><br>',
                    sum = 0;

                $.each(this.points, function (i, point) {
                    ind += '<span style="color:' + point.series.color + '">\u25CF</span> ' + point.series.name + ': <b>' + point.y + '</b><br/>';
                });

                ind += '<br/>Total: <b>' + this.points[0].total + '</b>'

                console.log(this);
                return ind;
            }
        },
        """+series+"""
    });
}); 
    </script>
    </head>
    <body>
<script src="js/highcharts.js"></script>
<script src="js/modules/exporting.js"></script>

<div id="chart-unit-product" style="min-width: 310px; height: 400px; margin: 0 auto"></div>

    </body>
</html>
"""
    return html