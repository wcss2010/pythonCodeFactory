#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
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
      try:
        f = open(self.configPath,mode='r',encoding='utf-8')
        self.configObj = json.loads(f.read())
        f.close()
      except Exception as e:
        print(e)
    else:
      try:
        self.configObj['adapters'] = {'xxxxDBCode':{'title':'xxx','command':'python3 xxx.py input.json output.json'}}
        f = open(self.configPath,mode='w+',encoding='utf-8')
        f.write(json.dumps(self.configObj))
        f.close()
      except Exception as e:
        print(e)
  
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
    pass
    #self.mainUI.btnEncode.clicked.connect(self.btnEncodeClicked)
    #self.mainUI.btnDecode.clicked.connect(self.btnDecodeClicked)

  def btnOpenDBClicked(self,e):
    pass

  def btnMakeCodeClicked(self,e):
    pass

  def btnModifyScriptClicked(self,e):
    pass

  def btnMakeAllCodeClicked(self,e):
    pass

  def btnHelpClicked(self,e):
    pass

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