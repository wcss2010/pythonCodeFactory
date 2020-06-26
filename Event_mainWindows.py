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
      try:
        jsonStr = MyIOTool.readAllText(self.configPath)
        self.configObj = json.loads(jsonStr)
      except Exception as exx:
        self.initConfig()        
    else:
      self.initConfig()
  
  def initConfig(self):
    #初始化的例子
    self.configObj['adapters'] = {'xxxxCode':{'title':'xxxDB','code':'xxxxCode','command':'python3 {local}/xxx.py {input} {output}','responseCoding':'utf8'}}
    self.configObj['codeFileExtName'] = '.cs'
    self.configObj['classNameBefore'] = 't'
    self.configObj['classNameAfter'] = 'Object'
    self.configObj['classNamespace'] = 'com.example'
    self.configObj['dialogRootDir'] = '~/'
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
    self.mainUI.btnDownloadJS.clicked.connect(self.btnDownloadJSClicked)
    self.mainUI.btnOpenAttachDir.clicked.connect(self.btnOpenAttachDirClicked)
    self.mainUI.btnOpenPluginDir.clicked.connect(self.btnOpenPluginDirClicked)
    self.mainUI.btnOpenScriptDir.clicked.connect(self.btnOpenScriptDirClicked)

  def initData(self):
    self.nodeModels = QStandardItemModel()
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
    self.mainUI.tvTables.setModel(None)
    dbAdapter = self.mainUI.cbxDBAdapters.currentData()
    if (dbAdapter==None):
      pass
    else:
      try:
         result,rData = dbAdapter.getTables(self.mainUI.txtDBUrl.toPlainText())
         print('Result:' + result)
         print('Tables:' + json.dumps(rData,indent=4))
         if result.startswith('ok'):
           #成功
           self.nodeModels = QStandardItemModel()
           tableList = rData["tables"]
           if tableList==None:
              pass
           else:
              for tName,tTable in tableList.items():
                tableObj = QStandardItem(tTable["tableName"] + '(' + tTable["tableType"] + ')')
                tableObj.setData(tTable)
                tableObj.setEditable(False)
                columnList = tTable["columns"]
                for cObj in columnList:
                   colTitle = cObj["name"] + '('+ cObj["type"] +',notnull:'+ cObj['notnull'] +',pk:' + cObj['pk'] + ')'
                   columnObj = QStandardItem(colTitle)
                   columnObj.setEditable(False)
                   tableObj.appendRow(columnObj)
                self.nodeModels.appendRow(tableObj)
           self.mainUI.tvTables.setModel(self.nodeModels)
         else:
           #失败
           errorResult = result.replace('error,','')
           QMessageBox.information(None,"错误","打开数据库错误！错误输出：" + errorResult)         
      except Exception as e:
        print('error:' + str(e))
        QMessageBox.information(None,"错误","打开数据库错误！错误输出：" + str(e))

  def btnMakeCodeClicked(self,e):
    if self.nodeModels.rowCount() >= 1:
      if len(self.mainUI.tvTables.selectedIndexes()) >= 1:
          #获得单表数据
          index = self.mainUI.tvTables.selectedIndexes()[0]
          crawler = index.model().itemFromIndex(index)
          tableData = crawler.data()
          print(json.dumps(tableData))
          if (tableData == None):
            pass
          else:
            #载入脚本代码
            normalScript = MyIOTool.readAllText(self.normalScriptFile)
            entityAndDAOScript = MyIOTool.readAllText(self.entityAndDAOScriptFile)
            #编译执行
            try:
              normalDisplayText = ''
              entityDisplayText = ''
              #编译并显示常用代码
              normalResult = json.loads(self.compileJS(normalScript,tableData))
              for kk,vv in normalResult.items():
                  normalDisplayText = normalDisplayText+'代码段('+kk+'):\n'
                  normalDisplayText = normalDisplayText+vv+';\n'
              self.mainUI.txtNormalText.setPlainText(normalDisplayText)
              #编译并显示实体和DAO代码
              entityResult = json.loads(self.compileJS(entityAndDAOScript,tableData))
              for kkk,vvv in entityResult.items():
                  entityDisplayText = entityDisplayText+'代码段('+kkk+'):\n'
                  entityDisplayText = entityDisplayText+vvv+';\n'
              self.mainUI.txtEntityAndDAOText.setPlainText(entityDisplayText)
            except Exception as ex:
              print(ex)
              QMessageBox.information(None,"错误","代码生成错误！错误输出：" + str(ex))
  
  def compileJS(self,script,tableData):
    return JsCompiler(script,self.mainUI.txtDBUrl.toPlainText(),tableData,self.configObj).execute()

  def btnMakeAllCodeClicked(self,e):
    if self.nodeModels.rowCount() >= 1:
      try:
        #选择路径
        destPath=QFileDialog.getExistingDirectory(None,"请选择保存位置！",self.configObj["dialogRootDir"])
        #生成目标路径      
        destCodePath = os.path.join(destPath,'classes')
        destAttachPath = os.path.join(destPath,'attachs')
        sourceAttachPath = os.path.join(os.getcwd(),'codeAttachs')
        #复制附件目录到
        if pathlib.Path(sourceAttachPath).exists():
          try:
            shutil.copytree(sourceAttachPath,destAttachPath)
          except Exception as ex:
            print(ex)
        #创建代码目录
        try:
          os.mkdir(destCodePath)
        except Exception as ee:
          print(ee)
        if pathlib.Path(destCodePath).exists():
          #生成代码
          classBeforeName = self.configObj["classNameBefore"]
          classAfterName = self.configObj["classNameAfter"]
          codeFileExtName = self.configObj["codeFileExtName"]
          #读入实体和DAO脚本
          entityScript = MyIOTool.readAllText(self.entityAndDAOScriptFile)
          for rowIndex in range(0,self.nodeModels.rowCount()):
            itemRow = self.nodeModels.item(rowIndex)
            if itemRow==None or itemRow.data()==None:
              pass
            else:
              tableData = itemRow.data()
              if tableData == None:
                pass
              else:              
                entityResult = json.loads(self.compileJS(entityScript,tableData))
                for kkk,vvv in entityResult.items():
                  destFile = os.path.join(destCodePath,kkk + codeFileExtName)
                  MyIOTool.writeAllText(destFile,vvv)
          QMessageBox.information(None,"提示","代码生成完成！")
      except Exception as vv:
        print(vv)
        QMessageBox.information(None,"错误","代码生成错误！错误输出：" + str(vv))
  
  def btnHelpClicked(self,e):
    QMessageBox.information(None,'关于','简易数据库代码生成器\n本软件基于Python3.7+PyQT5+JS2Py+NumPy编写！')

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
      self.mainUI.txtConfig.setText(MyIOTool.readAllText(self.configPath))
      QMessageBox.information(None,"提示","保存完成!")
    except Exception as e:
      QMessageBox.information(None,"错误","保存失败!输出：" + e)

  def btnDownloadInputTempleteClicked(self,e):
    inputAdapter = AdapterInputConfig("data source ='xxxdb'","xxxcode")    
    inputFile,inputFormat = QFileDialog.getSaveFileName(None,"选择输入模板保存位置",self.configObj["dialogRootDir"],"输入模板[JSON](*.json)")
    MyIOTool.writeAllText(inputFile,json.dumps(inputAdapter.toDict(),indent=4))
    QMessageBox.information(None,"提示","保存完成！")
  
  def btnDownloadOutputTempleteClicked(self,e):
    tempDB = SchemaDB("xxDB","data source ='xxxdb'",{})
    tempTable = SchemaTable("xxx","table")
    tempIDField = SchemaColumn("ID","bigint","true","true")
    tempNameField = SchemaColumn("Name","nvarchar(200)","false","false")
    tempTable.columns.append(tempIDField)
    tempTable.columns.append(tempNameField)
    tempDB.tables.append(tempTable)
    outputFile,outputFormat = QFileDialog.getSaveFileName(None,"选择输出模板保存位置",self.configObj["dialogRootDir"],"输出模板[JSON](*.json)")
    MyIOTool.writeAllText(outputFile,json.dumps(tempDB.toDict(),indent=4))
    QMessageBox.information(None,"提示","保存完成！")

  def btnDownloadJSClicked(self,e):    
    inputFile,inputFormat = QFileDialog.getSaveFileName(None,"选择脚本模板保存位置",self.configObj["dialogRootDir"],"JS脚本[JS](*.js)")
    MyIOTool.writeAllText(inputFile,MyIOTool.readAllText(os.path.join(os.getcwd(),"templete.js")))
    QMessageBox.information(None,"提示","保存完成！")

  def btnOpenAttachDirClicked(self,e):
    try:
      if sys.platform == 'win32':
        os.startfile(os.path.join(os.getcwd(),"codeAttachs"))
      else:
        QMessageBox.information(None,"提示","对不起，这个功能只能在windows下用！")
    except Exception as ex:
      print(ex)
  
  def btnOpenPluginDirClicked(self,e):
    try:
      if sys.platform == 'win32':
        os.startfile(os.path.join(os.getcwd(),"dbAdapters"))
      else:
        QMessageBox.information(None,"提示","对不起，这个功能只能在windows下用！")
    except Exception as ex:
      print(ex)

  def btnOpenScriptDirClicked(self,e):
    try:
      if sys.platform == 'win32':
        os.startfile(os.path.join(os.getcwd(),"scripts"))
      else:
        QMessageBox.information(None,"提示","对不起，这个功能只能在windows下用！")
    except Exception as ex:
      print(ex)