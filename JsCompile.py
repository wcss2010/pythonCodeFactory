#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import js2py

class JsCompiler(object):
    def __init__(self,jsCode,dbUrl,tables,config):
        self.scriptCode = jsCode
        self.dbUrl = dbUrl
        self.dbTables = tables
        self.dbConfig = config
    
    def execute(self):
        script = js2py.eval_js(self.scriptCode)
        return script(self.dbUrl,self.dbTables,self.dbConfig)