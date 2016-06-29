#coding=utf-8
import pymysql

class databaseFunction:
    def __init__(self):
        pass    
    
    def createDbConnect(self,connectPara):
        print(connectPara)
        dbConnectObject=pymysql.connect(host=connectPara["host"],
                             port=connectPara["port"],
                             user=connectPara["user"],
                             passwd=connectPara["passwd"],
                             db=connectPara["db"],
                             charset='utf8')
        dbCursorObject=dbConnectObject.cursor()
        return (dbConnectObject,dbCursorObject)
            
    def closeDbConnect(self,connectObject,cursorObject):
        cursorObject.close()
        connectObject.close()        
                
    def runSql(self,connectPara,sqlStr):
        dbConnect=self.createDbConnect(connectPara)
        connectObject=dbConnect[0]
        cursorObject=dbConnect[1]
        sqlStart=sqlStr.startswith("SELECT")
        try:
            cursorObject.execute(sqlStr)
            for result in cursorObject.fetchall:
                print (result)
        except Exception as e:
            if sqlStart == False:
                cursorObject.rollback()
            else:
                pass
            self.closeDbConnect(connectObject, cursorObject)
            raise ValueError("sql执行错误："+str(e))
        self.closeDbConnect(connectObject, cursorObject)
        
if __name__=="__main__":
    db=databaseFunction()
    connectPara={
        "host":"172.16.104.207",
        "port":3307,
        "user":"write_user",
        "passwd":"write_user",
        "db":"mia_test2"
    }
    sqlStr="SELECT * FROM item WHERE id='1000000';"
    db.runSql(connectPara, sqlStr)
    