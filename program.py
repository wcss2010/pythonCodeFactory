#-*- coding:utf-8 -*-
import sys
import os
from globaltool import *

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from ui.Ui_mainWindow import Ui_MainWindow
from Event_mainWindows import Event_mainWindow

if __name__ == '__main__':
   #初始化环境变量
   cfenv.initEnvData()
   print("Bin:" + cfenv.binDir)
   print("Data:" + cfenv.dataDir)
   print("dbPlugin:" + cfenv.dbPluginDir)
   print("scriptEnv:" + cfenv.scriptEnvDir)
   print("script:" + cfenv.scriptDir)
   print("attach:" + cfenv.attachDir)
   print("configFile:" + cfenv.configFilePath)
   print("backupConfigFile:" + cfenv.backupConfigFilePath)
   print("templeteScriptFile:" + cfenv.templeteScriptFile)
   #启动程序
   app = QApplication(sys.argv)
   MainWindow = QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   uiEvent = Event_mainWindow()
   uiEvent.setMainEvent(MainWindow,ui)
   MainWindow.show()
   sys.exit(app.exec_())