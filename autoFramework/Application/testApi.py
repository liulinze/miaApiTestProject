#coding=utf-8
import os,json,sys,logging
from Core import testcaseFunction
from Core import testsuitFunction
from Core import authenticationFunction
from config import config

class testcaseDefine:
    #初始化当前类所使用到的文件路径：参数路径，authsession参数路径
    def __init__(self):
        self.paraPath=config.autoFrameworkPathSetDic["paraPath"]
        self.authsessionParaPath=config.autoFrameworkPathSetDic["authsessionParaPath"]
        
    #Testcase参数读取和处理方法，从原始数据里读取参数，并处理成为相应的参数列表并返回
    def testcaseParaCreateApi(self):
        OriginalParasDic={}
        for root,dirs,files in os.walk(self.paraPath):
            for fileName in files:
                path=os.path.join(root,fileName).replace("\\","/")
                OriginalParasDic[fileName[:-5]]=path
        allTestcaseList=[]
        for key in OriginalParasDic.keys():
            interfaceClassFile=[]
            interfaceClassFile.append("Testcase_"+key)
            try:
                OriginalParaList=eval(open(OriginalParasDic[key]).read())
            except Exception as e:
                print(e)
                print(u"原始参数读取错误!")
            interfaceClassFile.append(OriginalParaList)
            allTestcaseList.append(interfaceClassFile)
        return allTestcaseList
    
    #调用当前类的Testcase参数读取方法，读取参数，然后调用Core模块的Testcase创建类，创建Testcase文件到指定目录
    def testcaseCreateApi(self):
        testcaseParas=self.testcaseParaCreateApi()
        testcaseCreateProcess=testcaseFunction.testcase()
        testcaseCreateProcess.create(testcaseParas)
        testcaseCreateProcess.initFileSet()

class testsuitDefine:
    #初始化当前类所使用到的文件路径：testcase路径
    def __init__(self):
        self.testcasePath=config.autoFrameworkPathSetDic["testcasePath"]
        
    #读取Testcase目录下所有用例文件，自动生成TestcaseList，供组织TestSuit使用，返回testcase列表       
    def testcaseListCreateApi(self):
        TestcaseList=[]            
        key=0
        exec("sys.path.append(os.path.dirname(self.testcasePath))")
        exec("from testcase import *")
        for root,dirs,files in os.walk(self.testcasePath):
            if key>=1:
                break
            else:            
                for file in files:
                    if file[-2:]=='py' and file[:-3]!='__init__':
                        moudle=eval(file[:-3])
                        moudle = getattr(moudle,file[:-3],"error")
                        TestcaseList.append(moudle)
            key=key+1
        return TestcaseList
    
    #创建Testsuit，供测试进程调用。
    def testsuitCreateApi(self):
        waitTestCaseList=self.testcaseListCreateApi()
        testsuitCreateProcess=testsuitFunction.testsuit()
        testSuit=testsuitCreateProcess.create(waitTestCaseList)
        return testSuit

#整合以上两个类，完成测试用例创建和测试用例套件组织功能
class testDefine:
    def __init__(self):
        pass
    
    def testGenerationApi(self,testcaseCreateNeedKey):
        #创建登录标记authSession
        loginMark=authenticationFunction.authentication()
        loginMark.authSessionCreate()
        if testcaseCreateNeedKey=='Y':
            #完成测试用例创建
            testcaseGeneration=testcaseDefine()
            testcaseGeneration.testcaseCreateApi()
        else:
            pass
        #完成测试用例套件组织
        testsuitObjCreate=testsuitDefine()
        testsuitObject=testsuitObjCreate.testsuitCreateApi()
        return testsuitObject
    
if __name__=='__main__':
    a=testDefine()
    aaa=a.testGenerationApi("Y")
