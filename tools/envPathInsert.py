#coding=utf-8
import os,shutil

class pthfileCreate:
    #获取当前框架的所有包路径
    def catchAllPath(self):
        rootList=[]
        for root,dirs,files in os.walk(os.path.dirname(os.getcwd())):
            if root.endswith("__pycache__")==True:
                pass
            else:
                rootList.append(root.replace("\\","/"))
        return rootList
    
    def writeRootPath(self):
        rootPath=os.path.dirname(os.getcwd()).replace("\\","/")
        rootPthfile=open(rootPath+"/config/rootPathConfig.py","w")
        rootPthfile.write(u'#coding=utf-8\n\nrootPath="'+rootPath+'"')
        rootPthfile.close()

    #将包路径写到指定路径的autoFrameworkPath.pth文件下,并复制到当前python环境的site-packages路径下，完成路径添加
    def writePthFile(self):
        self.writeRootPath()
        fromPath=os.path.dirname(os.getcwd()).replace("\\","/")+"/data/envSet/autoFrameworkEnvPath.pth"
        targetPath=((os.path.dirname(os.__file__)).replace("\\","/")+"/site-packages")
        pthfile=open(fromPath,"w")
        pathList=self.catchAllPath()
        for path in pathList:
            pthfile.write(path+"\n")
        pthfile.close()
        shutil.copy(fromPath,targetPath)
        print("环境配置完毕！")

    
if __name__=="__main__":
    pathObject=pthfileCreate()
    pathList=pathObject.writePthFile()
    

    