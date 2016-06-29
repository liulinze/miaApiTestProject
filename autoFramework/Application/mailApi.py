#coding: utf-8
import os,sys,logging
from Core import mailFunction
from config import config

class mailDefine:
    def __init__(self):
        self.reportPath = config.autoFrameworkPathSetDic["reportPath"] 
    
    #遍历目录获取最新文件的文件名，此函数应拆分到应用层
    def reportReadingApi(self):
        report_dir=self.reportPath
        lists=os.listdir(report_dir)
        lists.sort(key=lambda fn: os.path.getmtime(report_dir+"/"+fn) if not os.path.isdir(report_dir+"/"+fn) else 0)
        file_name= os.path.join(report_dir,lists[-1])
        logging.debug("The Name of last file: "+file_name)
        return file_name.replace("\\","/")
    
    def sendMailApi(self):
        reportFileName=self.reportReadingApi()
        emailSetDict=config.EmailSetDict
        sendMail=mailFunction.mail()
        sendMail.send(emailSetDict,reportFileName)
        
if __name__=='__main__':
    a=mailDefine()
    aaa=a.sendMailApi()
    