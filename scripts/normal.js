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

//用于模仿C#下的StringBuilder.Append
function append(buffer,content)
{
   buffer.push(content);
}
//用于模仿C#下的StringBuilder.AppendLine
function appendLine(buffer,content)
{
    buffer.push(content);
    buffer.push("\\r\\n");
}
//用于模仿C#下的StringBuilder.ToString()
function toString(buffer)
{
    return buffer.join("");
}

//开始Json
function beginJson(buffer)
{
   buffer.push("{");
}
//结束Json
function endJson(buffer)
{
   buffer.push("}");
}
//添加内容到Json串缓冲
function appendToJson(buffer,codeName,codeContent)
{
   //判断是否前面已经数据
   if (buffer.length == 1)
   {
      buffer.push("");
   }else
   {
      buffer.push(",");
   }
   //拼装数据
   buffer.push("\"");
   buffer.push(codeName);
   buffer.push("\"");
   buffer.push(":");
   buffer.push("\"");
   buffer.push(codeContent);
   buffer.push("\"");
}

//入口函数
function script(url,table,config)
{
   //取表名
   var tableName = table["tableName"];
   //取名称空间
   var namespace = config["classNamespace"]
   //Json缓冲
   var jsonBuf= new Array();
   //字符缓冲1
   var tempBuf1= new Array();
   //字符缓冲2
   var tempBuf2= new Array();
   
   //开始Json
   beginJson(jsonBuf);
   
   //拼装例子1
   var columns = table["columns"];
   for(var k = 0;k < columns.length;k++)
   {
      var colObj = columns[k];
      var colName = colObj["name"];
      append(tempBuf1,colName + ",");
   }

   //拼装例子2
   appendLine(tempBuf2,"update " + tableName + " set xx = '值' where xx = '值'");
   appendLine(tempBuf2,"update " + tableName + " set xx = '值' where xx = '值'");
   appendLine(tempBuf2,"update " + tableName + " set xx = '值' where xx = '值'");
   appendLine(tempBuf2,"update " + tableName + " set xx = '值' where xx = '值'");

   //加入代码段1
   appendToJson(jsonBuf,"xx查询语句代码段_常用",toString(tempBuf1));
   //加入代码段2
   appendToJson(jsonBuf,"xx更新语句代码段_常用",toString(tempBuf2));

   //结束Json
   endJson(jsonBuf);

   //返回Json字符串
   return toString(jsonBuf);
}