//使用说明：
//入口函数为 function script(dbUrl,tableData,dbPluginConfig)
//dbUrl=数据库连接代码
//tableData=格式为：
// {
//    "tableName":"XXX"  表名
//    "tableType":"table"  表类型
//    "columns":[  列
//                 {"name":"ID","type":"bigint","notnull":"true","pk":"true"}   列名，列类型，是否为空，是否为主键
//                 {"name":"Name","type":"nvarchar(200)","notnull":"false","pk":"false"} 列名，列类型，是否为空，是否为主键
//                 {"name":"Sex","type":"nvarchar(5)","notnull":"false","pk":"false"} 列名，列类型，是否为空，是否为主键
//                 {"name":"Age","type":"int","notnull":"false","pk":"false"} 列名，列类型，是否为空，是否为主键
//              ]
// }
//dbPluginConfig=格式为:
//{
//            "title": "xxxDB",  标题
//            "code": "xxxxCode",  识别码
//            "command": "python3 {local}/xxx.py {input} {output}", 命令行配置
//            "responseCoding": "utf8"  命令行返回的字节集
//}
//
// 返回结果为一个Json字符串，格式如下：
//  {
//     "代码段名称1(在实体和DAO脚本中为文件名去掉.cs)":"代码内容(需要转换成Base64编码，以保证 \ " ' / ? 等符号不会干扰JSON解析)",
//     "代码段名称2(在实体和DAO脚本中为文件名去掉.cs)":"代码内容(需要转换成Base64编码，以保证 \ " ' / ? 等符号不会干扰JSON解析)",
//     "代码段名称3(在实体和DAO脚本中为文件名去掉.cs)":"代码内容(需要转换成Base64编码，以保证 \ " ' / ? 等符号不会干扰JSON解析)",
//     "代码段名称4(在实体和DAO脚本中为文件名去掉.cs)":"代码内容(需要转换成Base64编码，以保证 \ " ' / ? 等符号不会干扰JSON解析)"
//  }
//

//入口函数
function script(dbUrl,tableData,dbPluginConfig)
{
   //引用内置的Python工具集
   pyimport globaltool;
   //
   // （1）cfenv（环境变量）
   //     rootDir(主目录变量) binDir(程序目录变量) dataDir(数据目录变量) dbPluginDir(插件目录变量) scriptDir(脚本目录变量) attachDir(附件目录变量) configFilePath(配置文件路径变量) backupConfigFilePath(备份配置文件路径变量) templeteScriptFile(标准的脚本模板) scriptEnvDir(脚本环境目录变量) normalScriptFile(常用代码脚本路径变量) entityAndDAOScriptFile(实体和DAO代码脚本路径变量) configObj（系统配置变量）
   //  (2) stringbuffer(类似于C#中的StringBuilder)
   //     enterFlag(回车点位符变量) clear(清理函数,参数：空) append(添加字符串函数,参数：字符串) appendLine(添加字符串并在末尾加回车函数,参数：字符串) fromString(载入非Base64字符串到缓冲区,参数：字符串) toString(输出可显示字符串,参数：空) fromB64String(解码并装载Base64字符串,参数：字符串) toB64String(将缓冲区内容编码为Base64字符串,参数：空)
   //  (3) jsondict(Json字典)
   //     addOrUpdate(添加或更新,参数：名称，内容) remove（删除,参数：名称） load(载入Json字典，参数：Json字符串) loadFile(载入Json字典从文件，参数：Json文件路径) loadFileFromScriptDir(载入Json字典从ScriptDir中的文件,参数：Json文件名) saveFile(保存Json字典到文件,参数：Json文件路径) saveFileToScriptDir(保存Json字典到ScriptDir中的文件,参数：Json文件名) getValue(获得键值，参数：名称，初始值) items(字典缓存中的items()函数) keys(字典缓存中的keys()函数) clear(字典缓存中的clear()函数) count(字典记录数) toJsonString(输出Json串)
   //  (4) iotool(读写工具类)
   //     start(运行指令并等待返回结果,参数：命令字符串，返回结果字符集) readAllText(读入所有文本,参数：文件路径) readAllByte(读入所有字节,参数：文件路径) writeAllText(写入所有文本,参数：文件路径,要写入的文本) writeAllByte(写入所有字节,参数：文件路径,要写入的字节集)
   //  (5) codemaker(模板文件替换生成类，模板中的占位符：$%占位符%$
   //     kvData(关键字字典变量，类型为jsondict，可使用对应的函数) loadTemplete(载入模板，参数：模板数据字符串) loadTempleteFile(从文件载入模板，参数：模板文件路径) loadTempleteFileFromScriptDir（从ScriptDir载入模板文件,参数：模板文件名） execute(根据kvData中的字典执行字符串替换，返回结果为stringbuffer变量)
   //

   //取表名
   var tableName = tableData["tableName"];
   //取名称空间
   var namespace = globaltool.cfenv.configObj["classNamespace"]
   //数据库类型
   var dbType = dbPluginConfig['code']

   //JSON代码块生成
   var jsonCodeMaker = globaltool.jsondict();
   
   //代码块例子1
   var sb1 = globaltool.stringbuffer();
   sb1.append('update ').append(tableName).append(' set xxx = \"\" where xx = 1').appendLine('');
   sb1.append('update ').append(tableName).append(' set xxx = \"\" where xx = 1').appendLine('');
   sb1.append('update ').append(tableName).append(' set xxx = \"\" where xx = 1').appendLine('');
   sb1.append('update ').append(tableName).append(' set xxx = \"\" where xx = 1').appendLine('');
   sb1.append('例子1').append(globaltool.stringbuffer.enterFlag);
   sb1.append('例子2').append(globaltool.stringbuffer.enterFlag);
   sb1.appendLine('例子3');
   sb1.appendLine('例子4');

   //代码块例子2
   var sb2 = globaltool.stringbuffer();
   sb2.appendLine(globaltool.cfenv.dataDir);
   sb2.appendLine(globaltool.cfenv.dbPluginDir);
   sb2.appendLine(globaltool.cfenv.scriptDir);
   sb2.appendLine(globaltool.cfenv.attachDir);
   sb2.appendLine(namespace);

   //代码块例子3
   var sb3 = globaltool.stringbuffer();
   pyimport os;
   sb3.fromString(globaltool.iotool.readAllText(os.path.join(globaltool.cfenv.rootDir,'config.json')));

   //代码块例子4
   var cm4 = globaltool.codemaker()
   cm4.loadTempleteFileFromScriptDir('templete.txt')
   cm4.kvData.addOrUpdate('colA','一地在要工');
   cm4.kvData.addOrUpdate('colB','上是中国同');
   var sb4 = cm4.execute();

   //代码块例子5
   var jd5 = globaltool.jsondict();
   jd5.loadFileFromScriptDir('test.json');
   var sb5 = globaltool.stringbuffer();
   sb5.append('属性1：').appendLine(jd5.getValue('rowA','空值1'));
   sb5.append('属性2：').appendLine(jd5.getValue('rowB','空值2'));

   //代码块例子6
   var sb6 = globaltool.stringbuffer();
   var keyss = jd5.keys();
   for(var k in keyss)
   {
      var key = keyss[k];
      sb6.append("Key:").append(jd5.getValue(key,"none"));
   }

   //添加代码块1
   jsonCodeMaker.addOrUpdate('第一个例子',sb1.toB64String());
   //添加代码块2
   jsonCodeMaker.addOrUpdate('第二个例子',sb2.toB64String());
   //添加代码块3
   jsonCodeMaker.addOrUpdate('第三个例子',sb3.toB64String());
   //添加代码块4
   jsonCodeMaker.addOrUpdate('第四个例子',sb4.toB64String());
   //添加代码块5
   jsonCodeMaker.addOrUpdate('第五个例子',sb5.toB64String());
   //添加代码块6
   jsonCodeMaker.addOrUpdate('第六个例子',sb6.toB64String());

   //返回Json字符串
   return jsonCodeMaker.toJsonString();
}