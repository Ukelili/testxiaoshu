# coding: gb2312
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time,os


class SysXSAdmin(object):
    ''' ???ㄦ?瑙??? '''
    def __init__(self,browser='ff'):
        if browser == "firefox" or browser=="ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser=="ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." %browser)
        print('???ㄦ?瑙???')
    # url?板??
    def UrlOpen(self,url):
        self.driver.maximize_window()
        self.driver.get(url) # Load page
    # ?抽??娴?瑙???
    def Quitbrow(self):
        self.driver.quit()  # Quit Browser
    # ?诲?绯荤?????
    def SysLogin(self,user,pwd,verify):
        self.driver.find_element_by_class_name("adm_name").send_keys(user)  # Input User name
        self.driver.find_element_by_class_name("adm_password").send_keys(pwd)  # Input password
        self.driver.find_element_by_name("adm_verify").send_keys(verify)  # Input verify
        self.driver.find_element_by_id("login_btn").click()
        print('绯荤????扮?诲?')
    # ?ㄤ???浣?menu????
    def MenuTpye(self,listnum):
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[1]/a").click()  # ?瑰?荤郴缁?棣?椤?
            print('???扮郴缁?棣?椤?')
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/a").click()  # ?瑰?昏捶娆剧?＄??
            print('璐锋?剧?＄??')
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[3]/a").click()  # ?瑰?讳???绠＄??
            print('浼???绠＄??')
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]/a").click()  # ?瑰?昏???绠＄??
            print('璧???绠＄??')
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[5]/a").click()  # ?瑰?诲???浜???
            print('寰???浜???')
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[6]/a").click()  # ?瑰?荤?璁℃ā??
            print('缁?璁℃ā??')
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[7]/a").click()  # ?瑰?婚?ㄩ?ㄧ?＄??
            print('?ㄩ?ㄧ?＄??')
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[8]/a").click()  # ?瑰?诲??甯???浼?浜?
            print('??甯???浼?浜?')
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[9]/a").click()  # ?瑰?荤Н??????
            print('绉???????')
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[10]/a").click()  # ?瑰?诲??绔?璁剧疆
            print('??绔?璁剧疆')
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[11]/a").click()  # ?瑰?绘椿?ㄤ??ㄥ箍
            print('娲诲?ㄤ??ㄥ箍')
        elif listnum == "12":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[12]/a").click()  # ?瑰?荤郴缁?璁剧疆
            print('绯荤?璁剧疆')
    # ?ㄤ???浣?璐锋?剧?＄??????涓???瀛?????
    def LoanMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?昏捶娆剧?＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?诲?ㄩ?ㄨ捶娆?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?婚???涓?璐锋??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?绘?版??璐锋??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?昏捶娆惧???剁??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?瑰?诲?℃?告?ュ???琛?
    # ?ㄤ???浣?瀹℃?哥?＄??涓??㈢??瀛?????
    def DealMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?诲?℃?哥?＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?婚???寰?瀹℃?稿??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?荤画??寰?瀹℃?稿??琛?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?瑰?绘????寰?瀹℃?稿??琛?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?瑰?诲?瀹℃?稿??琛?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?瑰?绘??婊℃??璐锋??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?瑰?昏?????璐锋??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?瑰?绘?????璐锋??
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?瑰?诲?℃?稿け璐ョ??璐锋??
    # ?ㄤ???浣?婊℃??绠＄??涓??㈢??瀛?????
    def FundDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?绘弧??绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?瑰?绘弧??寰??炬??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?瑰?昏?娆句腑璐锋??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?瑰?诲凡瀹???璐锋??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?瑰?绘????杩?璐锋??
    # ?ㄤ???浣?淇?璇???绠＄??????涓??㈢??瀛?????
    def Bmoney(self,listmun):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?讳?璇???绠＄??
        if listmun == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click() # ?瑰?诲?杩?杩?
        elif listmun == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?瑰?诲凡杩?杩?
        elif listmun == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?瑰?绘???炬??
    # ?ㄤ???浣????剁?＄??????涓??㈢??瀛?????
    def CollMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?瑰?诲???剁?＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?瑰?诲????跺??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?瑰?诲????舵????缁?
    # ?ㄤ???浣???璐疯?板?????涓??㈢??瀛?????
    def DealLog(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?瑰?诲??璐疯?板?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?瑰?诲?杩?娆捐处??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?瑰?婚?炬??寰??舵??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # ?瑰?荤?绔???浠?娆?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[4]/a").click()  # ?瑰?绘?舵?句俊??
    # ?ㄤ???浣?????淇℃??????涓??㈢??瀛?????
    def DealInfo(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ?瑰?绘????淇℃??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?瑰?绘????????
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?瑰?绘???ㄦ????
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ?瑰?昏???ㄦ????
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # ?瑰?绘??????????
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?瑰?诲け璐ョ??????
    # ?ㄤ???浣??烘??杞?璁╄????涓??㈢??瀛?????
    def Transfer(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?瑰?诲?烘??杞?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?瑰?绘????杞?璁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?瑰?绘?ｅ?ㄨ浆璁?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ?瑰?绘????杞?璁?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # ?瑰?绘?ら??杞?璁?
    # ?ㄤ???浣???瑷?寮?璐锋?剧?宠?疯????涓??㈢??瀛?????
    def MsgDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?瑰?荤??瑷?寮?璐锋?剧?宠??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # ?瑰?荤??瑷?寮?璐锋?剧?宠??
        try:
           if listnum <= "0":
               print("error")
        except Exception:
            raise NameError("Not found %s listnum,You can enter '1'....." %listnum)
    # ?ㄤ???浣???瑷?绠＄??????涓??㈢??瀛?????
    def MsgMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ?瑰?荤??瑷?绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd/a").click()  # ?瑰?荤??瑷???琛?
    # ?ㄤ???浣?涓??″???ヨ?㈣????涓??㈢??瀛?????
    def BusMan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[11]/dt").click()  # ?瑰?讳??″???ヨ??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[1]/a").click()  # ?瑰?绘?ㄨ??浜烘?ヨ??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[2]/a").click()  # ?瑰?诲?瀹℃?告?ヨ??
    # ?ㄤ???浣?????浼???????涓??㈢??瀛?????
    def User(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?绘????浼???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?绘?????ㄦ??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?诲??娆剧?ㄦ??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?荤??璐㈢?ㄦ??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?昏????????
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?瑰?诲???榛?????
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?瑰?荤?璐烽?????
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?瑰?诲?瀹℃?镐???
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?瑰?讳???淇℃??
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # ?瑰?讳??????剁??
    # ?ㄤ???浣?浼?涓?浼???????涓??㈢??瀛?????
    def UesrCompany(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click() # ?瑰?讳?涓?浼???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?讳?涓?浼???
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?讳???榛?????
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?瑰?诲?瀹℃?镐???
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?瑰?讳???淇℃??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?瑰?讳??????剁??
    # ?ㄤ???浣???淇??烘??????涓??㈢??瀛?????
    def DealAgency(self,liestnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?绘??淇??烘??
        if liestnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?瑰?绘??淇??烘??
        elif liestnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?瑰?绘??淇??烘?????剁??
    # ?ㄤ???浣??朵?淇℃??????涓??㈢??瀛?????
    def CompanyManage(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?诲?朵?淇℃??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?瑰?诲???稿??琛?
        elif listnum =="2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?瑰?诲伐浣?淇℃??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?瑰?婚?惰??″??琛?
    # ?ㄤ???浣?绾㈠??绠＄??????涓??㈢??瀛?????
    def EcvMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?瑰?? 绾㈠??绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd/a")  # ?瑰?荤孩??绫诲??
    # ?ㄤ???浣??稿?抽??缃?????涓??㈢??瀛?????
    def AboutConfig(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?瑰?荤?稿?抽??缃?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?瑰?讳???瀛?娈靛??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?瑰?讳俊?ㄧ??绾у??琛?
    # ?ㄤ???浣?绔???娑???????涓??㈢??瀛?????
    def MsgSystem(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ?瑰?荤????娑???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?瑰?绘???缇ゅ??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?瑰?绘?????琛?
    # ?ㄤ???浣?VIP?规??????涓??㈢??瀛?????
    def VipPrivilege(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?瑰??VIP?规??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?瑰??VIP浼?????琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?瑰??VIP绛?绾?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ?瑰??VIP??缃???琛?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # ?瑰??VIP??缃????剁??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[5]/a").click()  # ?瑰??VIP??绾ц?板?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[6]/a").click() # ?瑰??VIP??绾ц?板?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[7]/a").click()  # ?瑰??VIP璐?涔版?ュ?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[8]/a").click()  # ?瑰?诲?㈡????琛?
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[9]/a").click()  # ?瑰?诲?㈡?????剁??
    # ?ㄤ???浣???璧?濂??辫????涓??㈢??瀛?????
    def VipGift(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?瑰?绘??璧?濂???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[1]/a").click()  # ?瑰?诲??卞???惧??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[2]/a").click()  # ?瑰?荤ぜ??绠＄??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[3]/a").click()  # ?瑰?婚?????伴??绠＄??
    # ?ㄤ???浣????ョ??╄????涓??㈢??瀛?????
    def VipFestivals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ?瑰?昏???ョ???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[1]/a").click()  # ?瑰?昏???ョН??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[2]/a").click()  # ?瑰?荤??╁???惧??琛?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[3]/a").click()  # ?瑰?荤Н???辩??
    # ?ㄤ???浣?缁?绾??宠?疯????涓??㈢??瀛?????
    def GenerationRepay(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?荤画绾??宠??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd/a").click()  # ?瑰?荤画绾??宠?峰??????
    # ?ㄤ???浣???淇￠?搴??宠?疯????涓??㈢??瀛?????
    def DealQuota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?绘??淇￠?搴??宠??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click()  # ?瑰?荤?宠?峰??琛ㄥ??????
    # ?ㄤ???浣?淇＄?ㄩ?搴??宠?疯????涓??㈢??瀛?????
    def Quota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?讳俊?ㄩ?搴??宠??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # ?瑰?荤?宠?峰??琛?
    # ?ㄤ???浣?涓炬?ョ?＄??????涓??㈢??瀛?????
    def Reportguy(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?讳妇?ョ?＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # ?瑰?讳妇?ュ??琛?
    # ?ㄤ???浣?璁よ??绠＄??????涓??㈢??瀛?????
    def CreditMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?瑰?昏?よ??绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?瑰?绘????璁よ??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?瑰?诲?瀹℃?哥??璁よ??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[3]/a").click()  # ?瑰?婚??杩???璁よ??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[4]/a").click()  # ?瑰?诲け璐ョ??璁よ??
    # ?ㄤ???浣?浼???杩??╄????涓??㈢??瀛?????
    def Referrals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?瑰?讳???杩???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?瑰?婚??璇疯??╁??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?瑰?诲缓绔??宠??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # ?瑰?绘?ㄥ箍浜哄??琛?
    # ?ㄤ???浣????虹?璁¤????涓??㈢??瀛?????
    def StatisticsBorrow(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?诲???虹?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?诲???烘?荤?璁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?绘??璧?浜烘??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?绘??璧???棰?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?绘??绉???璧?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?瑰?诲凡??娆?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?瑰?诲??舵??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?瑰?绘??璧?????
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?瑰?绘??璧?棰?姣?渚?
    # ?ㄤ???浣????ョ?璁¤????涓??㈢??瀛?????
    def StatisticsLoan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?诲???ョ?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?诲???ユ?荤?璁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?诲??娆句汉??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?瑰?诲??娆鹃??棰?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?瑰?绘??绉???娆?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?瑰?诲凡杩?娆?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?瑰?诲?杩?娆?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?瑰?婚?炬??杩?娆?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?瑰?婚?炬????缁?
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[9]/a").click()  # ?瑰?婚?炬????琛?
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[10]/a").click()  # ?瑰?婚?炬???版??????
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[11]/a").click()  # ?瑰?婚?炬???ョ?璁℃??杈?
    # ?ㄤ???浣??烘??缁?璁¤????涓??㈢??瀛?????
    def StatisticsClaims(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?诲?烘??缁?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd").click()  # ?瑰?诲?烘??杞?璁?
    # ?ㄤ???浣?骞冲?扮?璁¤????涓??㈢??瀛?????
    def WebsiteStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?瑰?诲钩?扮?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?瑰?诲???肩?璁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?瑰?绘???扮?璁?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?瑰?荤?ㄦ?风?璁?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  #?瑰?诲勾榫?娈电?璁?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[5]/a").click()  # ?瑰?荤?绔???浠?缁?璁?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[6]/a").click()  # ?瑰?荤?绔?璐圭?ㄧ?璁?
    # ?ㄤ???浣??″??琛??胯????涓??㈢??瀛??ㄦ贰
    def Agentsstatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]").click()  # ?瑰?绘?″??琛??跨?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click() # ?瑰?绘?″???″??琛??垮??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?瑰?绘?″??琛??跨?璁?
    # ?ㄤ???浣?绠＄????绠＄??????涓??㈢??瀛?????
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?荤?＄????绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?婚?ㄩ?ㄥ??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?婚?ㄩ?ㄥ??绔?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?婚?ㄩ?ㄦ????
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?诲?????浼???
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?瑰?诲???????娆炬??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?瑰?绘??????娆炬??
    # ?ㄤ???浣?????缁?璁¤????涓??㈢??瀛?????
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?绘????缁?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?婚?ㄩ?ㄦ????缁?璁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?绘????????缁?璁?
    # ?ㄤ???浣?????浼???????涓??㈢??瀛?????
    def MyMembership(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?绘????浼???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?瑰?绘????浼?????琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?瑰?绘?????版??璐???
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?瑰?婚?炬??璐???
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?瑰?昏?娆句腑??娆炬??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[5]/a").click()  # ?瑰?诲凡瀹?????娆炬??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[6]/a").click()  # ?瑰?诲凡??璐???娆炬??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[7]/a").click()  # ?瑰?诲??娆句?????琛?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[8]/a").click()  # ?瑰?诲??璐?浼?????琛?
    # ?ㄤ???浣???甯???浼?浜鸿????涓??㈢??瀛?????
    def RegionPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?诲??甯???浼?浜?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?诲??甯???浼?浜哄??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?诲?缂翠?璇?????琛?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?诲凡缂翠?璇???璁板?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?讳??″????琛?
    # ?ㄤ???浣?璐锋?剧?璁¤????涓??㈢??瀛?????
    def LoanPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?昏捶娆剧?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click() # ?瑰?昏捶娆剧?璁″??琛?
    # ?ㄤ???浣??剁??缁?璁¤????涓??㈢??瀛?????
    def IncomeStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?绘?剁??缁?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # ?瑰?绘?剁??缁?璁″??琛?
    # ?ㄤ???浣??炬??缁?璁¤????涓??㈢??瀛?????
    def ExpiredStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?婚?炬??缁?璁?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # ?瑰?婚?炬??缁?璁″??琛?
    # ?ㄤ???浣?绉???????????涓??㈢??瀛?????
    def Goods(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # ?瑰?荤Н??????
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd[1]/a").click()  # ?瑰?诲??????琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl/dd[2]/a").click()  # ?瑰?诲??????绫?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl/dd[3]/a").click()  # ?瑰?诲???㈠????
    # ?ㄤ???浣???绔?绠＄??????涓??㈢??瀛?????
    def ArticleMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?绘??绔?绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?绘??绔???琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?绘??绔????剁??
    # ?ㄤ???浣???绔???绫昏????涓??㈢??瀛?????
    def ArticleCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?绘??绔???绫?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?诲??绫诲??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?诲??绫诲???剁??
    # ?ㄤ???浣???绔?璁剧疆????涓??㈢??瀛?????
    def NavSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?诲??绔?璁剧疆
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?瑰?诲?艰????????琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?瑰?绘??绁ㄨ??ュ??琛?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?瑰?诲??绔?骞垮????琛?
    # ?ㄤ???浣??????炬?ヨ????涓??㈢??瀛?????
    def LinkGroup(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?诲?????炬??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?瑰?诲?????炬?ュ??缁?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?瑰?诲?????炬?ュ??琛?
    # ?ㄤ???浣??ㄥ勾娲诲?ㄨ????涓??㈢??瀛?????
    def Special(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # ?瑰?诲?ㄥ勾娲诲??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd").click()  # ?瑰?诲コ绁?璇???
    # ?ㄤ?绯荤?璁剧疆????涓??㈢??瀛?????
    def SysConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?瑰?荤郴缁?璁剧疆
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?瑰?荤郴缁???缃?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?瑰?荤?惧?板??遍??缃?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?瑰?婚??璇疯??╅??缃?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?瑰?绘???????℃?烘??杩?浣ｈ?剧疆
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?瑰??QQ瀹㈡????缃?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?瑰?绘???版??缁?璐?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?瑰?绘???伴?惰?璁剧疆
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?瑰?昏?よ??绫诲??璁剧疆
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # ?瑰?荤?ㄦ?峰钩?版敞??楠?璇?璁剧疆
    # ?ㄤ???浣?璐锋?捐?剧疆????涓??㈢??瀛?????
    def DealCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?瑰?昏捶娆捐?剧疆
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?瑰?昏捶娆惧??绫昏?剧疆
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?瑰?诲??绫诲???剁??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?瑰?昏捶娆剧被??璁剧疆
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?瑰?荤被?????剁??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?瑰?昏捶娆惧??甯?璁剧疆
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?瑰?诲??甯????剁??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?瑰?诲????????璁剧疆
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?瑰?昏???????剁??
    # ?ㄤ???浣?浣?楠???绠＄??????涓??㈢??瀛?????
    def LearnMoney(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?瑰?讳?楠???绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?瑰?诲???惧??琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?瑰?绘??璧?璁板?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?瑰?绘椿?ㄨ?剧疆
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?瑰?荤??璐?浜у????琛?
    # ?ㄤ???浣??ュ?ｈ?剧疆????涓??㈢??瀛?????
    def AIPSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?瑰?绘?ュ?ｈ?剧疆
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?瑰?昏?????绠?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?瑰?绘??浠??ュ?ｈ?剧疆
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?瑰?讳???绗?涓??圭?诲?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  # ?瑰?讳????村????浠?
    # ?ㄤ???浣?绉诲?ㄥ钩璁剧疆????涓??㈢??瀛?????
    def MobileConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?瑰?荤Щ?ㄥ钩璁剧疆
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?瑰?绘???虹????缃?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?瑰?绘???虹??骞垮????琛?
    # ?ㄤ???浣?绯荤?绠＄??????涓??㈢??瀛?????
    def SyeRole(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?瑰?荤郴缁?绠＄????
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]").click()  # ?瑰?昏??茬?＄??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]").click()  # ?瑰?昏??插???剁??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]").click()  # ?瑰?荤?＄????绠?
    # ?ㄤ???浣???????浠剁?＄??????涓??㈢??瀛?????
    def MsgMailMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click() # ?瑰?荤??????浠剁?＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?瑰?绘???妯℃?跨?＄??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?瑰?婚??浠舵???″?ㄥ??琛?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ?瑰?婚??浠跺??琛?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # ?瑰?荤??????娆惧??琛?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[5]/a").click()  # ?瑰?荤??????琛?
    # ?ㄤ???浣?????绠＄??????涓??㈢??瀛?????
    def DealMsgList(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?瑰?婚????绠＄??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?瑰?讳??￠??????琛?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?瑰?绘?ㄥ箍??????琛?
    # ?ㄤ???浣??版??搴?????涓??㈢??瀛?????
    def Database(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?瑰?绘?版??搴?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # ?瑰??SQL??浣?
    # ?ㄤ???浣?棣???寰?瀹℃?稿??琛ㄥ?℃?稿?ㄤ?
    def FirstPublish(self,action):
        if action == "shcz" or action == "瀹℃?告??浣?" :
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[13]/a").click()  # ?瑰?诲?℃?告??浣?
        elif action == "rl" or action == "璁ら?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()  # ?瑰?昏?ら???浣?
        elif action == "shrz" or action == "瀹℃?告?ュ?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # ?瑰?诲?℃?告?ュ?
        elif action == "dkmc" or action == "璐锋?惧??绉?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()  # ?瑰?昏捶娆惧??绉?
        elif action == "jkr" or action == "??娆句汉":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ?瑰?诲??娆句汉
    # ?ㄤ???浣?澶?瀹℃?稿??琛ㄥ?℃?稿?ㄤ?
    def TruePublish(self,action):
        if action == "dkmc" or action == "璐锋?惧??绉?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()
        elif action == "jkr" or action == "??娆句汉":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()
        elif action == "shcz" or action == "瀹℃?告??浣?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()
        elif action == "shrz" or action == "瀹℃?告?ュ?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()
    # ?ㄤ???浣?缁???寰?瀹℃?稿??琛ㄥ?℃?稿?ㄤ?
    def Publish(self,action):
        if action == "shcz" or action == "瀹℃?告??浣?" :
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # ?瑰?诲?℃?告??浣?
        elif action == "rl" or action == "璁ら?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[16]/a").click()  # ?瑰?昏?ら???浣?
        elif action == "shrz" or action == "瀹℃?告?ュ?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[17]/a").click()  # ?瑰?诲?℃?告?ュ?
        elif action == "dkmc" or action == "璐锋?惧??绉?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[3]").click()  # ?瑰?昏捶娆惧??绉?
        elif action == "jkr" or action == "??娆句汉":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ?瑰?诲??娆句汉
    # ?ㄤ???浣?瀹℃?歌????椤电??瀹℃?稿?ㄤ?
    def PublishPage(self,state,city,type,status,time,action):
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]").click()  # ?瑰?婚???╀腑??浠?
        if state == "??浜?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[2]").click()
        elif state == "瀹?寰?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[3]").click()
        elif state == "绂?寤?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[4]").click()
        elif state == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[5]").click()
        elif state == "骞夸?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[6]").click()
        elif state == "骞胯タ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[7]").click()
        elif state == "璐靛?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[8]").click()
        elif state == "娴峰??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[9]").click()
        elif state == "娌冲??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[10]").click()
        elif state == "娌冲??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[11]").click()
        elif state == "榛?榫?姹?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[12]").click()
        elif state == "婀???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[13]").click()
        elif state == "婀???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[14]").click()
        elif state == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[15]").click()
        elif state == "姹???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[16]").click()
        elif state == "姹?瑗?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[17]").click()
        elif state == "杈藉??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[18]").click()
        elif state == "??????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[19]").click()
        elif state == "瀹?澶?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[20]").click()
        elif state == "??娴?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[21]").click()
        elif state == "灞变?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[22]").click()
        elif state == "灞辫タ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[23]").click()
        elif state == "??瑗?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[24]").click()
        elif state == "涓?娴?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[25]").click()
        elif state == "??宸?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[26]").click()
        elif state == "澶╂触":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[27]").click()
        elif state == "瑗胯??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[28]").click()
        elif state == "?扮??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[29]").click()
        elif state == "浜???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[30]").click()
        elif state == "娴?姹?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[31]").click()
        elif state == "??搴?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[32]").click()
        elif state == "棣?娓?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[33]").click()
        elif state == "婢抽??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[34]").click()
        elif state == "?版咕":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[35]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]").click()  # ?瑰?婚???╀腑??甯?
        if state == "??浜?" and city == "??浜?"\
                or state == "瀹?寰?" and city == "瀹?搴?" \
                or state == "绂?寤?" and city == "绂?宸?" \
                or state == "????" and city == "?板?" \
                or state == "骞夸?" and city == "骞垮?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[2]").click()
        elif state == "瀹?寰?" and city == "????" \
                or state == "绂?寤?" and city == "榫?宀?"\
                or state == "????" and city == "?介??" \
                or state == "骞夸?" and city == "娣卞??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[3]").click()
        elif state == "瀹?寰?" and city == "宸㈡?" \
                or state == "绂?寤?" and city == "??骞?"\
                or state == "????" and city == "瀹?瑗?" \
                or state == "骞夸?" and city == "娼?宸?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[4]").click()
        elif state == "瀹?寰?" and city == "姹?宸?" \
                or state == "绂?寤?" and city == "瀹?寰?"\
                or state == "????" and city == "????" \
                or state == "骞夸?" and city == "涓???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[5]").click()
        elif state == "瀹?寰?" and city == "婊?宸?" \
                or state == "绂?寤?" and city == "????"\
                or tate == "????" and city == "??宄???" \
                or state == "骞夸?" and city == "浣?灞?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[6]").click()
        elif state == "瀹?寰?" and city == "????" \
                or state == "绂?寤?" and city == "娉?宸?"\
                or state == "????" and city == "????" \
                or state == "骞夸?" and city == "娌虫?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[7]").click()
        elif state == "瀹?寰?" and city == "娣???" \
                or state == "绂?寤?" and city == "涓???"\
                or state == "????" and city == "??娉?" \
                or state == "骞夸?" and city == "??宸?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[8]").click()
        elif state == "瀹?寰?" and city == "娣???" \
                or state == "绂?寤?" and city == "????"\
                or state == "????" and city == "涓村?" \
                or state == "骞夸?" and city == "姹???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[9]").click()
        elif state == "瀹?寰?" and city == "榛?灞?" \
                or state == "绂?寤?" and city == "婕冲?"\
                or state == "????" and city == "????" \
                or state == "骞夸?" and city == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[10]").click()
        elif state == "瀹?寰?" and city == "??瀹?" \
                or state == "????" and city == "骞冲??" \
                or state == "骞夸?" and city == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[11]").click()
        elif state == "瀹?寰?" and city == "椹???灞?" \
                or state == "????" and city == "搴???" \
                or state == "骞夸?" and city == "姊?宸?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[12]").click()
        elif state == "瀹?寰?" and city == "瀹垮?" \
                or state == "????" and city == "澶╂按" \
                or state == "骞夸?" and city == "娓?杩?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[13]").click()
        elif state == "瀹?寰?" and city == "????" \
                or state == "????" and city == "姝?濞?" \
                or state == "骞夸?" and city == "姹?澶?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[14]").click()
        elif state == "瀹?寰?" and city == "??婀?" \
                or state == "????" and city == "寮???" \
                or state == "骞夸?" and city == "姹?灏?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[15]").click()
        elif state == "瀹?寰?" and city == "瀹ｅ??" \
                or state == "骞夸?" and city == "?跺??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[16]").click()
        elif state == "瀹?寰?" and city == "浜冲?" \
                or state == "骞夸?" and city == "?虫?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[17]").click()
        elif state == "瀹?寰?" and city == "????" \
                or state == "骞夸?" and city == "浜?娴?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[18]").click()
        elif state == "骞夸?" and city == "婀?姹?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[19]").click()
        elif state == "骞夸?" and city == "??搴?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[20]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select").click()  # ?瑰?婚??涓???娆剧?ㄩ??
        if type == "??涓???娆?" or type == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[2]").click()
        elif type == "寮?搴???娆?" or type == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[3]").click()
        elif type == "??娓稿??娆?" or type == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[4]").click()
        elif type == "涔扮?佃????娆?" or type == "4":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[5]").click()
        elif type == "涔版???哄??娆?" or type == "5":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[6]").click()
        elif type == "璐??╁??娆?" or type == "6":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[7]").click()
        elif type == "??椹剧?у??娆?" or type == "7":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[8]").click()
        elif type == "??娲昏垂??娆?" or type == "8":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[9]").click()
        elif type == "?朵?娑?璐瑰??娆?" or type == "9":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[10]").click()
        # ???╁?＄?舵??
        if status == "瀹℃?稿け璐?" or status == "澶辫触" or status == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[1]/input").click()
        elif status == "瀹℃?告????" or status == "????" or status == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[2]").click()
            # ???╂?堕??
            if time == "?堕??" :
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[2]").click()
                self.driver.find_element_by_xpath\
                    ("/html/body/div[7]/table/thead/tr[2]/td[3]/div").click()
            elif time == "娓?绌?":
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[3]").click()
        elif status == "瀹℃?镐腑" or status == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[3]/input").click()
        # 瀹℃?告??浜?
        if action == "??浜?" or action == "submit":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[7]").click()
        elif action == "??缃?" or action == "reset":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[8]").click()
    # ?ㄤ???浣?澶?瀹¤????椤?
    def TruePublish(self,status,action):
        if status == "pass" or status == "瀹℃?搁??杩?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[1]/input").click()
        elif status == "return" or status == "??????瀹?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[2]/input").click()
        if action == "submit" or action == "??浜?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[7]").click()
        elif action == "reset" or action == "??缃?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[8]").click()
    # ?ㄤ???浣???娆剧??棣?椤靛?ㄤ??ц?
    def DFristPageAction(self,action,status):
        if action == "fristpage" or action == "棣?椤?" or action == "fp":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[5]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
        elif action == "borrow" or action == "???归??" or action == "br":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
        elif action == "refund" or action == "杩?娆惧??" or action == "rf":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "login" or action == "?诲?" or action == "lg":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "register" or action == "娉ㄥ??" or action == "rs":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/span/a/span").click()
        elif action == "goinvest" or action == "???㈢??璐㈢??" or action == "gi":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a").click()
        elif action == "needmoney" or action == "??瑕??ㄩ??" or action == "nd":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/a/span").click()
        elif action == "easyrepay" or action == "蹇??疯?娆?" or action == "er":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a/span").click()
        elif action == "downloadiphone" or action == "iphone":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/a/img").click()
        elif action == "downloadandroid" or  action == "android":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/a/img").click()
    # ?ㄤ???浣??诲??ㄤ?锛???????娆剧??寮圭???诲???椤甸?㈣烦杞??诲?????璐㈢??寮瑰?虹?诲???椤甸?㈣烦杞??诲?锛?
    def FristWinLogin(self,user,pwd,method):
        self.driver.find_element_by_id("login-email-address").send_keys(user)
        self.driver.find_element_by_id("login-password").send_keys(pwd)
        if method == "0":
            self.driver.find_element_by_id("ajax-login-submit").click()
        elif method == "1":
            self.driver.find_element_by_id("user-login-submit").click()
    # ?ㄤ???浣???娆剧???ㄦ?疯?????ㄤ?
    def UserMenu(self,action):
        menu = self.driver.find_element_by_xpath\
            ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[1]")
        ActionChains.move_to_element(menu).perform()
        if action == "mypage" or action == "????涓婚〉":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[2]/a")\
                .click()
        elif action == "borrow" or action == "??瑕???娆?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[3]/a")\
                .click()
        elif action == "account" or action == "涓?浜鸿?剧疆":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[4]/a")\
                .click()
        elif action == "loginout" or action == "???虹?诲?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a")\
                .click()
    # ?ㄤ???浣???娆剧被??????
    def Borrow(self,type):
        if type == "25":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[1]/div[3]/a").click()
            time.sleep(2)
        elif type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[2]/div[3]/a").click()
            time.sleep(2)
    # ?ㄤ???浣?璐锋?捐????椤靛?ㄤ?
    def BorrowStepone(self,money,repaytime,QQ,describe,status,type):
        self.driver.find_element_by_class_name("lh30")
        self.driver.find_element_by_id("borrowamount").send_keys(money)
        self.driver.find_element_by_xpath\
            ("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dt/i").click()
        if repaytime == "6" and type == "25" or repaytime == "1" and type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dd/a[1]").click()
        elif repaytime == "7" and type == "25" or repaytime == "2" and type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dd/a[2]").click()
        elif repaytime == "8" and type == "25" or repaytime == "3" and type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dd/a[3]").click()
        elif repaytime == "9" and type == "25":
            self.driver.find_element_by_xpath\
                ("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dd/a[4]").click()
        self.driver.find_element_by_id("borrowQQ").send_keys(QQ)
        self.driver.find_element_by_class_name("ke-edit-iframe").send_keys(describe)
        if status == "save" or status == "淇?瀛?":
            self.driver.find_element_by_id("saveBtn").click()
        elif status == "publish" or status == "??浜ゅ?℃??":
            self.driver.find_element_by_id("publishBnt").click()
            self.driver.switch_to_alert().accept()
        elif status == "preview" or status == "棰?瑙?":
            self.driver.find_element_by_id("previewBtn").click()

