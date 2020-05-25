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
//      }
//  },
//  "codeFileExtName": ".cs",
//  "classNameBefore": "t",
//  "classNameAfter": "Object",
//  "classNamespace": "com.example"
//}
//
function script(url,table,config)
{
   return "生成常用代码! ";
}