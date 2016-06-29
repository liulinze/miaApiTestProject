#coding=utf-8
import os,sys
from string import Template
from config import config
from authenticationFunction import authentication

class testcaseTemplate():
    def __init__(self):
        self.templatePath=config.autoFrameworkPathSetDic["templatePath"]
        self.authsessionParaPath=config.autoFrameworkPathSetDic["authsessionParaPath"]
        
    def singleAssertCreate(self,judgeValue):
        templateMethodStr=open(self.templatePath+"/testcaseAssert.template").read()
        code=Template("\n"+templateMethodStr+"\n")
        methodCode = code.substitute(caseJudgeValue=judgeValue)
        return methodCode        
    
    def allAssertCreate(self,orderMember):
        allAssertCode=""
        for caseJudgeValue in orderMember["resultJudge"]:
            string=self.singleAssertCreate(caseJudgeValue)
            allAssertCode=allAssertCode+string
        return allAssertCode
        
    def testCycleCodeCreate(self,orderMember):
        templateMethodStr=open(self.templatePath+"/testcaseRequestForCycle.template").read()
        code=Template("\n"+templateMethodStr+"\n")
        assertCode=self.allAssertCreate(orderMember)
        try:
            outputMark=orderMember["isNeedOutput"]
        except Exception as e:
            outputMark="N"        
        try:
            cycleMark=orderMember["isNeedCycle"]
        except Exception as e:
            cycleMark="N"
        try:
            authenticationMark=orderMember["isNeedAuthsession"]
        except Exception as e:
            authenticationMark="Y"
        methodCode = code.substitute(requestMethod=orderMember["requestMethod"],url=config.BaseURL[int(orderMember["BaseUrlNum"])-1],
                                             path=orderMember["requestInterfaceName"],paras=orderMember["requestParas"],
                                             outputPara=outputMark,cycleParas=cycleMark,authentication=authenticationMark,testAssert=assertCode)
        return methodCode        
        
                
    def testOrderCodeCreate(self,orderMember):
        templateMethodStr=open(self.templatePath+"/testcaseRequest.template").read()
        code=Template("\n"+templateMethodStr+"\n")
        assertCode=self.allAssertCreate(orderMember)
        try:
            outputMark=orderMember["isNeedOutput"]
        except Exception as e:
            outputMark="N"
        try:
            authenticationMark=orderMember["isNeedAuthsession"]
        except Exception as e:
            authenticationMark="Y"        
        methodCode = code.substitute(requestMethod=orderMember["requestMethod"],url=config.BaseURL[int(orderMember["BaseUrlNum"])-1],
                                     path=orderMember["requestInterfaceName"],paras=orderMember["requestParas"],
                                     outputPara=outputMark,authentication=authenticationMark,
                                     testAssert=assertCode)
        return methodCode        
    
        
    #生成接口测试用例方法
    def singleMethodCreate(self,interfaceNamePara,MethodPara,CaseNum):
        methodName=interfaceNamePara[8:]+"_"+str(CaseNum)
        orderCode=""
        try:
            cleanCartNeed=MethodPara["isNeedCleanCart"]
        except Exception as e:
            cleanCartNeed="N"
                
        for orderMember in MethodPara["TestOrder"]:
            try:
                cycleMark=orderMember["isNeedCycle"]
            except Exception as e:
                cycleMark="N"            
            if cycleMark=="N":
                string=self.testOrderCodeCreate(orderMember)
            else:
                string=self.testCycleCodeCreate(orderMember)
            orderCode=orderCode+string
        templateMethodStr=open(self.templatePath+"/testcaseMethod.template").read()
        code=Template("\n"+templateMethodStr+"\n")
        methodCode = code.substitute(testcase=methodName,cleanCartMark=cleanCartNeed,testcaseName=MethodPara["TestcaseMethodName"],
                                     testOrder=orderCode)
        return methodCode
    
    #拼接单个的测试用例函数字符串为完整字符串并传回主函数
    def allMethodCreate(self,interfaceNamePara,MethodParaList):
        allMethodCode=""
        key=1
        for MethodPara in MethodParaList:
            string=self.singleMethodCreate(interfaceNamePara,MethodPara,key)
            allMethodCode=allMethodCode+string
            key=key+1
        return allMethodCode
    
    #生成测试用例类函数字符串
    def modelClassCreate(self,parameters):
        modelCode=self.allMethodCreate(parameters[0],parameters[1])
        interfaceNameValue="/"+parameters[0][9:].replace("_","/")
        templateClassStr=open(self.templatePath+"/testcaseClass.template").read()
        code = Template(templateClassStr)
        testcaseCode = code.substitute(className=parameters[0],interfaceName=interfaceNameValue,model=modelCode)
        return testcaseCode


if __name__=="__main__":
    bbb=testcaseTemplate()
    interfaceNamePara= "bbb"
    MethodParaList=[
    {
    "TestcaseMethodName": "168-1有效可单独售卖的有库存且仓库属于1、6、8的特卖商品---sku仅存在于有效未开始特卖中---下单成功",
    "isNeedCleanCart": "Y",
    "TestOrder": [
            {
                "BaseUrlNum":"1",
                "requestMethod":"post",
                "requestInterfaceName":"/topcart/add",
                "requestParas":{"item_id": "1000023","item_size": "SINGLE","quantity": "1"},
                "resultJudge":[{"assertExpect":"200","assertResult":"code","assertGrade":"1","assertThirdLevelName":"None"}
                        ],
                "isNeedInput":"N",
                "isNeedOutput":"N",
                "isNeedAuthsession":"Y",
                "isNeedCycle":"N"
            },
            {
                "BaseUrlNum":"2",
                "requestMethod":"post",
                "requestInterfaceName":"/order/checkout",
                "requestParas":{"params": '{"ck_type": "1","user_id": "4238217","channel": "4","sub_channel": "4.1.0|","ip": "127.0.0.1","from": "4","client_version": "4_1_0"}',"version":"3_0"},
                "resultJudge":[{"assertExpect":"200","assertResult":"code","assertGrade":"1","assertThirdLevelName":"None"}
                        ],
                "isNeedInput":"N",
                "isNeedOutput":"N",
                "isNeedAuthsession":"N",
                "isNeedCycle":"N"
            },
            {
                "BaseUrlNum":"2",
                "requestMethod":"post",
                "requestInterfaceName":"/order/create",
                "requestParas":{"params":'{"ck_type": "1","user_id": "4238217","address_id":"1813582","channel":"4","sub_channel":"4.1.0|","ip": "127.0.0.1","pay_mode":"3","dst_mode":"1","from":"4"}',"version":"3_0"},
                "resultJudge":[{"assertExpect":"200","assertResult":"code","assertGrade":"1","assertThirdLevelName":"None"},
                               {"assertExpect":"100","assertResult":"bbb","assertGrade":"2","assertThirdLevelName":"None"},
                               {"assertExpect":"kkk","assertResult":"nnn","assertGrade":"3","assertThirdLevelName":"ppp"},
                        ],
                "isNeedInput":"N",
                "isNeedOutput":"ck_superior_order_code",
                "isNeedAuthsession":"N",
                "isNeedCycle":"N"
            },
            {
                "BaseUrlNum":"3",
                "requestMethod":"post",
                "requestInterfaceName":"/order/result",
                "requestParas":{"ck_superior_order_code":"None","user_id":"4238217"},
                "resultJudge":[{"assertExpect":"True","assertResult":"result","assertGrade":"0","assertThirdLevelName":"None"}
                        ],
                "isNeedInput":"Y",
                "isNeedOutput":"ck_superior_order_code",
                "isNeedAuthsession":"Y",
                "isNeedCycle":{"paraWant":"result","judegValue":"2","stopNum":"15"}
            }
        ]
    }
]
    print(bbb.allMethodCreate(interfaceNamePara, MethodParaList))