#-*- coding:utf-8 -*-
import sys
import os
import pathlib

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from ui.Ui_mainWindow import Ui_MainWindow
from Event_mainWindows import Event_mainWindow

if __name__ == '__main__':
   app = QApplication(sys.argv)
   MainWindow = QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   uiEvent = Event_mainWindow()
   uiEvent.setMainEvent(MainWindow,ui)
   MainWindow.show()
   sys.exit(app.exec_())