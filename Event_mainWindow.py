#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from UtilTool import UtilTool
from JsCompile import JsCompile
import os
import sys
import pathlib
import json
from ui.Ui_mainWindow import Ui_MainWindow

class Event_mainWindow(object):
  def setMainEvent(self,mainWindowThread,mainUIDefine):
    #保存引用，主窗体线程
    self.mainWindow = mainWindowThread
    #保存引用，窗体定义类
    self.mainUI = mainUIDefine
    #屏蔽最大化按钮
    self.mainWindow.setFixedSize(1167, 635)
    #生成脚本路径
    self.scriptDir = os.path.join(os.getcwd(),"scripts")
    #生成配置文件路径
    self.configPath = os.path.join(os.getcwd(),'config.json')
    self.configObj = {}
    #载入配置
    self.loadConfig()
    #加载甜酸器类型
    self.loadAdapterList()
    #设置事件
    self.setEvents()

  def loadConfig(self):
    if pathlib.Path(self.configPath).exists():
      #读入数据
      jsonStr = UtilTool.readAllText(self.configPath)
      self.configObj = json.loads(jsonStr)
    else:
      #初始化的例子
      self.configObj['adapters'] = {'xxxxCode':{'title':'xxxDB','command':'python3 xxx.py *input* *output*','inputFile':'input.json','outputFile':'output.json'}}
      #写入数据
      UtilTool.writeAllText(self.configPath,json.dumps(self.configObj))
  
  def loadAdapterList(self):
    #内置
    self.mainUI.cbxDBAdapters.addItem('Sqlite数据库(内置)')
    #外置    
    if self.configObj.get('adapters') == None:
       pass
    else:
       self.adapterList = self.configObj.get('adapters')
       print(self.adapterList)
       for k,v in self.adapterList.items():
         self.mainUI.cbxDBAdapters.addItem(v['title'] + '数据库(外置)',userData=v)
  
  def setEvents(self):    
    self.mainUI.btnOpenDB.clicked.connect(self.btnOpenDBClicked)
    self.mainUI.btnMakeCode.clicked.connect(self.btnMakeCodeClicked)
    self.mainUI.btnModifyScript.clicked.connect(self.btnModifyScriptClicked)
    self.mainUI.btnMakeAllCode.clicked.connect(self.btnMakeAllCodeClicked)
    self.mainUI.btnHelp.clicked.connect(self.btnHelpClicked)
    self.mainUI.btnConfig.clicked.connect(self.btnConfigClicked)

  def btnOpenDBClicked(self,e):
    pass

  def btnMakeCodeClicked(self,e):
    scriptStr = UtilTool.readAllText('/home/flywcs/test.js')
    tableData = {'Version':[{"Name":"ID","Type":"nvarchar"},{"Name":"Name","Type":"nvarchar"}]}
    resultStr = JsCompile(scriptStr,self.mainUI.txtDBUrl.toPlainText(),json.dumps(tableData)).execute()
    QMessageBox.information(None,'结果',resultStr)

  def btnModifyScriptClicked(self,e):
    pass

  def btnMakeAllCodeClicked(self,e):
    pass

  def btnHelpClicked(self,e):
    QMessageBox.information(None,'关于','简易数据库代码生成器V1.0')

  def btnConfigClicked(self,e):
    pass

  def btnEncodeClicked(self,e):
    pass
    #if self.mainUI.txtCode.toPlainText() == None:
    #    pass
    #else:
    #    try:
    #        imgFile = os.getcwd() + '/q.png'
    #        img = qrcode.make(self.mainUI.txtCode.toPlainText())
    #        img.save(imgFile)
    #        self.mainUI.lblImage.setPixmap(QPixmap(imgFile))
    #    except Exception as ex:
    #        self.mainUI.statusbar.showMessage('生成错误...Ex:' + ex)    
  def btnDecodeClicked(self,e):
    pass
    #imgFile,imgFormat = QFileDialog.getOpenFileName(None,'选择二维码图片','~/','图片文件(*.png *.jpg *.jpeg)')
    #if pathlib.Path(imgFile).exists():
    #    self.mainUI.lblImage.setPixmap(QPixmap(imgFile))
    #    zx = zxing.BarCodeReader()
    #    zxData = zx.decode(imgFile)
    #    if zxData == None:
    #        pass
    #    else:
    #        self.mainUI.txtCode.setText(zxData.raw)
    #else:
    #    pass