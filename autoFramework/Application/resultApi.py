#coding=utf-8
import os,sys,logging
from Core import resultFunction

class resultDefine:
    def __init__(self):
        pass
    
    def jsonTextApi(self,result):
        textReturned=resultFunction.result()
        resultText=textReturned.resultTextJsonCreate(result)
        return resultText
        
    def noJsonTextApi(self,result):
        textReturned=resultFunction.result()
        resultText=textReturned.resultTextNoJsonCreate(result)
        return resultText
        
    def onlyJsonTextApi(self,result):
        textReturned=resultFunction.result()
        resultText=textReturned.resultTextOnlyJsonCreate(result)
        return resultText
        
if __name__=='__main__':
    a=resultDefine()
    aaa=a.jsonTextApi()
    bbb=a.noJsonTextApi()
    ccc=a.onlyJsonTextApi()

