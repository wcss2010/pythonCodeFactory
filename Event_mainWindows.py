#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from UtilTool import *
from JsCompile import *
from dbAdapters.BaseAdapters import *
from dbAdapters.SQLiteSchemaAdapters import *
from dbAdapters.AppConfigSchemaAdapters import *
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
      jsonStr = MyIOTool.readAllText(self.configPath)
      self.configObj = json.loads(jsonStr)
    else:
      #初始化的例子
      self.configObj['adapters'] = {'xxxxCode':{'title':'xxxDB','command':'python3 xxx.py {input} {output}','inputFile':'input.json','outputFile':'output.json'}}
      self.configObj['codeFileExtName'] = '.cs'
      self.configObj['classNameBefore'] = 't'
      self.configObj['classNameAfter'] = 'Object'
      self.configObj['classNamespace'] = 'com.example'
      #写入数据
      MyIOTool.writeAllText(self.configPath,json.dumps(self.configObj,indent=4))
  
  def loadAdapterList(self):
    self.mainUI.cbxDBAdapters.clear()
    #内置
    sqliteAdapter = SQLiteSchemaAdapter()
    sqliteAdapter.initAdapter(None)
    self.mainUI.cbxDBAdapters.addItem('Sqlite数据库(内置)',userData=sqliteAdapter)
    #外置
    if self.configObj.get('adapters') == None:
       pass
    else:
       self.adapterList = self.configObj.get('adapters')
       print(self.adapterList)
       for k,v in self.adapterList.items():
         appAdapter = AppConfigSchemaAdapter()
         appAdapter.initAdapter(v)
         self.mainUI.cbxDBAdapters.addItem(v['title'] + '数据库(外置)',userData=appAdapter)
  
  def setEvents(self):    
    self.mainUI.btnOpenDB.clicked.connect(self.btnOpenDBClicked)
    self.mainUI.btnMakeCode.clicked.connect(self.btnMakeCodeClicked)    
    self.mainUI.btnMakeAllCode.clicked.connect(self.btnMakeAllCodeClicked)
    self.mainUI.btnHelp.clicked.connect(self.btnHelpClicked)
    self.mainUI.btnSaveNormalScript.clicked.connect(self.btnSaveNormalScriptClicked)
    self.mainUI.btnSaveEntityAndDAOScript.clicked.connect(self.btnSaveEntityAndDAOScriptClicked)
    self.mainUI.btnSaveConfig.clicked.connect(self.btnSaveConfigClicked)
    self.mainUI.btnDownloadInputTemplete.clicked.connect(self.btnDownloadInputTempleteClicked)
    self.mainUI.btnDownloadOutputTemplete.clicked.connect(self.btnDownloadOutputTempleteClicked)

  def initData(self):
    #加载配置文件
    if (pathlib.Path(self.configPath).exists()):
        self.mainUI.txtConfig.setText(MyIOTool.readAllText(self.configPath))
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
        MyIOTool.writeAllText(self.normalScriptFile)
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
        MyIOTool.writeAllText(self.entityAndDAOScriptFile)
    #显示脚本内容
    self.mainUI.txtNormalScript.setText(MyIOTool.readAllText(self.normalScriptFile))
    self.mainUI.txtEntityAndDAOScript.setText(MyIOTool.readAllText(self.entityAndDAOScriptFile))
  
  def btnOpenDBClicked(self,e):
    print(os.system("java -version"))

  def btnMakeCodeClicked(self,e):
    scriptStr = MyIOTool.readAllText('/home/flywcs/test.js')
    tempData = {'a1':'vvvvv','a2':'bbbbbb'}
    resultStr = JsCompileTool(scriptStr,self.mainUI.txtDBUrl.toPlainText(),tempData).execute()
    QMessageBox.information(None,'结果',resultStr)

  def btnMakeAllCodeClicked(self,e):
    pass
  
  def btnHelpClicked(self,e):
    QMessageBox.information(None,'关于','简易数据库代码生成器V1.0\n本软件基于Python编写！')

  def btnSaveNormalScriptClicked(self,e):
    try:
      MyIOTool.writeAllText(self.normalScriptFile,self.mainUI.txtNormalScript.toPlainText())
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnSaveEntityAndDAOScriptClicked(self,e):
    try:
      MyIOTool.writeAllText(self.entityAndDAOScriptFile,self.mainUI.txtEntityAndDAOScript.toPlainText())
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnSaveConfigClicked(self,e):
    try:
      MyIOTool.writeAllText(self.configPath,self.mainUI.txtConfig.toPlainText())
      self.loadConfig()
      self.loadAdapterList()
      QMessageBox.information(None,"提示","保存完成!")
    except IOError as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnDownloadInputTempleteClicked(self,e):
    inputAdapter = AdapterInputConfig("data source ='xxxdb'","xxxdb")    
    inputFile,inputFormat = QFileDialog.getSaveFileName(None,"选择输入模板保存位置","~/","输入模板[JSON](*.json)")
    MyIOTool.writeAllText(inputFile,json.dumps(inputAdapter.toDict(),indent=4))
    QMessageBox.information(None,"提示","保存完成！")
  
  def btnDownloadOutputTempleteClicked(self,e):
    tempDB = SchemaDB("xxDB","data source ='xxxdb'",{})
    tempTable = SchemaTable("xxx","table")
    tempIDField = SchemaColumn("ID","bigint")
    tempNameField = SchemaColumn("Name","nvarchar(200)")
    tempTable.columns.append(tempIDField)
    tempTable.columns.append(tempNameField)
    tempDB.tables.append(tempTable)
    outputFile,outputFormat = QFileDialog.getSaveFileName(None,"选择输出模板保存位置","~/","输出模板[JSON](*.json)")
    MyIOTool.writeAllText(outputFile,json.dumps(tempDB.toDict(),indent=4))
    QMessageBox.information(None,"提示","保存完成！")