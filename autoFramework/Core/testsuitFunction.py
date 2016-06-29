 #coding=utf-8
import os,unittest

#组织测试套件
class testsuit:
    def __init__(self):
        pass

    #创建测试用例套件
    def create(self,ClassList):
        TestSuite=unittest.TestSuite()
        if len(ClassList)<1:
            print (u"配置文件的待测用例列表为空！")
        else:
            for Testcase in ClassList:
                try:
                    TestSuite.addTest(unittest.makeSuite(Testcase))
                except:
                    print(u"Testcase文件自定义的类名称与该文件名不一致！")
        return TestSuite
