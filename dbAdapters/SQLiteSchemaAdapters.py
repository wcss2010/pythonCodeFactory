#-*- coding:utf-8 -*-
import sys
import os
import shutil
import sqlite3
import pathlib
from dbAdapters.BaseAdapters import *

class SQLiteSchemaAdapter(BaseAdapter):
    def getTables(self,dbUrl):
       schemaObj = SchemaDB("main",dbUrl,self.dbAdapterInfo)
       result = 'error'
       if pathlib.Path(dbUrl).exists():
           try:
               conn = sqlite3.connect(dbUrl)
               cur = conn.cursor()
               cur.execute("select name,type from sqlite_master order by name")
               result = cur.fetchall()
               for r in result:
                   tableInfo = SchemaTable(r[0],r[1])
                   cur.execute("PRAGMA table_info(" + tableInfo.tableName + ")")
                   tableResult = cur.fetchall()
                   for rr in tableResult:
                       columnInfo = SchemaColumn(rr[1],str(rr[2]).lower())
                       tableInfo.columns.append(columnInfo)
                   schemaObj.tables.append(tableInfo)
               result='ok'
           except sqlite3.Error as e:
               result='error,' + e
       else:
           result='error,db not found!'
       return result,schemaObj.toDict()