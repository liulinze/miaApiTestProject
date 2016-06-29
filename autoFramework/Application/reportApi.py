#coding=utf-8
import sys,os,logging
from Core import reportFunction
from config import config

class reportDefine:
    def __init__(self):
        pass
    
    def reportApi(self):
        reportObjCreate=reportFunction.report()
        reportTitle=config.InterfaceTest["ReportTitle"]
        reportTouple=reportObjCreate.Create(reportTitle)
        return reportTouple
        
if __name__=='__main__':
    a=reportDefine()
    aaa=a.reportApi()

        

