#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from login.view_login import Login
from PySide import QtGui,QtCore

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = Login()
    main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    main_window.show()
    app.setStyleSheet(open("style.qss", "r").read())
    sys.exit(app.exec_())
