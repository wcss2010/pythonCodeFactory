#-*- coding:utf-8 -*-
import sys
import os
import pathlib
import json
import js2py

class JsCompileTool(object):
    def __init__(self,jsCode,dbUrl,tables):
        self.scriptCode = jsCode
        self.dbUrl = dbUrl
        self.dbTables = tables
    def execute(self):
        script = js2py.eval_js(self.scriptCode)
        return script(self.dbUrl,self.dbTables)