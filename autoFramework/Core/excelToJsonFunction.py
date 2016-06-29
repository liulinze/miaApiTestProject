#coding=utf-8
import xlrd,json,datetime,os
from config import config

class excelToJson:
    #初始化excel参数化文件的路径
    def __init__(self):
        self.excelParasPath=config.autoFrameworkPathSetDic["excelParasPath"]
        self.paraPath=config.autoFrameworkPathSetDic["paraPath"]
    
    #获取所有excel文件的名称  
    def readAllExcelFile(self):
        excelFileNameList=[]
        for root,dirs,files in os.walk(self.excelParasPath):
            for fileName in files:
                if fileName[-4:]!="xlsx":
                    pass
                else:
                    excelFileNameList.append(fileName)
        return excelFileNameList
    
    def createProjectPath(self):
        

    '''
        workbook=xlrd.open_workbook(config.autoFrameworkPathSetDic["excelParasPath"]+'/sample.xlsx')

        table=workbook.sheets()[0]

        rows=table.nrows
        cols=table.ncols
        #读取第一行的数据，读取前5000行，返回所有有数据的列号
    '''

    def testOrderCreate(row):
        #创建testOrder组
        #判断当前行的第二列是否为空
        if len(int(row[1]))!=0:
            testOrder={}
            #不为空，则处理第二列到第五列数据，第八到第十一列数据分别赋值给testOrder的参数
            testOrder["BaseUrlNum"]=str(int(row[1]))
            testOrder["requestMethod"]=str(row[2])
            testOrder["requestInterfaceName"]=str(row[3])
            testOrder["requestParas"]=eval(row[4])
            if len(str(row[9]))!=0:
                testOrder["isNeedOutput"]=str(row[9])
            if len(str(row[10]))!=0:
                testOrder["isNeedAuthsession"]=str(row[10])
            if len(str(row[11]))!=0:
                testOrder["isNeedCycle"]=str(row[11])
            testOrderArray.append(testOrder)
            return testOrder


    def testOrderArrayCreate(row):
        #for i in range(2,rows)
        if int(row[1])==1:
            testOrderArray=[]
            testOrderCreate(row)
        else:
            testOrderCreate(row)
        
    def caseCreate(row,rowNum):
        caseDic={}
        if len(str(row[0]))!=0:
            #不为空则将第一列的值赋值给caseDic的TestcaseMethodName字段，并将之添加到caseArray中
            caseDic["TestcaseMethodName"]=str(row[0])
        else:
            pass
    
        if len(str(row[12]))!=0:
            caseDic["isNeedCleanCart"]=str(row[12])
        else:
            pass
        return caseDic
    
    def caseArrayCreate():
        #创建case列表
        caseArray=[]
        #循环获取行数据，从第三行开始
        for i in range(2,rows):
            #获取当前行的值
            row=table.row_values(i)
            caseDic=caseCreate(row,i)
            if len(caseDic)>0:
                caseArray.append(caseDic)
            else:
                pass
            
        return caseArray
    
if __name__=="__main__":
    excelFunction=excelToJson()
    print(excelFunction.readAllExcelFile())
    
    
"""        
testOrder=[]
interfaceDic={}
resultJudgeArray=[]
for i in range(2,rows):
    row=table.row_values(i)
    if len(str(row[0]))!=0:
        caseDic["TestcaseMethodName"]=row[0]
    else:
        pass
    print(str(row[1]))
    if len(str(row[1]))!=0:
        interfaceDic["BaseUrlNum"]=str(int(row[1]))
        interfaceDic["requestMethod"]=str(row[2])
        interfaceDic["requestInterfaceName"]=str(row[3])
        interfaceDic["requestParas"]=eval(row[4])
    else:
        pass
    testOrder.append(interfaceDic)
print(testOrder)
print(caseDic)
"""          
        
        
        

#读取第一个有数据的位置，然后位置列号，开始依次读取有效值，付给变量


