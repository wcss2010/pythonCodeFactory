#-*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from ui.Ui_mainWindow import Ui_MainWindow

if __name__ == '__main__':
   app = QApplication(sys.argv)
   MainWindow = QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec_())