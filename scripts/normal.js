//
//入口函数
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
//     "代码段名称1(在实体和DAO脚本中为文件名去掉.cs)":"代码内容"
//     "代码段名称2(在实体和DAO脚本中为文件名去掉.cs)":"代码内容"
//     "代码段名称3(在实体和DAO脚本中为文件名去掉.cs)":"代码内容"
//     "代码段名称4(在实体和DAO脚本中为文件名去掉.cs)":"代码内容"
//
function script(url,table,config)
{
   //取表名
   var tableNames = table["tableName"];
   //取名称空间
   var namespaces = config["classNamespace"]
   return "{\"" + tableName + "\"Entity:\"Entity内容_常用\",\"" + tableName + "DAO\":\"DAO内容_常用\"}";
}