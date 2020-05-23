# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flywcs/myData/myCode/python-clone-workspace/pythonCodeFactory/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1167, 635)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -20, 1161, 140))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.txtDBUrl = QtWidgets.QTextEdit(self.groupBox)
        self.txtDBUrl.setGeometry(QtCore.QRect(10, 30, 1141, 61))
        self.txtDBUrl.setObjectName("txtDBUrl")
        self.btnOpenDB = QtWidgets.QPushButton(self.groupBox)
        self.btnOpenDB.setGeometry(QtCore.QRect(350, 100, 87, 27))
        self.btnOpenDB.setObjectName("btnOpenDB")
        self.btnMakeCode = QtWidgets.QPushButton(self.groupBox)
        self.btnMakeCode.setGeometry(QtCore.QRect(450, 100, 87, 27))
        self.btnMakeCode.setObjectName("btnMakeCode")
        self.btnModifyScript = QtWidgets.QPushButton(self.groupBox)
        self.btnModifyScript.setGeometry(QtCore.QRect(670, 100, 141, 27))
        self.btnModifyScript.setObjectName("btnModifyScript")
        self.cbxDBAdapters = QtWidgets.QComboBox(self.groupBox)
        self.cbxDBAdapters.setGeometry(QtCore.QRect(10, 100, 331, 27))
        self.cbxDBAdapters.setObjectName("cbxDBAdapters")
        self.btnMakeAllCode = QtWidgets.QPushButton(self.groupBox)
        self.btnMakeAllCode.setGeometry(QtCore.QRect(550, 100, 111, 27))
        self.btnMakeAllCode.setObjectName("btnMakeAllCode")
        self.btnHelp = QtWidgets.QPushButton(self.groupBox)
        self.btnHelp.setGeometry(QtCore.QRect(880, 100, 51, 27))
        self.btnHelp.setObjectName("btnHelp")
        self.btnConfig = QtWidgets.QPushButton(self.groupBox)
        self.btnConfig.setGeometry(QtCore.QRect(820, 100, 51, 27))
        self.btnConfig.setObjectName("btnConfig")
        self.tvTables = QtWidgets.QTreeView(self.centralwidget)
        self.tvTables.setGeometry(QtCore.QRect(10, 130, 341, 470))
        self.tvTables.setObjectName("tvTables")
        self.twPages = QtWidgets.QTabWidget(self.centralwidget)
        self.twPages.setGeometry(QtCore.QRect(360, 130, 801, 470))
        self.twPages.setObjectName("twPages")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.twPages.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.twPages.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易数据库代码生成器V1.0"))
        self.btnOpenDB.setText(_translate("MainWindow", "打开连接"))
        self.btnMakeCode.setText(_translate("MainWindow", "生成代码"))
        self.btnModifyScript.setText(_translate("MainWindow", "修改代码生成脚本"))
        self.btnMakeAllCode.setText(_translate("MainWindow", "生成所有代码"))
        self.btnHelp.setText(_translate("MainWindow", "帮助"))
        self.btnConfig.setText(_translate("MainWindow", "配置"))
        self.twPages.setTabText(self.twPages.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.twPages.setTabText(self.twPages.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
