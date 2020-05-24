#-*- coding:utf-8 -*-
import sys
import os
import shutil
import UtilTool

class BaseAdapter(object):
   def initAdapter(adapterInfo):
       self.dbAdapterInfo = adapterInfo

   def getTables(self,dbUrl):
       pass

class AdapterInputConfig(object):
   def __init__(self,dUrl,dType):
       self.dbUrl = dUrl
       self.dbType = dType
   def toDict(self):
       data = {}
       data["dbUrl"] = self.dbUrl
       data["dbType"] = self.dbType
       return data

class SchemaDB(object):
   def __init__(self,dName,dUrl,dAdapterInfo):
       self.dbName = dName
       self.dbUrl = dUrl
       self.dbAdapterInfo = dAdapterInfo
       self.tables = []
   def toDict(self):
       data = {}
       data["dbName"] = self.dbName
       data["dbUrl"] = self.dbUrl
       data["tables"] = {}
       for table in self.tables:
           data["tables"][table.tableName] = table.toDict()
       return data

class SchemaTable(object):
   def __init__(self,tName,tType):
       self.tableName = tName
       self.tableType = tType
       self.columns = []
   def toDict(self):
       data = {}
       data["tableName"] = self.tableName
       data["tableType"] = self.tableType
       data["columns"] = []
       for col in self.columns:
          data["columns"].append({"name":col.columnName,"type":col.columnType})
       return data

class SchemaColumn(object):
   def __init__(self,cName,cType):
       self.columnName = cName
       self.columnType = cType