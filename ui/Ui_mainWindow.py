# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/flyss/myData/myCode/pythonWorkSpace/pythonCodeFactory/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1168, 635)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tvTables = QtWidgets.QTreeView(self.centralwidget)
        self.tvTables.setGeometry(QtCore.QRect(10, 109, 341, 491))
        self.tvTables.setTabletTracking(True)
        self.tvTables.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tvTables.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tvTables.setWordWrap(True)
        self.tvTables.setHeaderHidden(True)
        self.tvTables.setObjectName("tvTables")
        self.twPages = QtWidgets.QTabWidget(self.centralwidget)
        self.twPages.setGeometry(QtCore.QRect(360, 109, 801, 491))
        self.twPages.setObjectName("twPages")
        self.tabNormal = QtWidgets.QWidget()
        self.tabNormal.setObjectName("tabNormal")
        self.txtNormalText = LineCodeEditor(self.tabNormal)
        self.txtNormalText.setGeometry(QtCore.QRect(10, 10, 781, 390))
        self.txtNormalText.setObjectName("txtNormalText")
        self.txtNormalCodeSearch = QtWidgets.QLineEdit(self.tabNormal)
        self.txtNormalCodeSearch.setGeometry(QtCore.QRect(10, 410, 591, 31))
        self.txtNormalCodeSearch.setObjectName("txtNormalCodeSearch")
        self.btnNormalBeforeFind = QtWidgets.QPushButton(self.tabNormal)
        self.btnNormalBeforeFind.setGeometry(QtCore.QRect(610, 410, 81, 36))
        self.btnNormalBeforeFind.setObjectName("btnNormalBeforeFind")
        self.btnNormalAfterFind = QtWidgets.QPushButton(self.tabNormal)
        self.btnNormalAfterFind.setGeometry(QtCore.QRect(700, 410, 81, 36))
        self.btnNormalAfterFind.setObjectName("btnNormalAfterFind")
        self.twPages.addTab(self.tabNormal, "")
        self.tabEntityAndDAO = QtWidgets.QWidget()
        self.tabEntityAndDAO.setObjectName("tabEntityAndDAO")
        self.txtEntityAndDAOText = LineCodeEditor(self.tabEntityAndDAO)
        self.txtEntityAndDAOText.setGeometry(QtCore.QRect(10, 10, 781, 390))
        self.txtEntityAndDAOText.setObjectName("txtEntityAndDAOText")
        self.txtEntityAndDAOCodeSearch = QtWidgets.QLineEdit(self.tabEntityAndDAO)
        self.txtEntityAndDAOCodeSearch.setGeometry(QtCore.QRect(10, 410, 590, 31))
        self.txtEntityAndDAOCodeSearch.setObjectName("txtEntityAndDAOCodeSearch")
        self.btnEADAfterFind = QtWidgets.QPushButton(self.tabEntityAndDAO)
        self.btnEADAfterFind.setGeometry(QtCore.QRect(700, 410, 81, 36))
        self.btnEADAfterFind.setObjectName("btnEADAfterFind")
        self.btnEADBeforeFind = QtWidgets.QPushButton(self.tabEntityAndDAO)
        self.btnEADBeforeFind.setGeometry(QtCore.QRect(610, 410, 81, 36))
        self.btnEADBeforeFind.setObjectName("btnEADBeforeFind")
        self.twPages.addTab(self.tabEntityAndDAO, "")
        self.tabNormalScript = QtWidgets.QWidget()
        self.tabNormalScript.setObjectName("tabNormalScript")
        self.btnSaveNormalScript = QtWidgets.QPushButton(self.tabNormalScript)
        self.btnSaveNormalScript.setGeometry(QtCore.QRect(700, 10, 87, 27))
        self.btnSaveNormalScript.setObjectName("btnSaveNormalScript")
        self.txtNormalScript = JSCodeEditor(self.tabNormalScript)
        self.txtNormalScript.setGeometry(QtCore.QRect(10, 40, 781, 390))
        self.txtNormalScript.setObjectName("txtNormalScript")
        self.twPages.addTab(self.tabNormalScript, "")
        self.tabEntityAndDAOScript = QtWidgets.QWidget()
        self.tabEntityAndDAOScript.setObjectName("tabEntityAndDAOScript")
        self.btnSaveEntityAndDAOScript = QtWidgets.QPushButton(self.tabEntityAndDAOScript)
        self.btnSaveEntityAndDAOScript.setGeometry(QtCore.QRect(700, 10, 87, 27))
        self.btnSaveEntityAndDAOScript.setObjectName("btnSaveEntityAndDAOScript")
        self.txtEntityAndDAOScript = JSCodeEditor(self.tabEntityAndDAOScript)
        self.txtEntityAndDAOScript.setGeometry(QtCore.QRect(10, 40, 781, 391))
        self.txtEntityAndDAOScript.setObjectName("txtEntityAndDAOScript")
        self.twPages.addTab(self.tabEntityAndDAOScript, "")
        self.btnConfigEditor = QtWidgets.QWidget()
        self.btnConfigEditor.setObjectName("btnConfigEditor")
        self.btnSaveConfig = QtWidgets.QPushButton(self.btnConfigEditor)
        self.btnSaveConfig.setGeometry(QtCore.QRect(700, 10, 87, 27))
        self.btnSaveConfig.setObjectName("btnSaveConfig")
        self.btnDownloadOutputTemplete = QtWidgets.QPushButton(self.btnConfigEditor)
        self.btnDownloadOutputTemplete.setGeometry(QtCore.QRect(580, 10, 111, 27))
        self.btnDownloadOutputTemplete.setObjectName("btnDownloadOutputTemplete")
        self.btnDownloadInputTemplete = QtWidgets.QPushButton(self.btnConfigEditor)
        self.btnDownloadInputTemplete.setGeometry(QtCore.QRect(460, 10, 111, 27))
        self.btnDownloadInputTemplete.setObjectName("btnDownloadInputTemplete")
        self.btnDownloadJS = QtWidgets.QPushButton(self.btnConfigEditor)
        self.btnDownloadJS.setGeometry(QtCore.QRect(340, 10, 111, 27))
        self.btnDownloadJS.setObjectName("btnDownloadJS")
        self.txtConfig = LineCodeEditor(self.btnConfigEditor)
        self.txtConfig.setGeometry(QtCore.QRect(10, 40, 781, 391))
        self.txtConfig.setObjectName("txtConfig")
        self.twPages.addTab(self.btnConfigEditor, "")
        self.btnHelp = QtWidgets.QPushButton(self.centralwidget)
        self.btnHelp.setGeometry(QtCore.QRect(1080, 70, 61, 27))
        self.btnHelp.setObjectName("btnHelp")
        self.btnMakeCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnMakeCode.setGeometry(QtCore.QRect(460, 70, 90, 27))
        self.btnMakeCode.setObjectName("btnMakeCode")
        self.btnMakeAllCode = QtWidgets.QPushButton(self.centralwidget)
        self.btnMakeAllCode.setGeometry(QtCore.QRect(560, 70, 151, 27))
        self.btnMakeAllCode.setObjectName("btnMakeAllCode")
        self.cbxDBAdapters = QtWidgets.QComboBox(self.centralwidget)
        self.cbxDBAdapters.setGeometry(QtCore.QRect(10, 70, 341, 27))
        self.cbxDBAdapters.setObjectName("cbxDBAdapters")
        self.txtDBUrl = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDBUrl.setGeometry(QtCore.QRect(10, 10, 1151, 50))
        self.txtDBUrl.setObjectName("txtDBUrl")
        self.btnOpenDB = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenDB.setGeometry(QtCore.QRect(360, 70, 90, 27))
        self.btnOpenDB.setObjectName("btnOpenDB")
        self.btnOpenAttachDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenAttachDir.setGeometry(QtCore.QRect(720, 70, 111, 27))
        self.btnOpenAttachDir.setObjectName("btnOpenAttachDir")
        self.btnOpenPluginDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenPluginDir.setGeometry(QtCore.QRect(840, 70, 111, 27))
        self.btnOpenPluginDir.setObjectName("btnOpenPluginDir")
        self.btnOpenScriptDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenScriptDir.setGeometry(QtCore.QRect(960, 70, 111, 27))
        self.btnOpenScriptDir.setObjectName("btnOpenScriptDir")
        self.plWaitBox = QtWidgets.QGroupBox(self.centralwidget)
        self.plWaitBox.setGeometry(QtCore.QRect(10, 420, 350, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plWaitBox.setFont(font)
        self.plWaitBox.setAutoFillBackground(False)
        self.plWaitBox.setStyleSheet("QGroupBox  {background:rgb(0, 170, 255);}\n"
"QGroupBox  {color:white;}\n"
"QGroupBox{\n"
"border-width:2px;\n"
"border-style:solid;\n"
"border-radius: 10px;\n"
"border-color:rgb(0, 170, 255);\n"
"margin-top:0.5ex;\n"
"}")
        self.plWaitBox.setAlignment(QtCore.Qt.AlignCenter)
        self.plWaitBox.setObjectName("plWaitBox")
        self.lblWaitText = QtWidgets.QLabel(self.plWaitBox)
        self.lblWaitText.setGeometry(QtCore.QRect(10, 30, 330, 110))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblWaitText.setFont(font)
        self.lblWaitText.setStyleSheet("QLabel{color:white}\n"
"QLabel{\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: white;}")
        self.lblWaitText.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWaitText.setObjectName("lblWaitText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.twPages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易数据库代码生成器V1.4.4  本项目地址: https://github.com/wcss2010/pythoncodefactory"))
        self.tabNormal.setProperty("currentTabText", _translate("MainWindow", "常用代码"))
        self.txtNormalCodeSearch.setPlaceholderText(_translate("MainWindow", "请输入要查询的关键字！"))
        self.btnNormalBeforeFind.setText(_translate("MainWindow", "向前找"))
        self.btnNormalAfterFind.setText(_translate("MainWindow", "向后找"))
        self.twPages.setTabText(self.twPages.indexOf(self.tabNormal), _translate("MainWindow", "常用代码"))
        self.tabEntityAndDAO.setProperty("currentTabText", _translate("MainWindow", "fff"))
        self.txtEntityAndDAOCodeSearch.setPlaceholderText(_translate("MainWindow", "请输入要查询的关键字！"))
        self.btnEADAfterFind.setText(_translate("MainWindow", "向后找"))
        self.btnEADBeforeFind.setText(_translate("MainWindow", "向前找"))
        self.twPages.setTabText(self.twPages.indexOf(self.tabEntityAndDAO), _translate("MainWindow", "实体和DAO"))
        self.btnSaveNormalScript.setText(_translate("MainWindow", "保存"))
        self.twPages.setTabText(self.twPages.indexOf(self.tabNormalScript), _translate("MainWindow", "编辑常用代码脚本"))
        self.btnSaveEntityAndDAOScript.setText(_translate("MainWindow", "保存"))
        self.twPages.setTabText(self.twPages.indexOf(self.tabEntityAndDAOScript), _translate("MainWindow", "编辑实体和DAO代码脚本"))
        self.btnSaveConfig.setText(_translate("MainWindow", "保存"))
        self.btnDownloadOutputTemplete.setText(_translate("MainWindow", "下载输出模板"))
        self.btnDownloadInputTemplete.setText(_translate("MainWindow", "下载输入模板"))
        self.btnDownloadJS.setText(_translate("MainWindow", "下载脚本模板"))
        self.twPages.setTabText(self.twPages.indexOf(self.btnConfigEditor), _translate("MainWindow", "编辑配置文件"))
        self.btnHelp.setText(_translate("MainWindow", "关于我"))
        self.btnMakeCode.setText(_translate("MainWindow", "生成代码"))
        self.btnMakeAllCode.setText(_translate("MainWindow", "生成所有代码文件"))
        self.btnOpenDB.setText(_translate("MainWindow", "打开数据库"))
        self.btnOpenAttachDir.setText(_translate("MainWindow", "打开附件目录"))
        self.btnOpenPluginDir.setText(_translate("MainWindow", "打开插件目录"))
        self.btnOpenScriptDir.setText(_translate("MainWindow", "打开脚本目录"))
        self.plWaitBox.setTitle(_translate("MainWindow", "提示"))
        self.lblWaitText.setText(_translate("MainWindow", "正在XX，请等待......"))

from jsCodeEditors import JSCodeEditor, LineCodeEditor
