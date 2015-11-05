#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from main_window import Ui_MainWindow
from view_admin_user import AdminUsers
import sys


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_signals()

        self.show()

    def set_signals(self):
        QtGui.QAction.connect(self.ui.actionUsuarios,
                              QtCore.SIGNAL("triggered()"), self.admin_users)

    def admin_users(self):
        admin_user = AdminUsers()
        admin_user.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    # main.setSourceModel(main.loadMovies(main))
    sys.exit(app.exec_())
