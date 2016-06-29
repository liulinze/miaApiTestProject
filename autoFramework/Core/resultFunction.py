#coding=utf-8
import json

class result():
    def __init__(self):
        pass
    
    #用于打印最终post结果时
    def resultTextJsonCreate(self,result):
        dicResult=result.text
        print(dicResult)
        dicResJson=json.loads(dicResult,encoding='utf-8')
        resultsText=json.dumps(dicResJson,ensure_ascii=False)
        return dicResJson

    #用于验证错误结果，仅需要把Post结果转成文本时
    def resultTextNoJsonCreate(self,result):
        resultsText=result.text
        return resultsText

    #用于写断言仅需要把Post结果转成Json时
    def resultTextOnlyJsonCreate(self,result):
        dicResult=result.text
        dicResJson=json.loads(dicResult,encoding='utf-8')
        return dicResJson