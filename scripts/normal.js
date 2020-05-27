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
//   "adapters": {
//      "OracleDBCode": {
//          "title": "Oracle",
//          "command": "java -version",
//          "inputFile": "input.json",
//          "outputFile": "output.json"
//          "responseCoding": "gbk"
//      }
//  },
//  "codeFileExtName": ".cs",
//  "classNameBefore": "t",
//  "classNameAfter": "Object",
//  "classNamespace": "com.example"
//  "dialogRootDir": "~/"
//}
//
// 返回结果为一个Json字符串，格式如下：
//  {
//     "代码段名称1(在实体和DAO脚本中为文件名去掉.cs)":"代码内容",
//     "代码段名称2(在实体和DAO脚本中为文件名去掉.cs)":"代码内容",
//     "代码段名称3(在实体和DAO脚本中为文件名去掉.cs)":"代码内容",
//     "代码段名称4(在实体和DAO脚本中为文件名去掉.cs)":"代码内容"
//  }
//

//添加内容到Json串缓冲
function appendToJson(buffer,codeName,codeContent)
{
	if (buffer==""){
	   buffer =  buffer + "\"" + codeName + "\":\"" + codeContent + "\"";
	}else{
	   buffer =  buffer +  ",\"" + codeName + "\":\"" + codeContent + "\"";
	}
	return buffer;
}
//用于模仿C#下的StringBuilder.Append
function appendTo(buffer,content)
{
	return buffer + content;	
}
//用于模仿C#下的StringBuilder.AppendLine
function appendLineTo(buffer,content)
{
	return buffer + content + "\\r\\n";
}

//入口函数
function script(url,table,config)
{
   //取表名
   var tableName = table["tableName"];
   //取名称空间
   var namespace = config["classNamespace"]
   //清空Json串缓冲
   var jsonBuffer="";   
   //字符缓冲1
   var tempStr1 = "";
   //字符缓冲2
   var tempStr2 = "";
   
   //例子查询语句
   tempStr1 = appendLineTo(tempStr1,"select * from " + tableName + " where xx = '值'");
   tempStr1 = appendLineTo(tempStr1,"select * from " + tableName + " where xx = '值'");
   tempStr1 = appendLineTo(tempStr1,"select * from " + tableName + " where xx = '值'");
   tempStr1 = appendLineTo(tempStr1,"select * from " + tableName + " where xx = '值'");
   tempStr1 = appendTo(tempStr1,"select * from " + tableName + " where xx = '值'");
   
   //例子更新语句
   tempStr2 = appendLineTo(tempStr2,"update " + tableName + " set xx = '值' where xx = '值'");
   tempStr2 = appendLineTo(tempStr2,"update " + tableName + " set xx = '值' where xx = '值'");
   tempStr2 = appendLineTo(tempStr2,"update " + tableName + " set xx = '值' where xx = '值'");
   tempStr2 = appendLineTo(tempStr2,"update " + tableName + " set xx = '值' where xx = '值'");
   tempStr2 = appendTo(tempStr2,"update " + tableName + " set xx = '值' where xx = '值'");
   
   //加入代码段1
   jsonBuffer=appendToJson(jsonBuffer,"xx查询语句代码段",tempStr1);
   //加入代码段2
   jsonBuffer=appendToJson(jsonBuffer,"xx更新语句代码段",tempStr2);
   
   //返回Json字符串
   return "{" + jsonBuffer + "}";
}