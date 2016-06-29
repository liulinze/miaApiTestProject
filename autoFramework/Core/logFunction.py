#coding=utf-8
import logging,os,datetime
from config import config

class log:
    #定义报告存放路径，当前文件调试使用以下路径
    def __init__(self):
        self.logPath = config.autoFrameworkPathSetDic["logPath"]
    
    def logLevelSet(self):
        #CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
        LevelDic={
            "Critical":logging.CRITICAL,
            "Error":logging.ERROR,
            "Warning":logging.WARNING,
            "Info":logging.INFO,
            "Debug":logging.DEBUG,
            "Noset":logging.NOTSET
            }
        return LevelDic
        
    def create(self,level):
        logTime=str((datetime.datetime.now()).strftime('%Y-%m-%d_%H-%M-%S'))        
        logFileName=(self.logPath+"/Log_"+logTime+".log").replace("\\","/")    
        #打印指定和以上级别的日志
        logLevel=self.logLevelSet()
        logging.basicConfig(
            level=logLevel[level],
            #指定日志格式
            format='%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s:%(message)s',
            datefmt='%b %d %Y %H:%M:%S',
            filename=logFileName,
            filemode='a'
            )
        
if __name__=="__main__":
    Log=log()
    Log.create("Info")