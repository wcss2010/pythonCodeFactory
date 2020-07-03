//使用说明：
//入口函数为 function script(url,table,config)
//url=数据库连接代码
//table=格式为：
// {
//    "tableName":"XXX"
//    "tableType":"table"
//    "columns":[
//                 {"name":"ID","type":"bigint","notnull":"true","pk":"true"}
//                 {"name":"Name","type":"nvarchar(200)","notnull":"false","pk":"false"}
//                 {"name":"Sex","type":"nvarchar(5)","notnull":"false","pk":"false"}
//                 {"name":"Age","type":"int","notnull":"false","pk":"false"}
//              ]
// }
//config=格式为:
//{
//    "dbPlugins": {
//        "xxxxCode": {
//            "title": "xxxDB",
//            "code": "xxxxCode",
//            "command": "python3 {local}/xxx.py {input} {output}",
//            "responseCoding": "utf8"
//        }
//    },
//    "codeFileExtName": ".cs",
//    "classNameBefore": "t",
//    "classNameAfter": "Object",
//    "classNamespace": "com.example",
//    "dialogRootDir": "~/"
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
function script(url,table,config)
{
   //引用内置的Python工具集
   pyimport globaltool;
   //
   // （1）cfenv（环境变量）
   //     rootDir(主目录变量) binDir(程序目录变量) dataDir(数据目录变量) dbPluginDir(插件目录变量) scriptDir(脚本目录变量) attachDir(附件目录变量)
   //  (2) stringbuffer(类似于C#中的StringBuilder)
   //     enterFlag(回车点位符变量) clear(清理函数,参数：空) append(添加字符串函数,参数：字符串) appendLine(添加字符串并在末尾加回车函数,参数：字符串) fromString(载入非Base64字符串到缓冲区,参数：字符串) toString(输出可显示字符串,参数：空) fromB64String(解码并装载Base64字符串,参数：字符串) toB64String(将缓冲区内容编码为Base64字符串,参数：空)
   //  (3) jsoncodewriter(Json代码块生成)
   //     append(添加代码块,参数：字符串)  remove(删除代码块,参数：字符串)  toString(输出代码块到JSON字符串,参数：空)
   //  (4) iotool(读写工具类)
   //     start(运行指令并等待返回结果,参数：命令字符串，返回结果字符集) readAllText(读入所有文本,参数：文件路径) readAllByte(读入所有字节,参数：文件路径) writeAllText(写入所有文本,参数：文件路径,要写入的文本) writeAllByte(写入所有字节,参数：文件路径,要写入的字节集)
   //
   //

   //取表名
   var tableName = table["tableName"];
   //取名称空间
   var namespace = config["classNamespace"]
   
   //JSON代码块生成
   var jsonCodeMaker = globaltool.jsoncodewriter();
   
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

   //代码块例子3
   var sb3 = globaltool.stringbuffer();
   pyimport os;
   sb3.appendLine(globaltool.iotool.readAllText(os.path.join(globaltool.cfenv.rootDir,'config.json')));

   //添加代码块1
   jsonCodeMaker.append('第一个例子',sb1.toB64String());
   //添加代码块2
   jsonCodeMaker.append('第二个例子',sb2.toB64String());
   //添加代码块3
   jsonCodeMaker.append('第三个例子',sb3.toB64String());

   //返回Json字符串
   return jsonCodeMaker.toString();
}