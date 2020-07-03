#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import base64

class cfenv(object):
    def __init__(self):
        super().__init__()
        cfenv.paths = self
        self.rootDir = pathlib.Path(os.getcwd()).parent
        self.binDir = os.path.join(self.rootDir,'bin')
        self.dataDir = os.path.join(self.rootdir,'data')
        self.dbPluginDir = os.path.join(self.dataDir,'dbPlugins')
        self.scriptDir = os.path.join(self.dataDir,'scripts')
        self.attachDir = os.path.join(self.dataDir,'attachs')
        try:
            os.mkdir(self.binDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(self.dataDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(self.dbPluginDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(self.scriptDir)
        except Exception as ex1:
            pass
        try:
            os.mkdir(self.attachDir)
        except Exception as ex1:
            pass

class stringbuffer(object):
    def __init__(self):
        super().__init__()
        self.clear()

    def clear(self):
        self.__buf = ''
        return self

    def append(self,cnt):
        self.__buf = self.__buf + cnt
        return self

    def appendLine(self,cnt):
        self.append(cnt).append('\n')
        return self

    def toString(self):
        return self.__buf
    
    def fromB64String(self,b64String):
        self.__buf = base64.b64decode(b64String)
        return self
    
    def toB64String(self):
        return base64.b64encode(self.toString())

class jsonbuilder(object):
    def __init__(self):
        super().__init__()
        self.__buf = {}

    def append(self,cName,b64String):
        self.__buf[cName] = b64String
    
    def remove(self,cName):
        try:
            self.__buf.pop(cName)
        except Exception as ex:
            pass

    def toString(self):
        return json.dumps(self.__buf)

class iotool(object):
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