#coding: utf-8
import smtplib,logging,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class mail:
    def __init__(self):
        pass
    #按照传入的配置发送邮件
    def send(self,emailSetDict,file_name):
        logging.debug("Current email set: "+str(emailSetDict))
        file=open(file_name,encoding="utf-8")
        mail=file.read()    
        sender=emailSetDict['Sender']
        receiver=emailSetDict['Receiver']
        subject=emailSetDict['SubjectStr']
        smtpserver=emailSetDict['SmtpServer']
        username=emailSetDict['Username']
        password=emailSetDict['Password']
        logging.info("The email set succeed.")
        msgRoot = MIMEMultipart('alternative')
        msgRoot['Subject'] = subject
        
        #构造正文并添加
        msg = MIMEText(mail,'html','utf-8')
        msgRoot.attach(msg)
        #构造附件并添加
        att=MIMEText(open(file_name,'rb').read(),'base64','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename='+file_name.split("/")[-1]
        msgRoot.attach(att)             
        
        smtp = smtplib.SMTP()
        smtp.connect(emailSetDict['Connect'])
        logging.debug("服务器连接成功！")
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        logging.info("邮件发送成功！")
        smtp.quit()
        
if __name__=="__main__":
    emailSetDict={'Receiver': 'liulinze@mia.com', 'Username': 'rinzer', 'SubjectStr': '订单系统接口特卖逻辑自动化测试结果', 'Connect': 'smtp.yeah.net', 'Sender': 'rinzer@yeah.net', 'Password': 'liulinze1987.', 'SmtpServer': 'smtp.yeah.net'}
    file_name="C:/Users/Test/Desktop/auto4.0/data/Report/Report_2016-06-07_11-33-50.html"
    mailsend=mail()
    mailsend.send(emailSetDict, file_name)