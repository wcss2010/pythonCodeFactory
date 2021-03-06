#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import base64
import subprocess
import shutil
import io

'''
   环境变量
'''
class cfenv(object):
    '''
        初始化配置及环境变量
    '''
    def initEnvData():
        #初始化配置对象
        cfenv.configObj = {}
        #初始化基础目录结构
        cfenv.rootDir = pathlib.Path(os.getcwd()).parent
        cfenv.binDir = os.path.join(cfenv.rootDir,'bin')
        cfenv.dataDir = os.path.join(cfenv.rootDir,'data')
        cfenv.dbPluginDir = os.path.join(cfenv.dataDir,'dbPlugins')        
        try:
            os.makedirs(cfenv.binDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.dataDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.dbPluginDir)
        except Exception as ex1:
            pass

        #初始化配置文件路径
        cfenv.configFilePath = os.path.join(cfenv.rootDir,'config.json')
        cfenv.backupConfigFilePath = os.path.join(cfenv.rootDir,'config.json.backup')
        cfenv.templeteScriptFile = os.path.join(cfenv.rootDir,'templete.js')

        #载入配置
        cfenv.loadConfig()

        #取环境变量名称
        cfenv.switchScriptEnv()
    
    '''
        切换脚本环境目录
    '''
    def switchScriptEnv():
        if cfenv.configObj.get('envDirName') == None:
            cfenv.__sEnvName = 'dotnet'
        else:
            cfenv.__sEnvName = cfenv.configObj['envDirName']

        #初始化脚本相关路径
        cfenv.scriptEnvDir = os.path.join(cfenv.dataDir,cfenv.__sEnvName)
        cfenv.scriptDir = os.path.join(cfenv.scriptEnvDir,'scripts')
        cfenv.attachDir = os.path.join(cfenv.scriptEnvDir,'attachs')
        try:
            os.makedirs(cfenv.scriptDir)
        except Exception as ex1:
            pass
        try:
            os.makedirs(cfenv.attachDir)
        except Exception as ex1:
            pass
        
        #初始化脚本文件路径        
        cfenv.normalScriptFile = os.path.join(cfenv.scriptDir,"normal.js")
        cfenv.entityAndDAOScriptFile = os.path.join(cfenv.scriptDir,"entityanddao.js")

    '''
        载入配置文件
    '''
    def loadConfig():
        #载入配置
        if pathlib.Path(cfenv.configFilePath).exists():
            #读入数据
            try:
                jsonStr = iotool.readAllText(cfenv.configFilePath)
                cfenv.configObj = json.loads(jsonStr)
            except Exception as exx:
                cfenv.initConfig()
        else:
            cfenv.initConfig()

    '''
        初始化配置文件,如果存在备份则使用，否则输出一个新的
    '''
    def initConfig():
        if pathlib.Path(cfenv.backupConfigFilePath).exists():
            shutil.copyfile(cfenv.backupConfigFilePath,cfenv.configFilePath)
        else:
            cfenv.writeNewConfig()
    '''
        输出标准配置文件
    '''
    def writeNewConfig():
        #初始化的例子
        cfenv.configObj['dbPlugins'] = {'xxxxCode':{'title':'xxxDB','code':'xxxxCode','command':'python3 {local}/xxx.py {input} {output}','responseCoding':'utf8'}}
        cfenv.configObj['codeFileExtName'] = '.cs'
        cfenv.configObj['classNameBefore'] = 'c'
        cfenv.configObj['classNameAfter'] = 'Entity'
        cfenv.configObj['classNamespace'] = 'com.pythoncodefactory.DotNetClasses'
        cfenv.configObj['envDirName'] = 'dotnet'
        cfenv.configObj['dialogRootDir'] = '~/'
        #写入数据
        iotool.writeAllText(cfenv.configFilePath,json.dumps(cfenv.configObj,indent=4))

'''
   用于模仿C#下的StringBuilder的功能
'''
class stringbuffer(object):
    def __init__(self):
        super().__init__()
        stringbuffer.enterFlag = '{<%enter%>}'
        self.clear()

    '''
       清空缓冲区
    '''
    def clear(self):
        self.__buf = ''
        return self

    '''
       添加文字
    '''
    def append(self,cnt):
        self.__buf = self.__buf + (cnt.replace('\r','').replace('\n',stringbuffer.enterFlag))
        return self

    '''
       添加文字并添加换行符
    '''
    def appendLine(self,cnt):
        self.append(cnt).append(stringbuffer.enterFlag)
        return self

    '''
       将文字放入缓冲区
    '''
    def fromString(self,cnt):
        self.__buf = (cnt.replace('\r','').replace('\n',stringbuffer.enterFlag))
        return self

    '''
       输出文字
    '''
    def toString(self):
        return self.__buf.replace(stringbuffer.enterFlag,'\n')

    '''
       解析Base64编码并放入缓冲区
    '''
    def fromB64String(self,b64String):
        return self.fromString(str(base64.b64decode(b64String), "utf-8"))        

    '''
       将内容编译为Base64文字并输出
    '''
    def toB64String(self):
        return str(base64.b64encode(self.__buf.encode("utf-8")), "utf-8")

'''
    Json字典
'''
class jsondict(object):
    def __init__(self):
        super().__init__()
        self.__buf = {}

    '''
       添加或更新
    '''
    def addOrUpdate(self,cName,cContent):
        self.__buf[cName] = cContent

    '''
       删除
    '''
    def remove(self,cName):
        try:
            return self.__buf.pop(cName)
        except Exception as ex:
            return None

    '''
       载入Json字典数据(从Json字符串)
    '''
    def load(self,cnt):
        try:
            self.__buf = json.loads(cnt)
        except Exception as ex:
            self.__buf = {}

    '''
       从文件载入Json字典数据(从文件)
    '''
    def loadFile(self,file):
        self.load(iotool.readAllText(file))

    '''
       从文件载入Json字典数据(从ScriptDir中的文件)
    '''
    def loadFileFromScriptDir(self,fName):
        self.loadFile(os.path.join(cfenv.scriptDir,fName))

    '''
       保存Json数据到文件
    '''
    def saveFile(self,file):
        iotool.writeAllText(file,json.dumps(self.__buf,indent=4))

    '''
       保存Json数据到ScriptDir中的文件
    '''
    def saveFileToScriptDir(self,fName):
        self.saveFile(os.path.join(cfenv.scriptDir,fName))

    '''
       获得数据
    '''
    def getValue(self,pName,defaultVal):
        if self.__buf.get(pName) == None:
            return defaultVal
        else:
            return self.__buf[pName]

    '''
       字典缓存中的items()函数
    '''
    def items(self):
        return self.__buf.items()

    '''字典缓存中的keys()函数
    '''
    def keys(self):
        keyList = []
        for k,v in self.items():
            keyList.append(k)
        return keyList

    '''
       字典缓存中的clear()函数
    '''
    def clear(self):
        self.__buf.clear()

    '''
       字典记录数
    '''
    def count(self):
        return len(self.__buf)

    '''
       输出Json串
    '''
    def toJsonString(self):
        return json.dumps(self.__buf,indent=4)
    
'''
    代码生成（主要用于载入模板文件然后替换）
'''
class codemaker(object):
    def __init__(self):
        self.__templete = ''
        self.kvData = jsondict()

    '''
        载入模板(从字符串)
    '''
    def loadTemplete(self,cnt):
        self.__templete = cnt
    
    '''
        载入模板(从文件)
    '''
    def loadTempleteFile(self,file):
        self.loadTemplete(iotool.readAllText(file))

    '''
        载入模板(从ScriptDir中的文件)
    '''
    def loadTempleteFileFromScriptDir(self,tName):
        self.loadTempleteFile(os.path.join(cfenv.scriptDir,tName))

    '''
        替换关键字
    '''
    def execute(self):
        tempStr = self.__templete
        for k,v in self.kvData.items():
            replaceKey = '$%' + k + '%$'
            tempStr = tempStr.replace(replaceKey,v)
        return stringbuffer().fromString(tempStr)

'''
   读写工具类
'''
class iotool(object):
    '''
      运行指令并等待返回结果
    '''
    def start(cmdStr,responseCoding):
       print('start command:' + cmdStr)
       proc = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
       proc.wait()
       stream_stdout = io.TextIOWrapper(proc.stdout, encoding=responseCoding)
       stream_stderr = io.TextIOWrapper(proc.stderr, encoding=responseCoding)      
       str_stdout = str(stream_stdout.read())
       str_stderr = str(stream_stderr.read())
       print("stdout: " + str_stdout)
       print("stderr: " + str_stderr)
       result = (str_stdout + str_stderr).strip()
       print('stdresult:' + result)
       return result,str_stdout,str_stderr

    '''
      读入所有文本
    '''
    def readAllText(fPath):
        result = ""
        if pathlib.Path(fPath).exists():
            try:
                f = open(fPath,mode='r',encoding='utf-8')
                result = f.read()
                f.close()
            except IOError as e:
                print(e)            
        return result

    '''
      读入所有字节
    '''
    def readAllByte(fPath):
        result = b''
        if pathlib.Path(fPath).exists():
            try:
                f = open(fPath,mode='rb')
                result = f.read()
                f.close()
            except IOError as e:
                print(e)            
        return result

    '''
      写入所有文本
    '''
    def writeAllText(fPath,strContent):
        try:
            f = open(fPath,mode='w',encoding='utf-8')
            f.write(strContent)
            f.close()
        except IOError as e:
            print(e)

    '''
      写入所有字节
    '''
    def writeAllByte(fPath,byteContent):
        try:
            f = open(fPath,mode='wb')
            f.write(byteContent)
            f.close()
        except IOError as e:
            print(e)