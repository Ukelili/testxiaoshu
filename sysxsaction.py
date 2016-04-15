# coding: gb2312
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time,os


class SysXSAdmin(object):
    ''' ��������� '''
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
        print('���������')
    # url��ַ
    def UrlOpen(self,url):
        self.driver.maximize_window()
        self.driver.get(url) # Load page
    # �ر������
    def Quitbrow(self):
        self.driver.quit()  # Quit Browser
    # ��¼ϵͳ��̨
    def SysLogin(self,user,pwd,verify):
        self.driver.find_element_by_class_name("adm_name").send_keys(user)  # Input User name
        self.driver.find_element_by_class_name("adm_password").send_keys(pwd)  # Input password
        self.driver.find_element_by_name("adm_verify").send_keys(verify)  # Input verify
        self.driver.find_element_by_id("login_btn").click()
        print('ϵͳ��̨��¼')
    # ���ڲ���menu�˵�
    def MenuTpye(self,listnum):
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[1]/a").click()  # ���ϵͳ��ҳ
            print('��̨ϵͳ��ҳ')
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/a").click()  # ����������
            print('�������')
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[3]/a").click()  # �����Ա����
            print('��Ա����')
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]/a").click()  # ����ʽ����
            print('�ʽ����')
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[5]/a").click()  # �����������
            print('��������')
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[6]/a").click()  # ���ͳ��ģ��
            print('ͳ��ģ��')
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[7]/a").click()  # ������Ź���
            print('���Ź���')
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[8]/a").click()  # ������кϻ���
            print('���кϻ���')
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[9]/a").click()  # ��������̳�
            print('�����̳�')
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[10]/a").click()  # ���ǰ������
            print('ǰ������')
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[11]/a").click()  # �������ƹ�
            print('����ƹ�')
        elif listnum == "12":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[12]/a").click()  # ���ϵͳ����
            print('ϵͳ����')
    # ���ڲ����������˵��µ��Ӳ˵�
    def LoanMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ���ȫ������
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ���Ԥ���д���
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ������ִ���
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ����������վ
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ��������־�б�
    # ���ڲ�����˹���������Ӳ˵�
    def DealMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # �����˹���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ����׵�������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ������������б�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ����ҵĴ�����б�
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ���������б�
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ���δ�������
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ������ڵĴ���
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # �������Ĵ���
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ������ʧ�ܵĴ���
    # ���ڲ����������������Ӳ˵�
    def FundDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ���������ſ�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ��������д���
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # �������ɴ���
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # �����ǰ������
    # ���ڲ�����֤�����˵�������Ӳ˵�
    def Bmoney(self,listmun):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # �����֤�����
        if listmun == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click() # ���������
        elif listmun == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ����ѷ���
        elif listmun == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ���������
    # ���ڲ������չ���˵�������Ӳ˵�
    def CollMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ������չ���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ����������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # �������������ϸ
    # ���ڲ��������¼�˵�������Ӳ˵�
    def DealLog(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ��������¼
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ����������˵�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ������ڴ��տ�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # �����վ�渶��
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[4]/a").click()  # ����տ���Ϣ
    # ���ڲ���Ͷ����Ϣ�˵�������Ӳ˵�
    def DealInfo(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ���Ͷ����Ϣ
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # �������Ͷ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ����ֶ�Ͷ��
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ����Զ�Ͷ��
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # ����ɹ���Ͷ��
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ���ʧ�ܵ�Ͷ��
    # ���ڲ���ծȨת�ò˵�������Ӳ˵�
    def Transfer(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ���ծȨת��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # �������ת��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # �������ת��
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ����ɹ�ת��
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # �������ת��
    # ���ڲ�������ʽ��������˵�������Ӳ˵�
    def MsgDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # �������ʽ��������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # �������ʽ��������
        try:
           if listnum <= "0":
               print("error")
        except Exception:
            raise NameError("Not found %s listnum,You can enter '1'....." %listnum)
    # ���ڲ������Թ���˵�������Ӳ˵�
    def MsgMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ������Թ���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd/a").click()  # ��������б�
    # ���ڲ���ҵ��Ա��ѯ�˵�������Ӳ˵�
    def BusMan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[11]/dt").click()  # ���ҵ��Ա��ѯ
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[1]/a").click()  # ����Ƽ��˲�ѯ
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[2]/a").click()  # �������˲�ѯ
    # ���ڲ�����ͨ��Ա�˵�������Ӳ˵�
    def User(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # �����ͨ��Ա
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # �����ͨ�û�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # �������û�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # �������û�
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # �����������
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ���С��������
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # �������������
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # �������˻�Ա
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # �����Ա��Ϣ
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # �����Ա����վ
    # ���ڲ�����ҵ��Ա�˵�������Ӳ˵�
    def UesrCompany(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click() # �����ҵ��Ա
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # �����ҵ��Ա
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # �����Ա������
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # �������˻�Ա
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # �����Ա��Ϣ
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # �����Ա����վ
    # ���ڲ������������˵�������Ӳ˵�
    def DealAgency(self,liestnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # �����������
        if liestnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # �����������
        elif liestnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ���������������վ
    # ���ڲ���������Ϣ�˵�������Ӳ˵�
    def CompanyManage(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ���������Ϣ
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # �����˾�б�
        elif listnum =="2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ���������Ϣ
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ������п��б�
    # ���ڲ����������˵�������Ӳ˵�
    def EcvMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ��� �������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd/a")  # ����������
    # ���ڲ���������ò˵�������Ӳ˵�
    def AboutConfig(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # �����Ա�ֶ��б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # ������õȼ��б�
    # ���ڲ���վ����Ϣ�˵�������Ӳ˵�
    def MsgSystem(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # ���վ����Ϣ
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # �����ϢȺ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # �����Ϣ�б�
    # ���ڲ���VIP��Ȩ�˵�������Ӳ˵�
    def VipPrivilege(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ���VIP��Ȩ
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ���VIP��Ա�б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ���VIP�ȼ�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # ���VIP�����б�
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # ���VIP���û���վ
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[5]/a").click()  # ���VIP������¼
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[6]/a").click() # ���VIP������¼
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[7]/a").click()  # ���VIP������־
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[8]/a").click()  # ����ͷ��б�
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[9]/a").click()  # ����ͷ�����վ
    # ���ڲ���Ͷ�ʽ����˵�������Ӳ˵�
    def VipGift(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ���Ͷ�ʽ���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[1]/a").click()  # ������������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[2]/a").click()  # �����Ʒ����
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[3]/a").click()  # ��������ֽ����
    # ���ڲ������ո����˵�������Ӳ˵�
    def VipFestivals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # ������ո���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[1]/a").click()  # ������ջ��ֱ�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[2]/a").click()  # ������������б�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[3]/a").click()  # �����������
    # ���ڲ�����Լ����˵�������Ӳ˵�
    def GenerationRepay(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # �����Լ����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd/a").click()  # �����Լ�����Ӳ˵�
    # ���ڲ������Ŷ������˵�������Ӳ˵�
    def DealQuota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ������Ŷ������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click()  # ��������б��Ӳ˵�
    # ���ڲ������ö������˵�������Ӳ˵�
    def Quota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ������ö������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # ��������б�
    # ���ڲ����ٱ�����˵�������Ӳ˵�
    def Reportguy(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ����ٱ�����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # ����ٱ��б�
    # ���ڲ�����֤����˵�������Ӳ˵�
    def CreditMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # �����֤����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ���������֤
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # �������˵���֤
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[3]/a").click()  # ���ͨ������֤
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[4]/a").click()  # ���ʧ�ܵ���֤
    # ���ڲ�����Ա�����˵�������Ӳ˵�
    def Referrals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # �����Ա����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # ������뷵���б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # �����������
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # ����ƹ����б�
    # ���ڲ������ͳ�Ʋ˵�������Ӳ˵�
    def StatisticsBorrow(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ��������ͳ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ���Ͷ������
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ���Ͷ�ʽ��
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # �������Ͷ��
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ����ѻؿ�
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ������տ�
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ���Ͷ������
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # ���Ͷ�ʶ����
    # ���ڲ�������ͳ�Ʋ˵�������Ӳ˵�
    def StatisticsLoan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # �������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ���������ͳ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ����������
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ��������
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ������ֽ��
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ����ѻ���
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ���������
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # ������ڻ���
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # ���������ϸ
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[9]/a").click()  # �����������
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[10]/a").click()  # ����������ݷ���
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[11]/a").click()  # ���������ͳ�ƱȽ�
    # ���ڲ���ծȨͳ�Ʋ˵�������Ӳ˵�
    def StatisticsClaims(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ���ծȨͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd").click()  # ���ծȨת��
    # ���ڲ���ƽ̨ͳ�Ʋ˵�������Ӳ˵�
    def WebsiteStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ���ƽ̨ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # �����ֵͳ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # �������ͳ��
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # ����û�ͳ��
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  #��������ͳ��
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[5]/a").click()  # �����վ�渶ͳ��
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[6]/a").click()  # �����վ����ͳ��
    # ���ڲ���У԰�г��˵�������Ӳҵ�
    def Agentsstatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]").click()  # ���У԰�г�ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click() # ���У԰У԰�г��б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ���У԰�г�ͳ��
    # ���ڲ�������Ա����˵�������Ӳ˵�
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # �������Ա����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ��������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ������Ż�վ
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ������ų�Ա
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ����������Ա
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ������������
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # ������н���
    # ���ڲ������ͳ�Ʋ˵�������Ӳ˵�
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ����������ͳ��
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # �����Ա���ͳ��
    # ���ڲ����ҵĻ�Ա�˵�������Ӳ˵�
    def MyMembership(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ����ҵĻ�Ա
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ����ҵĻ�Ա�б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ������µ����˵�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ��������˵�
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # ��������н���
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[5]/a").click()  # �������ɽ���
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[6]/a").click()  # ����ѻ��˽���
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[7]/a").click()  # �������Ա�б�
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[8]/a").click()  # ������˻�Ա�б�
    # ���ڲ������кϻ��˲˵�������Ӳ˵�
    def RegionPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ������кϻ���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ������кϻ����б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ������ɱ�֤���б�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ����ѽɱ�֤���¼
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # ���ҵ��Ա�б�
    # ���ڲ�������ͳ�Ʋ˵�������Ӳ˵�
    def LoanPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # �������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click() # �������ͳ���б�
    # ���ڲ�������ͳ�Ʋ˵�������Ӳ˵�
    def IncomeStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # �������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # �������ͳ���б�
    # ���ڲ�������ͳ�Ʋ˵�������Ӳ˵�
    def ExpiredStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # �������ͳ��
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # �������ͳ���б�
    # ���ڲ��������̳ǲ˵�������Ӳ˵�
    def Goods(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # ��������̳�
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd[1]/a").click()  # �����Ʒ�б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl/dd[2]/a").click()  # �����Ʒ����
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl/dd[3]/a").click()  # ����һ���Ʒ
    # ���ڲ������¹���˵�������Ӳ˵�
    def ArticleMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ������¹���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ��������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ������»���վ
    # ���ڲ������·���˵�������Ӳ˵�
    def ArticleCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # ������·���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ��������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ����������վ
    # ���ڲ���ǰ�����ò˵�������Ӳ˵�
    def NavSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # ���ǰ������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ��������˵��б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ���ͶƱ�����б�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ���ǰ�˹���б�
    # ���ڲ����������Ӳ˵�������Ӳ˵�
    def LinkGroup(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # �����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ����������ӷ���
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ������������б�
    # ���ڲ��������˵�������Ӳ˵�
    def Special(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # �������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd").click()  # ���Ů����ѡ
    # ����ϵͳ���ò˵�������Ӳ˵�
    def SysConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # ���ϵͳ����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # ���ϵͳ����
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # ���ǩ����������
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # ������뷵������
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # �����Ȩ���������Ӷ����
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # ���QQ�ͷ�����
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # �������������
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # ���������������
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # �����֤��������
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # ����û�ƽ̨ע����֤����
    # ���ڲ����������ò˵�������Ӳ˵�
    def DealCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # �����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # ��������������
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # ����������վ
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # ���������������
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # ������ͻ���վ
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # ��������������
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # ������л���վ
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # �����ͬ��������
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # �����������վ
    # ���ڲ�����������˵�������Ӳ˵�
    def LearnMoney(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # �����������
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # ��������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # ���Ͷ�ʼ�¼
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # ��������
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # �����Ʋ�Ʒ�б�
    # ���ڲ����ӿ����ò˵�������Ӳ˵�
    def AIPSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # ����ӿ�����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # ����ʽ��й�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # ���֧���ӿ�����
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # �����Ա��������¼
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  # �����Ա���ϲ��
    # ���ڲ����ƶ�ƽ���ò˵�������Ӳ˵�
    def MobileConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # ����ƶ�ƽ����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # ����ֻ�������
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # ����ֻ��˹���б�
    # ���ڲ���ϵͳ����˵�������Ӳ˵�
    def SyeRole(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # ���ϵͳ����Ա
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]").click()  # �����ɫ����
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]").click()  # �����ɫ����վ
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]").click()  # �������Ա��
    # ���ڲ�����Ϣ�ʼ�����˵�������Ӳ˵�
    def MsgMailMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click() # �����Ϣ�ʼ�����
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # �����Ϣģ�����
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # ����ʼ��������б�
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # ����ʼ��б�
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # �����Ϣ����б�
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[5]/a").click()  # �����Ϣ�б�
    # ���ڲ������й���˵�������Ӳ˵�
    def DealMsgList(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # ������й���
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # ���ҵ������б�
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # ����ƹ�����б�
    # ���ڲ������ݿ�˵�������Ӳ˵�
    def Database(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # ������ݿ�
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # ���SQL����
    # ���ڲ����׵�������б���˶���
    def FirstPublish(self,action):
        if action == "shcz" or action == "��˲���" :
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[13]/a").click()  # �����˲���
        elif action == "rl" or action == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()  # ����������
        elif action == "shrz" or action == "�����־":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # ��������־
        elif action == "dkmc" or action == "��������":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()  # �����������
        elif action == "jkr" or action == "�����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ��������
    # ���ڲ���������б���˶���
    def TruePublish(self,action):
        if action == "dkmc" or action == "��������":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()
        elif action == "jkr" or action == "�����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()
        elif action == "shcz" or action == "��˲���":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()
        elif action == "shrz" or action == "�����־":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()
    # ���ڲ������������б���˶���
    def Publish(self,action):
        if action == "shcz" or action == "��˲���" :
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # �����˲���
        elif action == "rl" or action == "����":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[16]/a").click()  # ����������
        elif action == "shrz" or action == "�����־":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[17]/a").click()  # ��������־
        elif action == "dkmc" or action == "��������":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[3]").click()  # �����������
        elif action == "jkr" or action == "�����":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # ��������
    # ���ڲ����������ҳ����˶���
    def PublishPage(self,state,city,type,status,time,action):
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]").click()  # ���ѡ����ʡ��
        if state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[2]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[3]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[4]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[5]").click()
        elif state == "�㶫":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[6]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[7]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[8]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[9]").click()
        elif state == "�ӱ�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[10]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[11]").click()
        elif state == "������":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[12]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[13]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[14]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[15]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[16]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[17]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[18]").click()
        elif state == "���ɹ�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[19]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[20]").click()
        elif state == "�ຣ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[21]").click()
        elif state == "ɽ��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[22]").click()
        elif state == "ɽ��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[23]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[24]").click()
        elif state == "�Ϻ�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[25]").click()
        elif state == "�Ĵ�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[26]").click()
        elif state == "���":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[27]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[28]").click()
        elif state == "�½�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[29]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[30]").click()
        elif state == "�㽭":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[31]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[32]").click()
        elif state == "���":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[33]").click()
        elif state == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[34]").click()
        elif state == "̨��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[35]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]").click()  # ���ѡ���г���
        if state == "����" and city == "����"\
                or state == "����" and city == "����" \
                or state == "����" and city == "����" \
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[2]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "����"\
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[3]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "��ƽ"\
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[4]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "����"\
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "��ݸ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[5]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "����"\
                or tate == "����" and city == "������" \
                or state == "�㶫" and city == "��ɽ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[6]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "Ȫ��"\
                or state == "����" and city == "���" \
                or state == "�㶫" and city == "��Դ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[7]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "����"\
                or state == "����" and city == "��Ȫ" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[8]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "����"\
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[9]").click()
        elif state == "����" and city == "��ɽ" \
                or state == "����" and city == "����"\
                or state == "����" and city == "¤��" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[10]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "ƽ��" \
                or state == "�㶫" and city == "ï��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[11]").click()
        elif state == "����" and city == "��ɽ" \
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "÷��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[12]").click()
        elif state == "����" and city == "����" \
                or state == "����" and city == "��ˮ" \
                or state == "�㶫" and city == "��Զ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[13]").click()
        elif state == "����" and city == "ͭ��" \
                or state == "����" and city == "����" \
                or state == "�㶫" and city == "��ͷ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[14]").click()
        elif state == "����" and city == "�ߺ�" \
                or state == "����" and city == "��Ҵ" \
                or state == "�㶫" and city == "��β":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[15]").click()
        elif state == "����" and city == "����" \
                or state == "�㶫" and city == "�ع�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[16]").click()
        elif state == "����" and city == "����" \
                or state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[17]").click()
        elif state == "����" and city == "�Ϸ�" \
                or state == "�㶫" and city == "�Ƹ�":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[18]").click()
        elif state == "�㶫" and city == "տ��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[19]").click()
        elif state == "�㶫" and city == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[20]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select").click()  # ���ѡ�н����;
        if type == "��ҵ���" or type == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[2]").click()
        elif type == "������" or type == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[3]").click()
        elif type == "���ν��" or type == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[4]").click()
        elif type == "����Խ��" or type == "4":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[5]").click()
        elif type == "���ֻ����" or type == "5":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[6]").click()
        elif type == "������" or type == "6":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[7]").click()
        elif type == "�����ս��" or type == "7":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[8]").click()
        elif type == "����ѽ��" or type == "8":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[9]").click()
        elif type == "�������ѽ��" or type == "9":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[10]").click()
        # ѡ����״̬
        if status == "���ʧ��" or status == "ʧ��" or status == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[1]/input").click()
        elif status == "��˳ɹ�" or status == "�ɹ�" or status == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[2]").click()
            # ѡ��ʱ��
            if time == "ʱ��" :
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[2]").click()
                self.driver.find_element_by_xpath\
                    ("/html/body/div[7]/table/thead/tr[2]/td[3]/div").click()
            elif time == "���":
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[3]").click()
        elif status == "�����" or status == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[3]/input").click()
        # ����ύ
        if action == "�ύ" or action == "submit":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[7]").click()
        elif action == "����" or action == "reset":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[8]").click()
    # ���ڲ�����������ҳ
    def TruePublish(self,status,action):
        if status == "pass" or status == "���ͨ��":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[1]/input").click()
        elif status == "return" or status == "�˻س���":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[2]/input").click()
        if action == "submit" or action == "�ύ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[7]").click()
        elif action == "reset" or action == "����":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[8]").click()
    # ���ڲ���������ҳ����ִ��
    def DFristPageAction(self,action,status):
        if action == "fristpage" or action == "��ҳ" or action == "fp":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[5]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
        elif action == "borrow" or action == "���Ǯ" or action == "br":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
        elif action == "refund" or action == "������" or action == "rf":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "login" or action == "��¼" or action == "lg":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "register" or action == "ע��" or action == "rs":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/span/a/span").click()
        elif action == "goinvest" or action == "�л���ư�" or action == "gi":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a").click()
        elif action == "needmoney" or action == "��Ҫ��Ǯ" or action == "nd":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/a/span").click()
        elif action == "easyrepay" or action == "��ݻ���" or action == "er":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a/span").click()
        elif action == "downloadiphone" or action == "iphone":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/a/img").click()
        elif action == "downloadandroid" or  action == "android":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/a/img").click()
    # ���ڲ�����¼�������������˵�����¼��ҳ����ת��¼����ƶ˵�����¼��ҳ����ת��¼��
    def FristWinLogin(self,user,pwd,method):
        self.driver.find_element_by_id("login-email-address").send_keys(user)
        self.driver.find_element_by_id("login-password").send_keys(pwd)
        if method == "0":
            self.driver.find_element_by_id("ajax-login-submit").click()
        elif method == "1":
            self.driver.find_element_by_id("user-login-submit").click()
    # ���ڲ��������û��˵�����
    def UserMenu(self,action):
        menu = self.driver.find_element_by_xpath\
            ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[1]")
        ActionChains.move_to_element(menu).perform()
        if action == "mypage" or action == "�ҵ���ҳ":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[2]/a")\
                .click()
        elif action == "borrow" or action == "��Ҫ���":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[3]/a")\
                .click()
        elif action == "account" or action == "��������":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[4]/a")\
                .click()
        elif action == "loginout" or action == "�˳���¼":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a")\
                .click()
    # ���ڲ����������ѡ��
    def Borrow(self,type):
        if type == "25":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[1]/div[3]/a").click()
            time.sleep(2)
        elif type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[2]/div[3]/a").click()
            time.sleep(2)
    # ���ڲ�����������ҳ����
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
        if status == "save" or status == "����":
            self.driver.find_element_by_id("saveBtn").click()
        elif status == "publish" or status == "�ύ���":
            self.driver.find_element_by_id("publishBnt").click()
            self.driver.switch_to_alert().accept()
        elif status == "preview" or status == "Ԥ��":
            self.driver.find_element_by_id("previewBtn").click()

