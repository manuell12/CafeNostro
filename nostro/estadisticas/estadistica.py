# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadistica.ui'
#
# Created: Sun Dec 13 21:53:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Estadistica(object):
    def setupUi(self, Estadistica):
        Estadistica.setObjectName("Estadistica")
        Estadistica.resize(1100, 547)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Estadistica)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(Estadistica)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.calendarWidget_inicio = QtGui.QCalendarWidget(Estadistica)
        self.calendarWidget_inicio.setMaximumSize(QtCore.QSize(16777215, 180))
        self.calendarWidget_inicio.setObjectName("calendarWidget_inicio")
        self.verticalLayout_2.addWidget(self.calendarWidget_inicio)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(Estadistica)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.calendarWidget_fin = QtGui.QCalendarWidget(Estadistica)
        self.calendarWidget_fin.setMaximumSize(QtCore.QSize(16777215, 180))
        self.calendarWidget_fin.setObjectName("calendarWidget_fin")
        self.verticalLayout_3.addWidget(self.calendarWidget_fin)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Estadistica)
        self.label.setMinimumSize(QtCore.QSize(0, 10))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_ingreso_total = QtGui.QLabel(Estadistica)
        self.label_ingreso_total.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_ingreso_total.setObjectName("label_ingreso_total")
        self.horizontalLayout.addWidget(self.label_ingreso_total)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tableView = QtGui.QTableView(Estadistica)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.webView = QtWebKit.QWebView(Estadistica)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.webView.setObjectName("webView")
        self.horizontalLayout_3.addWidget(self.webView)

        self.retranslateUi(Estadistica)
        QtCore.QMetaObject.connectSlotsByName(Estadistica)

    def retranslateUi(self, Estadistica):
        Estadistica.setWindowTitle(QtGui.QApplication.translate("Estadistica", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Estadistica", "Inicio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Estadistica", "Fin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Estadistica", "Ingreso Total:   $", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ingreso_total.setText(QtGui.QApplication.translate("Estadistica", "0", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit