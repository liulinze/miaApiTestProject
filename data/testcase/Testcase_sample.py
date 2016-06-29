#coding: utf-8
        
"""
功能：待执行的接口测试用例
用法：通过框架自动触发调用
"""
    
import unittest,requests,datetime,sys,os,json,logging
from Application import resultApi
from config import config
from Core import authenticationFunction

class Testcase_sample(unittest.TestCase):
    u"""待测试用例集：/sample"""
    def setUp(self):
        self.authsessionParaPath=config.autoFrameworkPathSetDic["authsessionParaPath"]
            
    def tearDown(self):
        pass
            
    
    def test_sample_1(self,input=None):
        u"""示例用例1"""
        start=datetime.datetime.now()
        resultProcess=resultApi.resultDefine()
        authenticatedPara=authenticationFunction.authentication()
        if "Y"=="Y":
            authenticatedPara.cleanCart()
        else:
            pass
        
        if input==None:
            paras={'quantity': '1', 'item_id': '1056879', 'item_size': 'SINGLE'}
        else:
            paras={'quantity': '1', 'item_id': '1056879', 'item_size': 'SINGLE'}
            paras["N"]=input["N"]
        if "Y"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://api.miyabaobei.com","/topcart/add"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "N"!="N":
            input={"N":result["content"]["N"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'params': '{"ck_type": "1","user_id": "4238217","channel": "4","sub_channel": "4.1.0|","ip": "127.0.0.1","from": "4","client_version": "4_1_0"}', 'version': '3_0'}
        else:
            paras={'params': '{"ck_type": "1","user_id": "4238217","channel": "4","sub_channel": "4.1.0|","ip": "127.0.0.1","from": "4","client_version": "4_1_0"}', 'version': '3_0'}
            paras["N"]=input["N"]
        if "N"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://ckapi.mia.com/cksrv","/order/checkout"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "N"!="N":
            input={"N":result["content"]["N"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass

        caseJudgeValue={'assertExpect': '99', 'assertGrade': '3', 'assertThirdLevelName': 'cart_total', 'assertResult': 'pay_price'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'params': '{"ck_type": "1","user_id": "4238217","address_id":"1813582","channel":"4","sub_channel":"4.1.0|","ip": "127.0.0.1","pay_mode":"3","dst_mode":"1","from":"4"}', 'version': '3_0'}
        else:
            paras={'params': '{"ck_type": "1","user_id": "4238217","address_id":"1813582","channel":"4","sub_channel":"4.1.0|","ip": "127.0.0.1","pay_mode":"3","dst_mode":"1","from":"4"}', 'version': '3_0'}
            paras["ck_superior_order_code"]=input["ck_superior_order_code"]
        if "N"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://ckapi.mia.com/cksrv","/order/create"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "ck_superior_order_code"!="N":
            input={"ck_superior_order_code":result["content"]["ck_superior_order_code"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'user_id': '4238217', 'ck_superior_order_code': 'None'}
        else:
            paras={'user_id': '4238217', 'ck_superior_order_code': 'None'}
            paras["ck_superior_order_code"]=input["ck_superior_order_code"]
        if "Y"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        requestMethod="post"
        requestURL=self.url("http://ckresult.mia.com","/order/result")
        requestParas=paras
        cycleParas={'paraWant': 'result', 'stopNum': '15', 'judegValue': '2'}
        try:
            paraWant=cycleParas["paraWant"]
        except Exception as e:
            paraWant="result"
        try:
            judegValue=cycleParas["judegValue"]
        except Exception as e:
            judegValue="2"
        try:
            stopNum=cycleParas["stopNum"]
        except Exception as e:
            stopNum="15"
        cycleResult=authenticatedPara.cycleRequest(requestMethod,requestURL,requestParas,paraWant,judgeValue,stopNum)
        
        caseJudgeValue={'assertExpect': 'True', 'assertGrade': '9', 'assertThirdLevelName': 'None', 'assertResult': 'result'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        end=datetime.datetime.now()
        print ("case time:"+str((end-start).microseconds/1000000.0))

    def test_sample_2(self,input=None):
        u"""示例用例2"""
        start=datetime.datetime.now()
        resultProcess=resultApi.resultDefine()
        authenticatedPara=authenticationFunction.authentication()
        if "Y"=="Y":
            authenticatedPara.cleanCart()
        else:
            pass
        
        if input==None:
            paras={'quantity': '1', 'item_id': '1143977', 'item_size': '42g*3罐'}
        else:
            paras={'quantity': '1', 'item_id': '1143977', 'item_size': '42g*3罐'}
            paras["N"]=input["N"]
        if "Y"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://api.miyabaobei.com","/topcart/add"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "N"!="N":
            input={"N":result["content"]["N"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'params': '{"ck_type": "1","user_id": "4238217","channel": "4","sub_channel": "4.1.0|","ip": "127.0.0.1","from": "4","client_version": "4_1_0"}', 'version': '3_0'}
        else:
            paras={'params': '{"ck_type": "1","user_id": "4238217","channel": "4","sub_channel": "4.1.0|","ip": "127.0.0.1","from": "4","client_version": "4_1_0"}', 'version': '3_0'}
            paras["N"]=input["N"]
        if "N"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://ckapi.mia.com/cksrv","/order/checkout"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "N"!="N":
            input={"N":result["content"]["N"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass

        caseJudgeValue={'assertExpect': '90', 'assertGrade': '3', 'assertThirdLevelName': 'cart_total', 'assertResult': 'pay_price'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'params': '{"ck_type": "1","user_id": "4238217","address_id":"1813582","channel":"4","sub_channel":"4.1.0|","ip": "127.0.0.1","pay_mode":"3","dst_mode":"1","from":"4"}', 'version': '3_0'}
        else:
            paras={'params': '{"ck_type": "1","user_id": "4238217","address_id":"1813582","channel":"4","sub_channel":"4.1.0|","ip": "127.0.0.1","pay_mode":"3","dst_mode":"1","from":"4"}', 'version': '3_0'}
            paras["ck_superior_order_code"]=input["ck_superior_order_code"]
        if "N"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        result = requests.post(self.url("http://ckapi.mia.com/cksrv","/order/create"),paras)
        result = resultProcess.jsonTextApi(result)
        #print(result)
        if "ck_superior_order_code"!="N":
            input={"ck_superior_order_code":result["content"]["ck_superior_order_code"]}
        else:
            input=None
        logging.info("当前接口访问的结果是："+str(result))
        
        caseJudgeValue={'assertExpect': '200', 'assertGrade': '1', 'assertThirdLevelName': 'None', 'assertResult': 'code'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        if input==None:
            paras={'user_id': '4238217', 'ck_superior_order_code': 'None'}
        else:
            paras={'user_id': '4238217', 'ck_superior_order_code': 'None'}
            paras["ck_superior_order_code"]=input["ck_superior_order_code"]
        if "Y"=="Y":
            paras=authenticatedPara.CreateEntryDic(paras,open(self.authsessionParaPath).read())
        else:
            pass
        requestMethod="post"
        requestURL=self.url("http://ckresult.mia.com","/order/result")
        requestParas=paras
        cycleParas={'paraWant': 'result', 'stopNum': '15', 'judegValue': '2'}
        try:
            paraWant=cycleParas["paraWant"]
        except Exception as e:
            paraWant="result"
        try:
            judegValue=cycleParas["judegValue"]
        except Exception as e:
            judegValue="2"
        try:
            stopNum=cycleParas["stopNum"]
        except Exception as e:
            stopNum="15"
        cycleResult=authenticatedPara.cycleRequest(requestMethod,requestURL,requestParas,paraWant,judgeValue,stopNum)
        
        caseJudgeValue={'assertExpect': 'True', 'assertGrade': '9', 'assertThirdLevelName': 'None', 'assertResult': 'result'}
        #判断断言字段在结果中所处等级，进而决定进入哪个分支
        if caseJudgeValue["assertGrade"]==9 or caseJudgeValue["assertGrade"]=="9":
            if str(cycleResult)!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(cycleResult))
            self.failUnless(str(cycleResult)==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(cycleResult))
        elif caseJudgeValue["assertGrade"]==1 or caseJudgeValue["assertGrade"]=="1":
            if str(result[caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
            self.failUnless(str(result[caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result[caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==2 or caseJudgeValue["assertGrade"]=="2":
            if str(result["content"][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertResult"]]))
        elif caseJudgeValue["assertGrade"]==3 or caseJudgeValue["assertGrade"]=="3":
            if str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])!=str(caseJudgeValue["assertExpect"]):
                logging.info("结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
            self.failUnless(str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]])==str(caseJudgeValue["assertExpect"]),
                            "结果与期望不一致，当前结果是："+str(result["content"][caseJudgeValue["assertThirdLevelName"]][caseJudgeValue["assertResult"]]))
        else:
            pass


        end=datetime.datetime.now()
        print ("case time:"+str((end-start).microseconds/1000000.0))

        
    def url(self,url,path):
        return url+path
        
if __name__=="__main__":
    unittest.main()