#coding=utf-8
import os,sys
from Core import logFunction
from config import config

class logDefine:
    def __init__(self):
        pass
        
    def logApi(self):
        logCreate=logFunction.log()
        logCreate.create(config.LogLevel)
        
if __name__=='__main__':
    a=logDefine()
    aaa=a.logApi()