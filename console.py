#coding=utf-8
import logging,sys,os
from autoFramework.Application import *
from config import config

class runTest:
    def __init__(self):
        pass
    
    def RunTest(self):
        #定义日志级别
        logLevelGrade=config.LogLevel
        logSetting=logApi.logDefine()
        logSetting.logApi()        
        #定义测试套件
        testcaseCreateNeedKey=config.InterfaceTest["TestcaseCreateKey"]
        testSuiteObject=testApi.testDefine()
        testSuit=testSuiteObject.testGenerationApi(testcaseCreateNeedKey)
        #刷新测试用例目录的__init__.py文件
        #定义测试报告
        ReportTitle=config.InterfaceTest["ReportTitle"]
        runnerTupleObject=reportApi.reportDefine()
        runnerTuple=runnerTupleObject.reportApi()
        #执行测试用例
        runnerTuple[0].run(testSuit)
        runnerTuple[1].close()
        #判断是否需要发送邮件
        EmailKey=config.InterfaceTest["EmailKey"]
        if EmailKey=='Y':
            eMail=mailApi.mailDefine()
            eMail.sendMailApi()
        else:
            pass
    
if __name__=='__main__':
    run=runTest()
    run.RunTest()