# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estadistica.ui'
#
# Created: Sun Dec 13 17:59:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Estadistica(object):
    def setupUi(self, Estadistica):
        Estadistica.setObjectName("Estadistica")
        Estadistica.resize(622, 411)
        self.calendarWidget = QtGui.QCalendarWidget(Estadistica)
        self.calendarWidget.setGeometry(QtCore.QRect(330, 10, 280, 155))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableView = QtGui.QTableView(Estadistica)
        self.tableView.setGeometry(QtCore.QRect(50, 40, 256, 192))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Estadistica)
        QtCore.QMetaObject.connectSlotsByName(Estadistica)

    def retranslateUi(self, Estadistica):
        Estadistica.setWindowTitle(QtGui.QApplication.translate("Estadistica", "Form", None, QtGui.QApplication.UnicodeUTF8))

