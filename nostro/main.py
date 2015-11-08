#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
# sys.path.append('/login')
from PySide import QtGui
from login.view_login import Login


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = Login()
    main_window.show()
    sys.exit(app.exec_())
