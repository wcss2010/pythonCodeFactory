#-*- coding:utf-8 -*-
import sys
import os
import shutil
from UtilTool import *
import pathlib
from BaseAdapters import *

class AppConfigSchemaAdapter(BaseAdapter):
    def getTables(self,dbUrl,dbAdapterInfo):
       schemaObj = SchemaDB("main",dbUrl,dbAdapterInfo)
       
       return schemaObj