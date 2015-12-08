#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from login.view_login import Login
from PySide import QtGui

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = Login()
    main_window.show()
    app.setStyleSheet(open("style.qss", "r").read())
    sys.exit(app.exec_())
