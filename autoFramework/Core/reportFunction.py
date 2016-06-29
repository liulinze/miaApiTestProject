#coding=utf-8
import HTMLTestRunner,os,datetime,logging
from config import config

class report:
    #定义报告存放路径，当前文件调试使用以下路径
    def __init__(self):
        self.reportPath = config.autoFrameworkPathSetDic["reportPath"]
    
    #创建日志文件，并获取待测试列表传入报告模块，返回报告中待显示列表    
    def Create(self,ReportTitle):
        ReportTime=datetime.datetime.now()
        ReportTime=str(ReportTime.strftime('%Y-%m-%d_%H-%M-%S'))
        filename=self.reportPath+'/Report_'+ReportTime+'.html'
        fp = open(filename, 'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=ReportTitle,description=u'测试用例执行情况（具体执行情况请下载附件使用浏览器打开查看）：')
        runnerList=(runner,fp,self.reportPath)
        return runnerList

