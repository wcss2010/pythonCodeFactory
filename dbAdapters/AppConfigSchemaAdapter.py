#-*- coding:utf-8 -*-
import sys
import os
import shutil
from UtilTool import *
import pathlib
from BaseAdapters import *
import time

class AppConfigSchemaAdapter(BaseAdapter):
    def getTables(self,dbUrl,dbAdapterInfo):       
       result = 'error'
       nameStr = self.dbAdapterInfo['title']
       cmdStr = self.dbAdapterInfo['command']
       inputFileStr = self.dbAdapterInfo['inputFile']
       outputFileStr = self.dbAdapterInfo['outputFile']
       #检查输入和输出配置目录
       inputDir = os.path.join(os.getcwd(),'inputTempDir')
       outputDir = os.path.join(os.getcwd(),'outputTempDir')
       try:
           os.mkdir(inputDir)
       except IOError as e:
          print(e)
       try:
           os.mkdir(outputDir)
       except IOError as e:
          print(e)
       #生成输入和输出配置路径
       inputFile = os.path.join(inputDir,'input_' + time.time() + ".json")
       outputFile = os.path.join(outputDir,'output_' + time.time() + ".json")
       #写输入配置
       inputConfig = AdapterInputConfig(dbUrl,nameStr)
       MyIOTool.writeAllText(inputFile,json.dumps(inputConfig.toDict(),indent=4))
       #运行外部程序获得数据库结构       
       result = os.system(cmdStr.format(input=inputFile,output=outputFile))
       runResult = {}
       if pathlib.Path(outputFile).exists():
           runResult = json.loads(MyIOTool.readAllText(outputFile))
       return result,runResult