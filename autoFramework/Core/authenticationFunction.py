#coding=utf-8
import time,json,hashlib,os,rsa
import sys,re,base64,requests
from config import config

class rsaEncryption:
    def __init__(self):
        pass    
    #方法名称：RSA公钥加密函数
    def PublicRSA(self,PartJsonParameter):
        publicKey =b"""-----BEGIN PUBLIC KEY-----
        MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCiwJbb2EeK9ZB4Chyj5/mIVPRE
        od0pJrv3LM2UVtkod+2mPVjV9Xi1E06gUaoexX/ebfRXm1eBwu3LtYbklh5Ji5oF
        ycoUCFhwzhmm8ZtjdkCIicFfxUU4I5NunL6+37+hy43EgCrao5tFgHtnkeR/vNyG
        faxdxevPbVEtWlJz6wIDAQAB
        -----END PUBLIC KEY-----"""
        key=rsa.PublicKey.load_pkcs1_openssl_pem(publicKey)
        MiddleCipher=rsa.encrypt(str.encode(PartJsonParameter),key)
        SecretText=base64.encodestring(MiddleCipher)
        #return (bytes.decode(SecretText)).replace("\n","")
        return SecretText
    
    #方法名称：调用RSA加密做分段加密函数
    def SliceEncryption(self,JsonPara):
        #切割入参字符串
        PartSecretTextList=re.split(r'(.{117})',JsonPara)
        SecretParameter=''
        for PartSecretText in PartSecretTextList:
            #去除为空的非法元素
            if PartSecretText=='':
                PartSecretTextList.remove(PartSecretText)
            #对非空的列表元素进行加密拼接
            else:
                key=bytes.decode(self.PublicRSA(PartSecretText))
                #SecretParameter=(SecretParameter+key)[:-1]
                SecretParameter=SecretParameter+key
        #返回密文
        return SecretParameter    
    
class authentication:
    def __init__(self):
        self.authsessionParaPath=config.autoFrameworkPathSetDic["authsessionParaPath"]
        
    #方法名称：MD5加密函数
    def md5(self,SignStr):
        SignStrResult=isinstance(SignStr,str)
        if SignStrResult==True:
            m=hashlib.md5()
            m.update(SignStr.encode('utf-8'))
            return m.hexdigest()
        else:
            return False

    #方法名称：字典键值对排序并转字符串函数
    def SortDicAndTurnToStr(self,DicSignPara):
        ListBeforeMD5=sorted(DicSignPara.items(),key=lambda asd:asd[0],reverse=False)
        StrSignPara=''
        for i in range(len(ListBeforeMD5)):
            for j in range(2):
                StrSignPara=StrSignPara+str(ListBeforeMD5[i][j])
        return StrSignPara


    #方法名称：业务参数转Json字符串函数
    def ParamsJsonCreate(self,Parameter,ParaType):
        if ParaType=='Y':
            JsonParameter=json.dumps(Parameter).replace(' ','')
        else:
            JsonParameter=json.dumps(Parameter)
        return JsonParameter

    #方法名称：Post请求的参数字典创建函数
    def CreateEntryDic(self,BusinessParameters,AuthSession,result=0):
        #最终业务参数处理
        if len(BusinessParameters)>0:
            #定义原始业务参数，业务参数序列化成json字符串
            ParaType='Y'
            JsonBusinessParameter=self.ParamsJsonCreate(BusinessParameters,ParaType)
            #做RSA加密传给para
            if result==0:
                rsaPara=rsaEncryption()
                para=rsaPara.SliceEncryption(JsonBusinessParameter).replace('\n', '')
            else:
                para=JsonBusinessParameter
        else:
            ParaType='N'
            para=self.ParamsJsonCreate(BusinessParameters,ParaType)
        #定义创建sign参数的入参字典
        CreateSignPara={
            "timestamp":int(time.time()),
            "app_id":config.InterfacePubPara['app_id'],
            "version":config.InterfacePubPara['version'],
            "session":config.InterfacePubPara['session'],
            "auth_session":AuthSession,
            "params":para
        }
        #序列化成json字符串
        JsonSignPara=self.SortDicAndTurnToStr(CreateSignPara)
        #获取Secret参数
        secret=config.InterfacePubPara['secret']
        #将入参字典的Json字符串和secret拼接后做MD5加密获取sign参数
        if result==0:
            sign=self.md5(JsonSignPara+secret)
        else:
            sign=self.md5("2ea342511cb908728db3998d71f4161f"+JsonSignPara+secret)
        #定义接口入参字典
        DicInterfaceTestPara=CreateSignPara
        DicInterfaceTestPara['sign']=sign
        return DicInterfaceTestPara


    #调用登录接口将用户登录上去并获取AuthSession，记录到指定文件中，留备使用
    def authSessionCreate(self):
        loginApiPara={}
        loginApiPara['name']=base64.encodestring(('miababy'+config.LoginUsername).encode()).decode()[:-1]
        loginApiPara['password']=base64.encodestring(('miababy'+config.LoginPassword).encode()).decode()[:-1]
        AuthSession="5ca6242f7db1b275783d95a4892727e8"
        interfacePara=self.CreateEntryDic(loginApiPara,AuthSession)
        #url=config.BaseURL[0]+'/account/PressureTestLogin/'
        url=config.BaseURL[0]+'/account/Login/'
        result=(requests.post(url,interfacePara)).text
        result=json.loads(result,encoding='utf-8')
        AuthSession=result['content']['auth_session']
        AuthSessionPara=open(self.authsessionParaPath,'w')
        AuthSessionPara.write(AuthSession)
        AuthSessionPara.close()
    
    #调用指定接口并获取指定参数，返回给主调功能    
    def cycleRequest(self,requestMethod,requestURL,requestParas,paraWant,judgeValue,stopNum):
        for i in range(int(stopNum)):
            cmd="requests."+requestMethod+"("+'"'+requestURL+'"'+","+"requestParas"+")"
            requestResult=eval(cmd)
            requestResult=json.loads(requestResult.text,encoding='utf-8')
            catch=requestResult['content'][paraWant]
            time.sleep(1)
            print(catch)
            if catch==judgeValue or catch==int(judgeValue):
                return "True"
            elif i==int(stopNum)-1:
                return "False"
            else:
                pass
            
    def cleanCart(self):
        url=config.BaseURL[0]+'/cart/info/'
        AuthSession=open(self.authsessionParaPath).read()
        interfacePara=self.CreateEntryDic({},AuthSession)
        result=requests.post(url,interfacePara)
        result=json.loads(result.text,encoding='utf-8')
        
        catch=result["content"]["row_infos"]
        rowidList=[]
        for itemGroup in catch:
            for items in (itemGroup["item_group"]):
                for item in items["items"]:
                    rowid=item["id"]
                    rowidList.append(rowid)
        for rowid in rowidList:
            para={"row_id":rowid}
            interfacePara2=self.CreateEntryDic(para,AuthSession)
            url2=config.BaseURL[0]+'/cart/delete/'
            result=requests.post(url2,interfacePara2)
            result=json.loads(result.text,encoding='utf-8')
        #return rowidList
    
if __name__=="__main__":
    aa=authentication()
    
    paras=aa.authSessionCreate()

    print(paras)
    