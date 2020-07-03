#-*- coding:utf-8 -*-
import sys
import os
import shutil
from globaltool import *
import pathlib
from dbAdapters.BaseAdapters import *
import time
import subprocess
import io

class AppConfigSchemaAdapter(BaseAdapter):
    def getTables(self,dbUrl):
       #初始化变量
       result = 'error'
       nameStr = self.dbAdapterInfo['title']
       codeStr = self.dbAdapterInfo['code']
       cmdStr = self.dbAdapterInfo['command']
       responseCoding = self.dbAdapterInfo['responseCoding']

       #检查输入配置,输出配置
       inputDir = os.path.join(cfenv.dataDir,'inputTempDir')
       outputDir = os.path.join(cfenv.dataDir,'outputTempDir')
       try:
           os.mkdir(inputDir)
       except IOError as e:
          print(e)
       try:
           os.mkdir(outputDir)
       except IOError as e:
          print(e)
        
       #生成输入和输出配置路径
       inputFile = os.path.join(inputDir,'input_' + str(time.time()) + ".json")
       outputFile = os.path.join(outputDir,'output_' + str(time.time()) + ".json")
       #写输入配置
       inputConfig = AdapterInputConfig(dbUrl,codeStr)
       iotool.writeAllText(inputFile,json.dumps(inputConfig.toDict(),indent=4))

       #生成命令字符串
       dbCmd = cmdStr.format(local=cfenv.dbPluginDir, input=inputFile, output=outputFile)
       
       #运行数据适配器程序等待结果返回
       allStr,normalStr,errorStr = iotool.start(dbCmd,responseCoding)

       #返回数据集
       runResult = {}
       if pathlib.Path(outputFile).exists():
           runResult = json.loads(iotool.readAllText(outputFile))
       return allStr,runResult