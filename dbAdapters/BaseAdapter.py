#-*- coding:utf-8 -*-
import sys
import os
import shutil
import UtilTool

class BaseAdapter(object):
   def getTables(self,dbUrl,dbAdapterInfo):
       pass

class SchemaDB(object):
   def __init__(self,dbName,dbUrl,dbAdapterInfo):
       self.dbName = dbName
       self.dbUrl = dbUrl
       self.dbAdapterInfo = dbAdapterInfo
       self.tables = {}
   def toDict(self):
       data = {}
       data["dbName"] = self.dbName
       data["dbUrl"] = self.dbUrl
       data["tables"] = {}
       for(table in self.tables):
           data["tables"][table.tableName] = table.toDict()
       return data

class SchemaTable(object):
   def __init__(self,tableName,tableType):
       self.tableName = tableName
       self.tableType = tableType
       self.columns = []
   def toDict(self):
       data = {}
       data["tableName"] = self.tableName
       data["tableType"] = self.tableType
       data["columns"] = []
       for(col in self.columns):
          data["columns"].append({"name":col.columnName,"type":col.columnType})
       return data

class SchemaColumn(object):
   def __init__(self,columnName,columnType):
       self.columnName = columnName
       self.columnType = columnType