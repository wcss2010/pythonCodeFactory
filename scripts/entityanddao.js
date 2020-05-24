//
//入口函数
//url=数据库连接代码
//table=格式为：
// {
//    "tableName":"XXX"
//    "tableType":"table"
//    "columns":[
//                 {"name":"ID","type":"bigint"}
//                 {"name":"Name","type":"nvarchar(200)"}
//                 {"name":"Sex","type":"nvarchar(5)"}
//                 {"name":"Age","type":"int"}
//              ]
// }
//
function script(url,table)
{
   return "生成实体和DAO代码! ";
}