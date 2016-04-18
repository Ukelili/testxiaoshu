# coding: gb2312
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time,os


class SysXSAdmin(object):
    ''' ???��?�??? '''
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
        print('???��?�???')
    # url?��??
    def UrlOpen(self,url):
        self.driver.maximize_window()
        self.driver.get(url) # Load page
    # ?��??�?�???
    def Quitbrow(self):
        self.driver.quit()  # Quit Browser
    # ?��?系�?????
    def SysLogin(self,user,pwd,verify):
        self.driver.find_element_by_class_name("adm_name").send_keys(user)  # Input User name
        self.driver.find_element_by_class_name("adm_password").send_keys(pwd)  # Input password
        self.driver.find_element_by_name("adm_verify").send_keys(verify)  # Input verify
        self.driver.find_element_by_id("login_btn").click()
        print('系�????��?��?')
    # ?��???�?menu????
    def MenuTpye(self,listnum):
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[1]/a").click()  # ?��?�系�?�?�?
            print('???�系�?�?�?')
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/a").click()  # ?��?�贷款�?��??
            print('贷�?��?��??')
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[3]/a").click()  # ?��?��???管�??
            print('�???管�??')
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]/a").click()  # ?��?��???管�??
            print('�???管�??')
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[5]/a").click()  # ?��?��???�???
            print('�???�???')
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[6]/a").click()  # ?��?��?计模??
            print('�?计模??')
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[7]/a").click()  # ?��?��?��?��?��??
            print('?��?��?��??')
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[8]/a").click()  # ?��?��??�???�?�?
            print('??�???�?�?')
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[9]/a").click()  # ?��?�积??????
            print('�???????')
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[10]/a").click()  # ?��?��??�?设置
            print('??�?设置')
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[11]/a").click()  # ?��?�活?��??�广
            print('活�?��??�广')
        elif listnum == "12":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[12]/a").click()  # ?��?�系�?设置
            print('系�?设置')
    # ?��???�?贷�?��?��??????�???�?????
    def LoanMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?�贷款�?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��?��?�贷�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��???�?贷�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?��?��??贷�??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?�贷款�???��??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?��?��?��?��?��???�?
    # ?��???�?审�?��?��??�??��??�?????
    def DealMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?��?��?��?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?��???�?审�?��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?�续??�?审�?��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?��?��????�?审�?��??�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?��?��?审�?��??�?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?��?��??满�??贷�??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?��?��?????贷�??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?��?��?????贷�??
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?��?��?��?�失败�??贷�??
    # ?��???�?满�??管�??�??��??�?????
    def FundDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?�满??管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?��?�满??�??��??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?��?��?款中贷�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?��?�已�???贷�??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?��?��????�?贷�??
    # ?��???�?�?�???管�??????�??��??�?????
    def Bmoney(self,listmun):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?��?�???管�??
        if listmun == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click() # ?��?��?�?�?
        elif listmun == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?��?�已�?�?
        elif listmun == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?��?��???��??
    # ?��???�????��?��??????�??��??�?????
    def CollMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?��?��???��?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?��?��????��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?��?��????��????�?
    # ?��???�???贷�?��?????�??��??�?????
    def DealLog(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?��?��??贷�?��?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?��?��?�?款账??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?��?��?��??�??��??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # ?��?��?�???�?�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[4]/a").click()  # ?��?��?��?�信??
    # ?��???�?????信�??????�??��??�?????
    def DealInfo(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ?��?��????信�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?��?��????????
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?��?��???��????
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ?��?��???��????
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # ?��?��??????????
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?��?�失败�??????
    # ?��???�??��??�?让�????�??��??�?????
    def Transfer(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?��?��?��??�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?��?��????�?�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?��?��?��?�转�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ?��?��????�?�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # ?��?��?��??�?�?
    # ?��???�???�?�?贷�?��?��?��????�??��??�?????
    def MsgDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?��?��??�?�?贷�?��?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # ?��?��??�?�?贷�?��?��??
        try:
           if listnum <= "0":
               print("error")
        except Exception:
            raise NameError("Not found %s listnum,You can enter '1'....." %listnum)
    # ?��???�???�?管�??????�??��??�?????
    def MsgMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ?��?��??�?管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd/a").click()  # ?��?��??�???�?
    # ?��???�?�??��???��?��????�??��??�?????
    def BusMan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[11]/dt").click()  # ?��?��??��???��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[1]/a").click()  # ?��?��?��??人�?��??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[2]/a").click()  # ?��?��?审�?��?��??
    # ?��???�?????�???????�??��??�?????
    def User(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?��????�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��?????��??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��??款�?��??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?��??财�?��??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?��????????
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?��?��???�?????
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?��?��?贷�?????
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?��?��?审�?��???
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?��?��???信�??
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # ?��?��??????��??
    # ?��???�?�?�?�???????�??��??�?????
    def UesrCompany(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click() # ?��?��?�?�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?��?�?�???
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?��???�?????
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?��?��?审�?��???
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?��?��???信�??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?��?��??????��??
    # ?��???�???�??��??????�??��??�?????
    def DealAgency(self,liestnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��??�??��??
        if liestnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?��?��??�??��??
        elif liestnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?��?��??�??��?????��??
    # ?��???�??��?信�??????�??��??�?????
    def CompanyManage(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?��?��?信�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?��?��???��??�?
        elif listnum =="2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?��?�工�?信�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?��?��?��??��??�?
    # ?��???�?红�??管�??????�??��??�?????
    def EcvMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?��?? 红�??管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd/a")  # ?��?�红??类�??
    # ?��???�??��?��??�?????�??��??�?????
    def AboutConfig(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?��?��?��?��??�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?��?��???�?段�??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?��?�信?��??级�??�?
    # ?��???�?�???�???????�??��??�?????
    def MsgSystem(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ?��?��????�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?��?��???群�??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?��?��?????�?
    # ?��???�?VIP?��??????�??��??�?????
    def VipPrivilege(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?��??VIP?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?��??VIP�?????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?��??VIP�?�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ?��??VIP??�???�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # ?��??VIP??�????��??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[5]/a").click()  # ?��??VIP??级�?��?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[6]/a").click() # ?��??VIP??级�?��?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[7]/a").click()  # ?��??VIP�?买�?��?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[8]/a").click()  # ?��?��?��????�?
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[9]/a").click()  # ?��?��?��?????��??
    # ?��???�???�?�??��????�??��??�?????
    def VipGift(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?��?��??�?�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[1]/a").click()  # ?��?��??��???��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[2]/a").click()  # ?��?�礼??管�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[3]/a").click()  # ?��?��?????��??管�??
    # ?��???�????��??��????�??��??�?????
    def VipFestivals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ?��?��???��???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[1]/a").click()  # ?��?��???�积??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[2]/a").click()  # ?��?��??��???��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[3]/a").click()  # ?��?�积???��??
    # ?��???�?�?�??��?��????�??��??�?????
    def GenerationRepay(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?�续�??��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd/a").click()  # ?��?�续�??��?��??????
    # ?��???�???信�?�??��?��????�??��??�?????
    def DealQuota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?��??信�?�??��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click()  # ?��?��?��?��??表�??????
    # ?��???�?信�?��?�??��?��????�??��??�?????
    def Quota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?�信?��?�??��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # ?��?��?��?��??�?
    # ?��???�?举�?��?��??????�??��??�?????
    def Reportguy(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?�举?��?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # ?��?�举?��??�?
    # ?��???�?认�??管�??????�??��??�?????
    def CreditMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?��?��?��??管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?��?��????认�??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?��?��?审�?��??认�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[3]/a").click()  # ?��?��??�???认�??
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[4]/a").click()  # ?��?�失败�??认�??
    # ?��???�?�???�??��????�??��??�?????
    def Referrals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?��?��???�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ?��?��??请�??��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ?��?�建�??��??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # ?��?��?�广人�??�?
    # ?��???�????��?计�????�??��??�?????
    def StatisticsBorrow(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?��???��?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��???��?��?�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��??�?人�??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?��??�???�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?��??�???�?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?��?�已??�?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?��?��??��??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?��?��??�?????
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?��?��??�?�?�?�?
    # ?��???�????��?计�????�??��??�?????
    def StatisticsLoan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?��???��?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?��???��?��?�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?��??款人??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?��?��??款�??�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?��?��??�???�?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?��?�已�?�?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?��?��?�?�?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?��?��?��??�?�?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?��?��?��????�?
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[9]/a").click()  # ?��?��?��????�?
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[10]/a").click()  # ?��?��?��???��??????
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[11]/a").click()  # ?��?��?��???��?计�??�?
    # ?��???�??��??�?计�????�??��??�?????
    def StatisticsClaims(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��?��??�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd").click()  # ?��?��?��??�?�?
    # ?��???�?平�?��?计�????�??��??�?????
    def WebsiteStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?��?�平?��?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?��?��???��?�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?��?��???��?�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?��?��?��?��?�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  #?��?�年�?段�?�?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[5]/a").click()  # ?��?��?�???�?�?�?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[6]/a").click()  # ?��?��?�?费�?��?�?
    # ?��???�??��??�??��????�??��??�??�淡
    def Agentsstatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]").click()  # ?��?��?��??�??��?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click() # ?��?��?��???��??�??��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?��?��?��??�??��?�?
    # ?��???�?管�????管�??????�??��??�?????
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?��?��????管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��?��?��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��?��?��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?��?��?��????
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?��?????�???
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?��?��???????款�??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?��?��??????款�??
    # ?��???�?????�?计�????�??��??�?????
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?��????�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?��?��?��????�?�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?��????????�?�?
    # ?��???�?????�???????�??��??�?????
    def MyMembership(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��????�???
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?��?��????�?????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?��?��?????��??�???
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?��?��?��??�???
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?��?��?款中??款�??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[5]/a").click()  # ?��?�已�?????款�??
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[6]/a").click()  # ?��?�已??�???款�??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[7]/a").click()  # ?��?��??款�?????�?
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[8]/a").click()  # ?��?��??�?�?????�?
    # ?��???�???�???�?人�????�??��??�?????
    def RegionPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?��??�???�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��??�???�?人�??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��?缴�?�?????�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?�已缴�?�???记�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?��??��????�?
    # ?��???�?贷�?��?计�????�??��??�?????
    def LoanPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?�贷款�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click() # ?��?�贷款�?计�??�?
    # ?��???�??��??�?计�????�??��??�?????
    def IncomeStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��?��??�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # ?��?��?��??�?计�??�?
    # ?��???�??��??�?计�????�??��??�?????
    def ExpiredStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?��?��??�?�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # ?��?��?��??�?计�??�?
    # ?��???�?�???????????�??��??�?????
    def Goods(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # ?��?�积??????
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd[1]/a").click()  # ?��?��??????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl/dd[2]/a").click()  # ?��?��??????�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl/dd[3]/a").click()  # ?��?��???��????
    # ?��???�???�?管�??????�??��??�?????
    def ArticleMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?��??�?管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?��??�???�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��??�????��??
    # ?��???�???�???类�????�??��??�?????
    def ArticleCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?��??�???�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?��??类�??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?��??类�???��??
    # ?��???�???�?设置????�??��??�?????
    def NavSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��??�?设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?��?��?��????????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?��?��??票�??��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?��?��??�?广�????�?
    # ?��???�??????��?��????�??��??�?????
    def LinkGroup(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?��?????��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?��?��?????��?��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?��?��?????��?��??�?
    # ?��???�??�年活�?��????�??��??�?????
    def Special(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # ?��?��?�年活�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd").click()  # ?��?�女�?�???
    # ?��?系�?设置????�??��??�?????
    def SysConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ?��?�系�?设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ?��?�系�???�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ?��?��?��?��??��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ?��?��??请�??��??�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ?��?��???????��?��??�?佣�?�置
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ?��??QQ客�????�?
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ?��?��???��??�?�?
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ?��?��???��?��?设置
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ?��?��?��??类�??设置
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # ?��?��?��?�平?�注??�?�?设置
    # ?��???�?贷�?��?�置????�??��??�?????
    def DealCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ?��?�贷款�?�置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ?��?�贷款�??类�?�置
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ?��?��??类�???��??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ?��?�贷款类??设置
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ?��?�类?????��??
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ?��?�贷款�??�?设置
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ?��?��??�????��??
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ?��?��????????设置
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ?��?��???????��??
    # ?��???�?�?�???管�??????�??��??�?????
    def LearnMoney(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ?��?��?�???管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ?��?��???��??�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ?��?��??�?记�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ?��?�活?��?�置
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ?��?��??�?产�????�?
    # ?��???�??��?��?�置????�??��??�?????
    def AIPSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ?��?��?��?��?�置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ?��?��?????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ?��?��??�??��?��?�置
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ?��?��???�?�??��?��?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  # ?��?��????��????�?
    # ?��???�?移�?�平设置????�??��??�?????
    def MobileConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ?��?�移?�平设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ?��?��???��????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ?��?��???��??广�????�?
    # ?��???�?系�?管�??????�??��??�?????
    def SyeRole(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ?��?�系�?管�????
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]").click()  # ?��?��??��?��??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]").click()  # ?��?��??��???��??
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]").click()  # ?��?��?��????�?
    # ?��???�???????件�?��??????�??��??�?????
    def MsgMailMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click() # ?��?��??????件�?��??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # ?��?��???模�?��?��??
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ?��?��??件�???��?��??�?
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ?��?��??件�??�?
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # ?��?��??????款�??�?
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[5]/a").click()  # ?��?��??????�?
    # ?��???�?????管�??????�??��??�?????
    def DealMsgList(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ?��?��????管�??
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ?��?��??��??????�?
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ?��?��?�广??????�?
    # ?��???�??��??�?????�??��??�?????
    def Database(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ?��?��?��??�?
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # ?��??SQL??�?
    # ?��???�?�???�?审�?��??表�?��?��?��?
    def FirstPublish(self,action):
        if action == "shcz" or action == "审�?��??�?" :
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[13]/a").click()  # ?��?��?��?��??�?
        elif action == "rl" or action == "认�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()  # ?��?��?��???�?
        elif action == "shrz" or action == "审�?��?��?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # ?��?��?��?��?��?
        elif action == "dkmc" or action == "贷�?��??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()  # ?��?�贷款�??�?
        elif action == "jkr" or action == "??款人":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ?��?��??款人
    # ?��???�?�?审�?��??表�?��?��?��?
    def TruePublish(self,action):
        if action == "dkmc" or action == "贷�?��??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()
        elif action == "jkr" or action == "??款人":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()
        elif action == "shcz" or action == "审�?��??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()
        elif action == "shrz" or action == "审�?��?��?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()
    # ?��???�?�???�?审�?��??表�?��?��?��?
    def Publish(self,action):
        if action == "shcz" or action == "审�?��??�?" :
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # ?��?��?��?��??�?
        elif action == "rl" or action == "认�?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[16]/a").click()  # ?��?��?��???�?
        elif action == "shrz" or action == "审�?��?��?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[17]/a").click()  # ?��?��?��?��?��?
        elif action == "dkmc" or action == "贷�?��??�?":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[3]").click()  # ?��?�贷款�??�?
        elif action == "jkr" or action == "??款人":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ?��?��??款人
    # ?��???�?审�?��????页�??审�?��?��?
    def PublishPage(self,state,city,type,status,time,action):
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]").click()  # ?��?��???�中??�?
        if state == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[2]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[3]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[4]").click()
        elif state == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[5]").click()
        elif state == "广�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[6]").click()
        elif state == "广西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[7]").click()
        elif state == "贵�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[8]").click()
        elif state == "海�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[9]").click()
        elif state == "河�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[10]").click()
        elif state == "河�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[11]").click()
        elif state == "�?�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[12]").click()
        elif state == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[13]").click()
        elif state == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[14]").click()
        elif state == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[15]").click()
        elif state == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[16]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[17]").click()
        elif state == "辽�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[18]").click()
        elif state == "??????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[19]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[20]").click()
        elif state == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[21]").click()
        elif state == "山�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[22]").click()
        elif state == "山西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[23]").click()
        elif state == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[24]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[25]").click()
        elif state == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[26]").click()
        elif state == "天津":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[27]").click()
        elif state == "西�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[28]").click()
        elif state == "?��??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[29]").click()
        elif state == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[30]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[31]").click()
        elif state == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[32]").click()
        elif state == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[33]").click()
        elif state == "澳�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[34]").click()
        elif state == "?�湾":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[35]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]").click()  # ?��?��???�中??�?
        if state == "??�?" and city == "??�?"\
                or state == "�?�?" and city == "�?�?" \
                or state == "�?�?" and city == "�?�?" \
                or state == "????" and city == "?��?" \
                or state == "广�?" and city == "广�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[2]").click()
        elif state == "�?�?" and city == "????" \
                or state == "�?�?" and city == "�?�?"\
                or state == "????" and city == "?��??" \
                or state == "广�?" and city == "深�??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[3]").click()
        elif state == "�?�?" and city == "巢�?" \
                or state == "�?�?" and city == "??�?"\
                or state == "????" and city == "�?�?" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[4]").click()
        elif state == "�?�?" and city == "�?�?" \
                or state == "�?�?" and city == "�?�?"\
                or state == "????" and city == "????" \
                or state == "广�?" and city == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[5]").click()
        elif state == "�?�?" and city == "�?�?" \
                or state == "�?�?" and city == "????"\
                or tate == "????" and city == "??�???" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[6]").click()
        elif state == "�?�?" and city == "????" \
                or state == "�?�?" and city == "�?�?"\
                or state == "????" and city == "????" \
                or state == "广�?" and city == "河�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[7]").click()
        elif state == "�?�?" and city == "�???" \
                or state == "�?�?" and city == "�???"\
                or state == "????" and city == "??�?" \
                or state == "广�?" and city == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[8]").click()
        elif state == "�?�?" and city == "�???" \
                or state == "�?�?" and city == "????"\
                or state == "????" and city == "临�?" \
                or state == "广�?" and city == "�???":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[9]").click()
        elif state == "�?�?" and city == "�?�?" \
                or state == "�?�?" and city == "漳�?"\
                or state == "????" and city == "????" \
                or state == "广�?" and city == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[10]").click()
        elif state == "�?�?" and city == "??�?" \
                or state == "????" and city == "平�??" \
                or state == "广�?" and city == "????":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[11]").click()
        elif state == "�?�?" and city == "�???�?" \
                or state == "????" and city == "�???" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[12]").click()
        elif state == "�?�?" and city == "宿�?" \
                or state == "????" and city == "天水" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[13]").click()
        elif state == "�?�?" and city == "????" \
                or state == "????" and city == "�?�?" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[14]").click()
        elif state == "�?�?" and city == "??�?" \
                or state == "????" and city == "�???" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[15]").click()
        elif state == "�?�?" and city == "宣�??" \
                or state == "广�?" and city == "?��??":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[16]").click()
        elif state == "�?�?" and city == "亳�?" \
                or state == "广�?" and city == "?��?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[17]").click()
        elif state == "�?�?" and city == "????" \
                or state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[18]").click()
        elif state == "广�?" and city == "�?�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[19]").click()
        elif state == "广�?" and city == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[20]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select").click()  # ?��?��??�???款�?��??
        if type == "??�???�?" or type == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[2]").click()
        elif type == "�?�???�?" or type == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[3]").click()
        elif type == "??游�??�?" or type == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[4]").click()
        elif type == "买�?��????�?" or type == "4":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[5]").click()
        elif type == "买�???��??�?" or type == "5":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[6]").click()
        elif type == "�??��??�?" or type == "6":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[7]").click()
        elif type == "??驾�?��??�?" or type == "7":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[8]").click()
        elif type == "??活费??�?" or type == "8":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[9]").click()
        elif type == "?��?�?费�??�?" or type == "9":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[10]").click()
        # ???��?��?��??
        if status == "审�?�失�?" or status == "失败" or status == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[1]/input").click()
        elif status == "审�?��????" or status == "????" or status == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[2]").click()
            # ???��?��??
            if time == "?��??" :
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[2]").click()
                self.driver.find_element_by_xpath\
                    ("/html/body/div[7]/table/thead/tr[2]/td[3]/div").click()
            elif time == "�?�?":
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[3]").click()
        elif status == "审�?�中" or status == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[3]/input").click()
        # 审�?��??�?
        if action == "??�?" or action == "submit":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[7]").click()
        elif action == "??�?" or action == "reset":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[8]").click()
    # ?��???�?�?审�????�?
    def TruePublish(self,status,action):
        if status == "pass" or status == "审�?��??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[1]/input").click()
        elif status == "return" or status == "??????�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[2]/input").click()
        if action == "submit" or action == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[7]").click()
        elif action == "reset" or action == "??�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[8]").click()
    # ?��???�???款�??�?页�?��??��?
    def DFristPageAction(self,action,status):
        if action == "fristpage" or action == "�?�?" or action == "fp":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[5]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
        elif action == "borrow" or action == "???��??" or action == "br":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
        elif action == "refund" or action == "�?款�??" or action == "rf":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "login" or action == "?��?" or action == "lg":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "register" or action == "注�??" or action == "rs":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/span/a/span").click()
        elif action == "goinvest" or action == "???��??财�??" or action == "gi":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a").click()
        elif action == "needmoney" or action == "??�??��??" or action == "nd":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/a/span").click()
        elif action == "easyrepay" or action == "�??��?�?" or action == "er":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a/span").click()
        elif action == "downloadiphone" or action == "iphone":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/a/img").click()
        elif action == "downloadandroid" or  action == "android":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/a/img").click()
    # ?��???�??��??��?�???????款�??弹�???��???页�?�跳�??��?????财�??弹�?��?��???页�?�跳�??��?�?
    def FristWinLogin(self,user,pwd,method):
        self.driver.find_element_by_id("login-email-address").send_keys(user)
        self.driver.find_element_by_id("login-password").send_keys(pwd)
        if method == "0":
            self.driver.find_element_by_id("ajax-login-submit").click()
        elif method == "1":
            self.driver.find_element_by_id("user-login-submit").click()
    # ?��???�???款�???��?��?????��?
    def UserMenu(self,action):
        menu = self.driver.find_element_by_xpath\
            ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[1]")
        ActionChains.move_to_element(menu).perform()
        if action == "mypage" or action == "????主页":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[2]/a")\
                .click()
        elif action == "borrow" or action == "??�???�?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[3]/a")\
                .click()
        elif action == "account" or action == "�?人�?�置":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[4]/a")\
                .click()
        elif action == "loginout" or action == "???��?��?":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a")\
                .click()
    # ?��???�???款类??????
    def Borrow(self,type):
        if type == "25":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[1]/div[3]/a").click()
            time.sleep(2)
        elif type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[2]/div[3]/a").click()
            time.sleep(2)
    # ?��???�?贷�?��????页�?��?
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
        if status == "save" or status == "�?�?":
            self.driver.find_element_by_id("saveBtn").click()
        elif status == "publish" or status == "??交�?��??":
            self.driver.find_element_by_id("publishBnt").click()
            self.driver.switch_to_alert().accept()
        elif status == "preview" or status == "�?�?":
            self.driver.find_element_by_id("previewBtn").click()

