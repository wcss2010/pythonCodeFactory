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
       result = 'error'
       nameStr = self.dbAdapterInfo['title']
       codeStr = self.dbAdapterInfo['code']
       cmdStr = self.dbAdapterInfo['command']
       responseCoding = self.dbAdapterInfo['responseCoding']
       #检查输入配置,输出配置,插件工作目录
       inputDir = os.path.join(os.getcwd(),'inputTempDir')
       outputDir = os.path.join(os.getcwd(),'outputTempDir')
       pluginDir = os.path.join(os.getcwd(),'dbAdapters')
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
       MyIOTool.writeAllText(inputFile,json.dumps(inputConfig.toDict(),indent=4))
       #运行外部程序获得数据库结构
       nowCmd = cmdStr.format(local=pluginDir, input=inputFile, output=outputFile)
       print('db command:' + nowCmd)
       proc = subprocess.Popen(nowCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
       proc.wait()
       stream_stdout = io.TextIOWrapper(proc.stdout, encoding=responseCoding)
       stream_stderr = io.TextIOWrapper(proc.stderr, encoding=responseCoding)      
       str_stdout = str(stream_stdout.read())
       str_stderr = str(stream_stderr.read())
       print("stdout: " + str_stdout)
       print("stderr: " + str_stderr)
       result = (str_stdout + str_stderr).strip()
       print('db command result:' + result)
       runResult = {}
       if pathlib.Path(outputFile).exists():
           runResult = json.loads(MyIOTool.readAllText(outputFile))
       return result,runResult
