#coding=utf-8
import os,sys,logging,testcaseTemplateFunction
from config import config


class testcase:
    def __init__(self):
        self.testcasePath=config.autoFrameworkPathSetDic["testcasePath"]
        
    def create(self,classFileList):
        classFileTuple=tuple(classFileList)
        for classFile in classFileTuple:
            f=open(self.testcasePath+"/"+classFile[0]+".py",'w',encoding='utf-8')
            testcaseTemplateCreate=testcaseTemplateFunction.testcaseTemplate()
            f.write(testcaseTemplateCreate.modelClassCreate(classFile))
            f.close()
            
    def initFileSet(self):
        TestcaseFiles=[]
        key=0
        for root,dirs,files in os.walk(self.testcasePath):
            if key>=1:
                break
            else:
                for fileName in files:
                    if fileName[-2:]=='py' and fileName[:-3]!='__init__':
                        TestcaseFiles.append(fileName[:-3])
                    else:
                        pass      
            key=key+1
        initfile='__all__='+str(TestcaseFiles)
        file_object=open(self.testcasePath+'/__init__.py','w')
        file_object.write(initfile)
        file_object.close()
            
if __name__=="__main__":
    aa=testcase()
    aa.initFileSet()