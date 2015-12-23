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
    """
    Método que retorna todos los productos de un pedido (especificado por id).
    """
    productos = VentaProducto()
    productos.id_pedido = id_pedido
    return VentaProducto.getProductosPedido(productos)

def getVentas():
    """
    Retorna todas las ventas registradas en la base de datos.
    """
    return Venta.all()

def getVentasPorFecha(fecha_inicio,fecha_fin):
    """
    Retorna todas las ventas comprendidas entre 'fecha_inicio' y 'fecha_fin'.
    """
    return Venta.getVentasPorFecha(fecha_inicio,fecha_fin)

def getProductosPorFecha(fecha):
    """
    Retorna todos los productos realizados en la fecha 'fecha'.
    """
    return VentaProducto.getProductosPorFecha(fecha)

class ProductoVenta(object):
    """
    Clase especializada de productos vendidos para mostrarlos en los 
    graficos estadisticos.
    Se almacena el producto (objeto), la fecha en la cual fue vendido,
    el precio y la cantidad.
    """
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
            row = [data.producto.codigo,data.producto.nombre,str(controller_admin_producto.zerosAtLeft(data.cantidad,3)),controller_admin_producto.monetaryFormat(data.precio),controller_admin_producto.monetaryFormat(data.precio*data.cantidad)]
            for j, field in enumerate(row):
                item = QtGui.QStandardItem(field)
                self.model.setItem(i, j, item)

        for col, h in enumerate(header):
            self.model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])

        self.setSourceModel(self.model)


def crear_html(lista_productos,fecha_inicio,fecha_fin):
    """
    Método que crea un html con los datos entregados en 'lista_productos'
    entre las fechas 'fecha_inicio' y 'fecha_fin'.
    """
    # Se crea un QProgressDialog para notificar al usuario sobre las cargas del programa.
    progress = QtGui.QProgressDialog("<font color='white'>Cargando graficos...</font>", "", 0, len(lista_productos))
    progress.setWindowTitle("Aviso")
    progress.setWindowFlags(QtCore.Qt.WindowTitleHint)
    progress.setCancelButton(None)
    progress.show()
    progress.setValue(0)

    distancia_dias = fecha_inicio.daysTo(fecha_fin)
    series = "series: ["
    series2 = "series: ["
    date = fecha_inicio.addMonths(-1).toString("yyyy,MM,dd")
    for i,producto_venta in enumerate(lista_productos):
        progress.setValue(i)
        fecha = fecha_inicio
        series = series + '{name:" '+ str(producto_venta.producto.nombre).decode('cp1252')+' ", pointInterval: 24 * 3600 * 1000, pointStart: Date.UTC('+date+'),data:['
        series2 = series2 + '{name:" '+ str(producto_venta.producto.nombre).decode('cp1252')+' ", pointInterval: 24 * 3600 * 1000, pointStart: Date.UTC('+date+'),data:['

        for i in range(distancia_dias+1):
            encontro_producto = False
            productos_venta = getProductosPorFecha(fecha.toString("yyyy-MM-dd"))
            for producto in productos_venta:
                if(producto_venta.producto.id_producto == producto.id_producto):
                    series = series + str(producto.cantidad) + ","
                    series2 = series2 + str(producto.cantidad*producto.precio_venta) + ","
                    encontro_producto = True
            if(not encontro_producto):
                series = series + "0" + ","
                series2 = series2 + "0" + ","
            fecha = fecha.addDays(1)
        series = series[:-1] + "]"
        series = series + "},"
        series2 = series2[:-1] + "]"
        series2 = series2 + "},"
    progress.setValue(len(lista_productos))
    series = series[:-1] + "]"
    series2 = series2[:-1] + "]"
    html = """
<!DOCTYPE HTML>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Highcharts Example</title>

        <script type="text/javascript" src="js/jquery.min.js"></script><script type="text/javascript">
        function isArray(obj) {
            return Object.prototype.toString.call(obj) === '[object Array]';
        }

        function splat(obj) {
            return isArray(obj) ? obj : [obj];
        }
        $(function () {
    $('#chart-unit-product').highcharts({
        chart: {
            type: 'line',
            zoomType: 'x'
        },
        title: {
            text: 'Unidades Vendidas por Producto'
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Fecha'
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
                    radius: 4
                },
                lineWidth: 2,
                states: {
                    hover: {
                        lineWidth: 3
                    }
                },
                threshold: null
            },
            column: {
                animation: false
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            formatter: function (tooltip) {
                var items = this.points || splat(this),
                    series = items[0].series,
                    s;

                // sort the values
                items.sort(function(a, b){
                    return ((a.y < b.y) ? -1 : ((a.y > b.y) ? 1 : 0));
                });
                items.reverse();

                return tooltip.defaultFormatter.call(this, tooltip);
            },
            shared: true
        },
        """+series+"""
    });
    $('#chart-price-product').highcharts({
        chart: {
            type: 'line',
            zoomType: 'x'
        },
        title: {
            text: 'Ingreso Total por Producto'
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Fecha'
            }
        },
        yAxis: {
            title: {
                text: '$ Pesos Chilenos (CLP)'
            },
            min: 0
        },
        plotOptions: {
            line: {
                marker: {
                    radius: 4
                },
                lineWidth: 2,
                states: {
                    hover: {
                        lineWidth: 3
                    }
                },
                threshold: null
            },
            column: {
                animation: false
            }
        },
        legend: {
            enabled: false
        },
        tooltip: {
            formatter: function (tooltip) {
                var items = this.points || splat(this),
                    series = items[0].series,
                    s;

                // sort the values
                items.sort(function(a, b){
                    return ((a.y < b.y) ? -1 : ((a.y > b.y) ? 1 : 0));
                });
                items.reverse();

                return tooltip.defaultFormatter.call(this, tooltip);
            },
            shared: true
        },
        """+series2+"""
    });
}); 
    </script>
    </head>
    <body>
<script src="js/highcharts.js"></script>
<script src="js/modules/exporting.js"></script>

<div id="chart-unit-product" style="min-width: 310px; height: 350px; margin: 0 auto"></div>
<div id="chart-price-product" style="min-width: 310px; height: 350px; margin: 0 auto"></div>

    </body>
</html>
"""
    return html