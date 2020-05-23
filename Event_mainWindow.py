#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
import os
import sys
import pathlib

class Event_mainWindow(object):
  def setMainEvent(self,mainWindowThread,mainUIDefine):
    #保存引用
    self.mainWindow = mainWindowThread #主窗体线程
    self.mainUI = mainUIDefine  #窗体定义类

    #设置事件
    #self.mainUI.btnEncode.clicked.connect(self.btnEncodeClicked)
    #self.mainUI.btnDecode.clicked.connect(self.btnDecodeClicked)
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