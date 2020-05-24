#-*- coding:utf-8 -*-
import sys
import os
import shutil
import UtilTool
import pathlib
from BaseAdapter import *

class AppConfigSchemaAdapter(BaseAdapter):
    def getTables(self,dbUrl,dbAdapterInfo):
       schemaObj = SchemaDB("main",dbUrl,dbAdapterInfo)       
       return schemaObj