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
import shutil
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
    #初始化
    self.initData()

  def loadConfig(self):
    if pathlib.Path(self.configPath).exists():
      #读入数据
      jsonStr = UtilTool.readAllText(self.configPath)
      self.configObj = json.loads(jsonStr)
    else:
      #初始化的例子
      self.configObj['adapters'] = {'xxxxCode':{'title':'xxxDB','command':'python3 xxx.py *input* *output*','inputFile':'input.json','outputFile':'output.json'}}
      #写入数据
      UtilTool.writeAllText(self.configPath,json.dumps(self.configObj,indent=4))
  
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
    self.mainUI.btnMakeAllCode.clicked.connect(self.btnMakeAllCodeClicked)
    self.mainUI.btnHelp.clicked.connect(self.btnHelpClicked)
    self.mainUI.btnSaveNormalScript.clicked.connect(self.btnSaveNormalScriptClicked)
    self.mainUI.btnSaveEntityAndDAOScript.clicked.connect(self.btnSaveEntityAndDAOScriptClicked)
    self.mainUI.btnSaveConfig.clicked.connect(self.btnSaveConfigClicked)

  def initData(self):
    #加载配置文件
    if (pathlib.Path(self.configPath).exists()):
        self.mainUI.txtConfig.setText(UtilTool.readAllText(self.configPath))
    #检查是否脚本没有创建
    scriptDir = os.path.join(os.getcwd(),'scripts')
    if (pathlib.Path(scriptDir).exists()):
        pass
    else:
        os.makedirs(scriptDir)
    templeteFile = os.path.join(os.getcwd(),'templete.js')
    #初始化常用代码脚本
    self.normalScriptFile = os.path.join(scriptDir,"normal.js")
    if (pathlib.Path(self.normalScriptFile).exists()):
      pass
    else:
      if (pathlib.Path(templeteFile).exists()):
          try:
            shutil.copyfile(templeteFile,self.normalScriptFile)
          except Exception as e:
            print(e)
      else:
        UtilTool.writeAllText(self.normalScriptFile)
    #初始化实体和DAO代码脚本
    self.entityAndDAOScriptFile = os.path.join(scriptDir,"entityanddao.js")
    if (pathlib.Path(self.entityAndDAOScriptFile).exists()):
      pass
    else:
      if (pathlib.Path(templeteFile).exists()):
          try:
            shutil.copyfile(templeteFile,self.entityAndDAOScriptFile)
          except Exception as e:
            print(e)
      else:
        UtilTool.writeAllText(self.entityAndDAOScriptFile)
    #显示脚本内容
    self.mainUI.txtNormalScript.setText(UtilTool.readAllText(self.normalScriptFile))
    self.mainUI.txtEntityAndDAOScript.setText(UtilTool.readAllText(self.entityAndDAOScriptFile))
  
  def btnOpenDBClicked(self,e):
    print(os.system("java -version"))

  def btnMakeCodeClicked(self,e):
    scriptStr = UtilTool.readAllText('/home/flywcs/test.js')
    tempData = {'a1':'vvvvv','a2':'bbbbbb'}
    resultStr = JsCompile(scriptStr,self.mainUI.txtDBUrl.toPlainText(),tempData).execute()
    QMessageBox.information(None,'结果',resultStr)

  def btnMakeAllCodeClicked(self,e):
    pass
  
  def btnHelpClicked(self,e):
    QMessageBox.information(None,'关于','简易数据库代码生成器V1.0\n本软件基于Python编写！')

  def btnSaveNormalScriptClicked(self,e):
    try:
      UtilTool.writeAllText(self.normalScriptFile,self.mainUI.txtNormalScript.toPlainText())
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnSaveEntityAndDAOScriptClicked(self,e):
    try:
      UtilTool.writeAllText(self.entityAndDAOScriptFile,self.mainUI.txtEntityAndDAOScript.toPlainText())
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnSaveConfigClicked(self,e):
    try:
      UtilTool.writeAllText(self.configPath,self.mainUI.txtConfig.toPlainText())
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)