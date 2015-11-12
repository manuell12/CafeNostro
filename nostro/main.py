#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('.\login')
from PySide import QtGui
import view_login as v


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = v.Login()
    main_window.show()
    sys.exit(app.exec_())
