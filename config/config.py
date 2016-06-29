#coding=utf-8
import os
from rootPathConfig import rootPath

'''
设置生成日志级别
级别设置：Critical > Error > Warning > Info > Debug > Noset
'''
LogLevel='Debug'

'''
邮件发送设置字典
设置项依次为：发件人，收件人，Stmp服务器域名，登录用户名，登录密码，连接地址，邮件主题
'''
EmailSetDict={  
    'Sender':'rinzer@yeah.net',
    'Receiver':'liulinze@mia.com',
    'SmtpServer':'smtp.yeah.net',
    'Username':'rinzer',
    'Password':'liulinze1987.',
    'Connect':'smtp.yeah.net',
    'SubjectStr':'订单系统接口特卖逻辑自动化测试报告'
}

'''
测试主控字典
ReportTitle字段控制的是控制报告标题和邮件主题，引号内的内容可以随意更改
EmailKey字段控制的是否发送邮件，Y为发送，其他任意字符为不发送
TestcaseCreateKey字段控制的是是否需要创建测试用例，Y为创建，其他任意字符为不创建
'''
InterfaceTest={
    "ReportTitle":"订单系统接口特卖逻辑自动化测试报告",
    "EmailKey":"Y",
    "TestcaseCreateKey":"N"
}

'''
蜜芽APP接口测试配置
'''
BaseURL=["http://api.miyabaobei.com","http://ckapi.mia.com/cksrv","http://ckresult.mia.com"]
LoginUsername='15210026016'
LoginPassword='123456'

#蜜芽Android客户端使用
InterfacePubPara={
    'app_id':'android_test_id',
    'version':'android_4_2_0',
    'session':'357071054506316',
    'secret':'MIYABABY_ANDROID',
}

'''
#蜜芽IOS客户端使用
InterfacePubPara={
    'app_id':'ios_test_id',
    'version':'ios_4_2_0',
    'session':'357071054506316',
    'secret':'MIYABABY_IOS',
}

'''

"""
从console文件发起框架时的环境路径配置项
"""
autoFrameworkPathSetDic={
    "authsessionParaPath":rootPath+"/data/authSession/authSessionPara",
    "reportPath":rootPath+"/data/report",
    "paraPath":rootPath+"/data/jsonParameters/",
    "testcasePath":rootPath+"/data/testcase",
    "logPath":rootPath+"/data/log",
    "templatePath":rootPath+"/data/testcaseTemplate",
    "excelParasPath":rootPath+"/config"
}