#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import base64
import subprocess
import io

'''
   环境变量
'''
class cfenv(object):
    '''
       初始化目录
    '''
    def initDirs():
        cfenv.rootDir = pathlib.Path(os.getcwd()).parent
        cfenv.binDir = os.path.join(cfenv.rootDir,'bin')
        cfenv.dataDir = os.path.join(cfenv.rootDir,'data')
        cfenv.dbPluginDir = os.path.join(cfenv.dataDir,'dbPlugins')
        cfenv.scriptDir = os.path.join(cfenv.dataDir,'scripts')
        cfenv.attachDir = os.path.join(cfenv.dataDir,'attachs')
        try:
            os.mkdir(cfenv.binDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(cfenv.dataDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(cfenv.dbPluginDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(cfenv.scriptDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(cfenv.attachDir)
        except Exception as ex1:
            pass

'''
   用于模仿C#下的StringBuilder的功能
'''
class stringbuffer(object):
    def __init__(self):
        super().__init__()
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
        self.__buf = self.__buf + cnt
        return self

    '''
       添加文字并添加\n
    '''
    def appendLine(self,cnt):
        self.append(cnt).append('\n')
        return self

    '''
       将文字放入缓冲区
    '''
    def fromString(self,cnt):
        self.__buf = cnt
        return self

    '''
       输出文字
    '''
    def toString(self):
        return self.__buf

    '''
       解析Base64编码并放入缓冲区
    '''
    def fromB64String(self,b64String):
        self.__buf = base64.b64decode(b64String)
        return self

    '''
       将内容编译为Base64文字并输出
    '''
    def toB64String(self):
        return base64.b64encode(self.toString())

'''
    Json代码编辑类
'''
class jsoncodebuilder(object):
    def __init__(self):
        super().__init__()
        self.__buf = {}

    '''
       添加代码
    '''
    def append(self,cName,b64String):
        self.__buf[cName] = b64String

    '''
       删除代码
    '''
    def remove(self,cName):
        try:
            self.__buf.pop(cName)
        except Exception as ex:
            pass

    '''
       输出Json串
    '''
    def toString(self):
        return json.dumps(self.__buf)

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