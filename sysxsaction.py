# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time,os


class SysXSAdmin(object):
    ''' 启动浏览器 '''
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
        print('启动浏览器')
    # url地址
    def UrlOpen(self,url):
        self.driver.maximize_window()
        self.driver.get(url) # Load page
    # 关闭浏览器
    def Quitbrow(self):
        self.driver.quit()  # Quit Browser
    # 登录系统后台
    def SysLogin(self,user,pwd,verify):
        self.driver.find_element_by_class_name("adm_name").send_keys(user)  # Input User name
        self.driver.find_element_by_class_name("adm_password").send_keys(pwd)  # Input password
        self.driver.find_element_by_name("adm_verify").send_keys(verify)  # Input verify
        self.driver.find_element_by_id("login_btn").click()
        print('系统后台登录')
    # 用于操作menu菜单
    def MenuTpye(self,listnum):
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[1]/a").click()  # 点击系统首页
            print('后台系统首页')
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[2]/a").click()  # 点击贷款管理
            print('贷款管理')
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[3]/a").click()  # 点击会员管理
            print('会员管理')
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[4]/a").click()  # 点击资金管理
            print('资金管理')
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[5]/a").click()  # 点击待办事物
            print('待办事物')
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[6]/a").click()  # 点击统计模块
            print('统计模块')
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[7]/a").click()  # 点击部门管理
            print('部门管理')
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[8]/a").click()  # 点击城市合伙人
            print('城市合伙人')
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[9]/a").click()  # 点击积分商城
            print('积分商城')
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[10]/a").click()  # 点击前端设置
            print('前端设置')
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[11]/a").click()  # 点击活动与推广
            print('活动与推广')
        elif listnum == "12":
            self.driver.find_element_by_xpath("/html/body/div[4]/ul/li[12]/a").click()  # 点击系统设置
            print('系统设置')
    # 用于操作贷款管理菜单下的子菜单
    def LoanMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击贷款管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击全部贷款
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击预告中贷款
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击新手贷款
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击贷款回收站
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # 点击审核日志列表
    # 用于操作审核管理下面的子菜单
    def DealMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击审核管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击首单待审核列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击续借待审核列表
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # 点击我的待审核列表
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # 点击复审核列表
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # 点击未满标贷款
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # 点击过期的贷款
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # 点击流标的贷款
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # 点击审核失败的贷款
    # 用于操作满标管理下面的子菜单
    def FundDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击满标管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # 点击满标待放款
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # 点击还款中贷款
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # 点击已完成贷款
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # 点击提前还贷款
    # 用于操作保证金管理菜单下面的子菜单
    def Bmoney(self,listmun):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击保证金管理
        if listmun == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click() # 点击待返还
        elif listmun == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # 点击已返还
        elif listmun == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # 点击有逾期
    # 用于操作催收管理菜单下面的子菜单
    def CollMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # 点击催收管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # 点击待催收列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # 点击待催收期明细
    # 用于操作借贷记录菜单下面的子菜单
    def DealLog(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # 点击借贷记录
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # 点击待还款账单
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # 点击逾期待收款
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # 点击网站垫付款
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[4]/a").click()  # 点击收款信息
    # 用于操作投标信息菜单下面的子菜单
    def DealInfo(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # 点击投标信息
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # 点击所有投标
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # 点击手动投标
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # 点击自动投标
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # 点击成功的投标
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # 点击失败的投标
    # 用于操作债权转让菜单下面的子菜单
    def Transfer(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # 点击债权转让
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # 点击所有转让
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # 点击正在转让
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # 点击成功转让
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # 点击撤销转让
    # 用于操作留言式贷款申请菜单下面的子菜单
    def MsgDeal(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # 点击留言式贷款申请
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # 点击留言式贷款申请
        try:
           if listnum <= "0":
               print("error")
        except Exception:
            raise NameError("Not found %s listnum,You can enter '1'....." %listnum)
    # 用于操作留言管理菜单下面的子菜单
    def MsgMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # 点击留言管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd/a").click()  # 点击留言列表
    # 用于操作业务员查询菜单下面的子菜单
    def BusMan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[11]/dt").click()  # 点击业务员查询
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[1]/a").click()  # 点击推荐人查询
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[11]/dd[2]/a").click()  # 点击待审核查询
    # 用于操作普通会员菜单下面的子菜单
    def User(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击普通会员
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击普通用户
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击借款用户
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击理财用户
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击警告名单
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # 点击小树黑名单
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # 点击网贷黑名单
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # 点击待审核会员
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # 点击会员信息
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # 点击会员回收站
    # 用于操作企业会员菜单下面的子菜单
    def UesrCompany(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click() # 点击企业会员
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击企业会员
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击会员黑名单
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # 点击待审核会员
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # 点击会员信息
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # 点击会员回收站
    # 用于操作担保机构菜单下面的子菜单
    def DealAgency(self,liestnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击担保机构
        if liestnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # 点击担保机构
        elif liestnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # 点击担保机构回收站
    # 用于操作其他信息菜单下面的子菜单
    def CompanyManage(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击其他信息
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # 点击公司列表
        elif listnum =="2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # 点击工作信息
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # 点击银行卡列表
    # 用于操作红包管理菜单下面的子菜单
    def EcvMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # 点击 红包管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd/a")  # 点击红包类型
    # 用于操作相关配置菜单下面的子菜单
    def AboutConfig(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # 点击相关配置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # 点击会员字段列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # 点击信用等级列表
    # 用于操作站内消息菜单下面的子菜单
    def MsgSystem(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click()  # 点击站内消息
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # 点击消息群发
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # 点击消息列表
    # 用于操作VIP特权菜单下面的子菜单
    def VipPrivilege(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # 点击VIP特权
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # 点击VIP会员列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # 点击VIP等级
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[3]/a").click()  # 点击VIP配置列表
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[4]/a").click()  # 点击VIP配置回收站
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[5]/a").click()  # 点击VIP升级记录
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[6]/a").click() # 点击VIP降级记录
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[7]/a").click()  # 点击VIP购买日志
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[8]/a").click()  # 点击客服列表
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[9]/a").click()  # 点击客服回收站
    # 用于操作投资奖励菜单下面的子菜单
    def VipGift(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # 点击投资奖励
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[1]/a").click()  # 点击奖励发放列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[2]/a").click()  # 点击礼品管理
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd[3]/a").click()  # 点击非提现金管理
    # 用于操作节日福利菜单下面的子菜单
    def VipFestivals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[10]/dt").click()  # 点击节日福利
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[1]/a").click()  # 点击节日积分表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[2]/a").click()  # 点击福利发放列表
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[10]/dd[3]/a").click()  # 点击积分脱现
    # 用于操作续约申请菜单下面的子菜单
    def GenerationRepay(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击续约申请
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd/a").click()  # 点击续约申请子菜单
    # 用于操作授信额度申请菜单下面的子菜单
    def DealQuota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击授信额度申请
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click()  # 点击申请列表子菜单
    # 用于操作信用额度申请菜单下面的子菜单
    def Quota(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击信用额度申请
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # 点击申请列表
    # 用于操作举报管理菜单下面的子菜单
    def Reportguy(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击举报管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # 点击举报列表
    # 用于操作认证管理菜单下面的子菜单
    def CreditMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # 点击认证管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # 点击所有认证
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # 点击待审核的认证
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[3]/a").click()  # 点击通过的认证
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[4]/a").click()  # 点击失败的认证
    # 用于操作会员返利菜单下面的子菜单
    def Referrals(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # 点击会员返利
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]/a").click()  # 点击邀请返利列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]/a").click()  # 点击建立关联
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]/a").click()  # 点击推广人列表
    # 用于操作借出统计菜单下面的子菜单
    def StatisticsBorrow(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击借出统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击借出总统计
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击投资人数
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击投资金额
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击标种投资
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # 点击已回款
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # 点击待收款
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # 点击投资排名
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # 点击投资额比例
    # 用于操作借入统计菜单下面的子菜单
    def StatisticsLoan(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击借入统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击借入总统计
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击借款人数
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # 点击借款金额
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # 点击标种借款
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # 点击已还款
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # 点击待还款
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # 点击逾期还款
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # 点击逾期明细
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[9]/a").click()  # 点击逾期排行
        elif listnum == "10":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[10]/a").click()  # 点击逾期数据分析
        elif listnum == "11":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[11]/a").click()  # 点击逾期日统计比较
    # 用于操作债权统计菜单下面的子菜单
    def StatisticsClaims(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击债权统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd").click()  # 点击债权转让
    # 用于操作平台统计菜单下面的子菜单
    def WebsiteStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # 点击平台统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # 点击充值统计
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # 点击提现统计
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # 点击用户统计
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  #点击年龄段统计
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[5]/a").click()  # 点击网站垫付统计
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[6]/a").click()  # 点击网站费用统计
    # 用于操作校园行长菜单下面的子惨淡
    def Agentsstatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]").click()  # 点击校园行长统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click() # 点击校园校园行长列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # 点击校园行长统计
    # 用于操作管理员管理菜单下面的子菜单
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击管理员管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击部门列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击部门回站
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击部门成员
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击待分配会员
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # 点击待分配借款标
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # 点击所有借款标
    # 用于操作提成统计菜单下面的子菜单
    def Departments(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击提成统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击部门提成统计
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击成员提成统计
    # 用于操作我的会员菜单下面的子菜单
    def MyMembership(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击我的会员
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # 点击我的会员列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # 点击本月到期账单
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # 点击逾期账单
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # 点击还款中借款标
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[5]/a").click()  # 点击已完成借款标
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[6]/a").click()  # 点击已坏账借款标
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[7]/a").click()  # 点击借款会员列表
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[8]/a").click()  # 点击坏账会员列表
    # 用于操作城市合伙人菜单下面的子菜单
    def RegionPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击城市合伙人
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击城市合伙人列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击待缴保证金列表
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击已缴保证金记录
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击业务员列表
    # 用于操作贷款统计菜单下面的子菜单
    def LoanPartner(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击贷款统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd/a").click() # 点击贷款统计列表
    # 用于操作收益统计菜单下面的子菜单
    def IncomeStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击收益统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd/a").click()  # 点击收益统计列表
    # 用于操作逾期统计菜单下面的子菜单
    def ExpiredStatistics(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击逾期统计
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd/a").click()  # 点击逾期统计列表
    # 用于操作积分商城菜单下面的子菜单
    def Goods(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # 点击积分商城
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd[1]/a").click()  # 点击商品列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl/dd[2]/a").click()  # 点击商品分类
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl/dd[3]/a").click()  # 点击兑换商品
    # 用于操作文章管理菜单下面的子菜单
    def ArticleMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击文章管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击文章列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击文章回收站
    # 用于操作文章分类菜单下面的子菜单
    def ArticleCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击文章分类
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击分类列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击分类回收站
    # 用于操作前端设置菜单下面的子菜单
    def NavSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击前端设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # 点击导航菜单列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # 点击投票调查列表
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # 点击前端广告列表
    # 用于操作友情链接菜单下面的子菜单
    def LinkGroup(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击友情链接
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # 点击友情链接分组
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # 点击友情链接列表
    # 用于操作周年活动菜单下面的子菜单
    def Special(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl/dt").click()  # 点击周年活动
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl/dd").click()  # 点击女神评选
    # 用于系统设置菜单下面的子菜单
    def SysConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[1]/dt").click()  # 点击系统设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[1]/a").click()  # 点击系统配置
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[2]/a").click()  # 点击签到奖励配置
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[3]/a").click()  # 点击邀请返利配置
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[4]/a").click()  # 点击授权服务机构返佣设置
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[5]/a").click()  # 点击QQ客服配置
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[6]/a").click()  # 点击提现手续费
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[7]/a").click()  # 点击提现银行设置
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[8]/a").click()  # 点击认证类型设置
        elif listnum == "9":
            self.driver.find_element_by_xpath("/html/body/dl[1]/dd[9]/a").click()  # 点击用户平台注册验证设置
    # 用于操作贷款设置菜单下面的子菜单
    def DealCate(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[2]/dt").click()  # 点击贷款设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[1]/a").click()  # 点击贷款分类设置
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[2]/a").click()  # 点击分类回收站
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[3]/a").click()  # 点击贷款类型设置
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[4]/a").click()  # 点击类型回收站
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[5]/a").click()  # 点击贷款城市设置
        elif listnum == "6":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[6]/a").click()  # 点击城市回收站
        elif listnum == "7":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[7]/a").click()  # 点击合同范本设置
        elif listnum == "8":
            self.driver.find_element_by_xpath("/html/body/dl[2]/dd[8]/a").click()  # 点击范本回收站
    # 用于操作体验金管理菜单下面的子菜单
    def LearnMoney(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[3]/dt").click()  # 点击体验金管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[1]/a").click()  # 点击发放列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[2]/a").click()  # 点击投资记录
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[3]/a").click()  # 点击活动设置
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[3]/dd[4]/a").click()  # 点击理财产品列表
    # 用于操作接口设置菜单下面的子菜单
    def AIPSet(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[4]/dt").click()  # 点击接口设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[1]/a").click()  # 点击资金托管
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[2]/a").click()  # 点击支付接口设置
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[3]/a").click()  # 点击会员第三方登录
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[4]/dd[4]/a").click()  # 点击会员整合插件
    # 用于操作移动平设置菜单下面的子菜单
    def MobileConf(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[5]/dt").click()  # 点击移动平设置
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[1]/a").click()  # 点击手机端配置
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[5]/dd[2]/a").click()  # 点击手机端广告列表
    # 用于操作系统管理菜单下面的子菜单
    def SyeRole(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[6]/dt").click()  # 点击系统管理员
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[1]").click()  # 点击角色管理
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[2]").click()  # 点击角色回收站
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[6]/dd[3]").click()  # 点击管理员管
    # 用于操作短息邮件管理菜单下面的子菜单
    def MsgMailMent(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[7]/dt").click() # 点击短息邮件管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[1]/a").click()  # 点击消息模板管理
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[2]/a").click()  # 点击邮件服务器列表
        elif listnum == "3":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[3]/a").click()  # 点击邮件列表
        elif listnum == "4":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[4]/a").click()  # 点击短息借款列表
        elif listnum == "5":
            self.driver.find_element_by_xpath("/html/body/dl[7]/dd[5]/a").click()  # 点击短息列表
    # 用于操作队列管理菜单下面的子菜单
    def DealMsgList(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[8]/dt").click()  # 点击队列管理
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[1]/a").click()  # 点击业务队列列表
        elif listnum == "2":
            self.driver.find_element_by_xpath("/html/body/dl[8]/dd[2]/a").click()  # 点击推广队列列表
    # 用于操作数据库菜单下面的子菜单
    def Database(self,listnum):
        self.driver.find_element_by_xpath("/html/body/dl[9]/dt").click()  # 点击数据库
        if listnum == "1":
            self.driver.find_element_by_xpath("/html/body/dl[9]/dd/a").click()  # 点击SQL操作
    # 用于操作首单待审核列表审核动作
    def FirstPublish(self,action):
        if action == "shcz" or action == "审核操作" :
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[13]/a").click()  # 点击审核操作
        elif action == "rl" or action == "认领":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()  # 点击认领操作
        elif action == "shrz" or action == "审核日志":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # 点击审核日志
        elif action == "dkmc" or action == "贷款名称":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()  # 点击贷款名称
        elif action == "jkr" or action == "借款人":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # 点击借款人
    # 用于操作复审核列表审核动作
    def TruePublish(self,action):
        if action == "dkmc" or action == "贷款名称":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[3]/a").click()
        elif action == "jkr" or action == "借款人":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()
        elif action == "shcz" or action == "审核操作":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[14]/a").click()
        elif action == "shrz" or action == "审核日志":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()
    # 用于操作续借待审核列表审核动作
    def Publish(self,action):
        if action == "shcz" or action == "审核操作" :
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[15]/a").click()  # 点击审核操作
        elif action == "rl" or action == "认领":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[16]/a").click()  # 点击认领操作
        elif action == "shrz" or action == "审核日志":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[17]/a").click()  # 点击审核日志
        elif action == "dkmc" or action == "贷款名称":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[3]").click()  # 点击贷款名称
        elif action == "jkr" or action == "借款人":
            self.driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[3]/td[4]/a").click()  # 点击借款人
    # 用于操作审核详情页的审核动作
    def PublishPage(self,state,city,type,status,time,action):
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]").click()  # 点击选择中省份
        if state == "北京":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[2]").click()
        elif state == "安徽":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[3]").click()
        elif state == "福建":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[4]").click()
        elif state == "甘肃":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[5]").click()
        elif state == "广东":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[6]").click()
        elif state == "广西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[7]").click()
        elif state == "贵州":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[8]").click()
        elif state == "海南":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[9]").click()
        elif state == "河北":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[10]").click()
        elif state == "河南":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[11]").click()
        elif state == "黑龙江":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[12]").click()
        elif state == "湖北":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[13]").click()
        elif state == "湖南":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[14]").click()
        elif state == "吉林":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[15]").click()
        elif state == "江苏":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[16]").click()
        elif state == "江西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[17]").click()
        elif state == "辽宁":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[18]").click()
        elif state == "内蒙古":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[19]").click()
        elif state == "宁夏":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[20]").click()
        elif state == "青海":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[21]").click()
        elif state == "山东":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[22]").click()
        elif state == "山西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[23]").click()
        elif state == "陕西":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[24]").click()
        elif state == "上海":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[25]").click()
        elif state == "四川":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[26]").click()
        elif state == "天津":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[27]").click()
        elif state == "西藏":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[28]").click()
        elif state == "新疆":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[29]").click()
        elif state == "云南":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[30]").click()
        elif state == "浙江":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[31]").click()
        elif state == "重庆":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[32]").click()
        elif state == "香港":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[33]").click()
        elif state == "澳门":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[34]").click()
        elif state == "台湾":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[1]/option[35]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]").click()  # 点击选择中城市
        if state == "北京" and city == "北京"\
                or state == "安徽" and city == "安庆" \
                or state == "福建" and city == "福州" \
                or state == "甘肃" and city == "兰州" \
                or state == "广东" and city == "广州":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[2]").click()
        elif state == "安徽" and city == "蚌埠" \
                or state == "福建" and city == "龙岩"\
                or state == "甘肃" and city == "白银" \
                or state == "广东" and city == "深圳":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[3]").click()
        elif state == "安徽" and city == "巢湖" \
                or state == "福建" and city == "南平"\
                or state == "甘肃" and city == "定西" \
                or state == "广东" and city == "潮州":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[4]").click()
        elif state == "安徽" and city == "池州" \
                or state == "福建" and city == "宁德"\
                or state == "甘肃" and city == "甘南" \
                or state == "广东" and city == "东莞":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[5]").click()
        elif state == "安徽" and city == "滁州" \
                or state == "福建" and city == "莆田"\
                or tate == "甘肃" and city == "嘉峪关" \
                or state == "广东" and city == "佛山":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[6]").click()
        elif state == "安徽" and city == "阜阳" \
                or state == "福建" and city == "泉州"\
                or state == "甘肃" and city == "金昌" \
                or state == "广东" and city == "河源":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[7]").click()
        elif state == "安徽" and city == "淮北" \
                or state == "福建" and city == "三明"\
                or state == "甘肃" and city == "酒泉" \
                or state == "广东" and city == "惠州":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[8]").click()
        elif state == "安徽" and city == "淮南" \
                or state == "福建" and city == "厦门"\
                or state == "甘肃" and city == "临夏" \
                or state == "广东" and city == "江门":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[9]").click()
        elif state == "安徽" and city == "黄山" \
                or state == "福建" and city == "漳州"\
                or state == "甘肃" and city == "陇南" \
                or state == "广东" and city == "揭阳":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[10]").click()
        elif state == "安徽" and city == "六安" \
                or state == "甘肃" and city == "平凉" \
                or state == "广东" and city == "茂名":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[11]").click()
        elif state == "安徽" and city == "马鞍山" \
                or state == "甘肃" and city == "庆阳" \
                or state == "广东" and city == "梅州":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[12]").click()
        elif state == "安徽" and city == "宿州" \
                or state == "甘肃" and city == "天水" \
                or state == "广东" and city == "清远":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[13]").click()
        elif state == "安徽" and city == "铜陵" \
                or state == "甘肃" and city == "武威" \
                or state == "广东" and city == "汕头":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[14]").click()
        elif state == "安徽" and city == "芜湖" \
                or state == "甘肃" and city == "张掖" \
                or state == "广东" and city == "汕尾":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[15]").click()
        elif state == "安徽" and city == "宣城" \
                or state == "广东" and city == "韶关":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[16]").click()
        elif state == "安徽" and city == "亳州" \
                or state == "广东" and city == "阳江":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[17]").click()
        elif state == "安徽" and city == "合肥" \
                or state == "广东" and city == "云浮":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[18]").click()
        elif state == "广东" and city == "湛江":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[19]").click()
        elif state == "广东" and city == "肇庆":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[36]/td[2]/select[2]/option[20]").click()
        self.driver.find_element_by_xpath\
            ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select").click()  # 点击选中借款用途
        if type == "创业借款" or type == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[2]").click()
        elif type == "开店借款" or type == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[3]").click()
        elif type == "旅游借款" or type == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[4]").click()
        elif type == "买电脑借款" or type == "4":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[5]").click()
        elif type == "买手机借款" or type == "5":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[6]").click()
        elif type == "购物借款" or type == "6":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[7]").click()
        elif type == "考驾照借款" or type == "7":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[8]").click()
        elif type == "生活费借款" or type == "8":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[9]").click()
        elif type == "其他消费借款" or type == "9":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[1]/tbody/tr[37]/td[2]/select/option[10]").click()
        # 选择审状态
        if status == "审核失败" or status == "失败" or status == "3":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[1]/input").click()
        elif status == "审核成功" or status == "成功" or status == "1":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[2]").click()
            # 选择时间
            if time == "时间" :
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[2]").click()
                self.driver.find_element_by_xpath\
                    ("/html/body/div[7]/table/thead/tr[2]/td[3]/div").click()
            elif time == "清空":
                self.driver.find_element_by_xpath\
                    ("/html/body/div[2]/form/table[6]/tbody/tr[5]/td[2]/input[3]").click()
        elif status == "审核中" or status == "2":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/label[3]/input").click()
        # 审核提交
        if action == "提交" or action == "submit":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[7]").click()
        elif action == "重置" or action == "reset":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[7]/td[2]/input[8]").click()
    # 用于操作复审详情页
    def TruePublish(self,status,action):
        if status == "pass" or status == "审核通过":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[1]/input").click()
        elif status == "return" or status == "退回初审":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[3]/td[2]/label[2]/input").click()
        if action == "submit" or action == "提交":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[7]").click()
        elif action == "reset" or action == "重置":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/form/table[6]/tbody/tr[6]/td[2]/input[8]").click()
    # 用于操作借款端首页动作执行
    def DFristPageAction(self,action,status):
        if action == "fristpage" or action == "首页" or action == "fp":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[5]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
        elif action == "borrow" or action == "借点钱" or action == "br":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[4]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
        elif action == "refund" or action == "还款呐" or action == "rf":
            if status == "0":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[3]/a").click()
            elif status == "1":
                self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "login" or action == "登录" or action == "lg":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/a").click()
        elif action == "register" or action == "注册" or action == "rs":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/span/a/span").click()
        elif action == "goinvest" or action == "切换理财版" or action == "gi":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[1]/a").click()
        elif action == "needmoney" or action == "我要用钱" or action == "nd":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/a/span").click()
        elif action == "easyrepay" or action == "快捷还款" or action == "er":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/a/span").click()
        elif action == "downloadiphone" or action == "iphone":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[4]/a/img").click()
        elif action == "downloadandroid" or  action == "android":
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/a/img").click()
    # 用于操作登录动作（包含借款端弹窗登录、页面跳转登录、理财端弹出登录、页面跳转登录）
    def FristWinLogin(self,user,pwd,method):
        self.driver.find_element_by_id("login-email-address").send_keys(user)
        self.driver.find_element_by_id("login-password").send_keys(pwd)
        if method == "0":
            self.driver.find_element_by_id("ajax-login-submit").click()
        elif method == "1":
            self.driver.find_element_by_id("user-login-submit").click()
    # 用于操作借款端用户菜单动作
    def UserMenu(self,action):
        menu = self.driver.find_element_by_xpath\
            ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[1]")
        ActionChains.move_to_element(menu).perform()
        if action == "mypage" or action == "我的主页":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[2]/a")\
                .click()
        elif action == "borrow" or action == "我要借款":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[3]/a")\
                .click()
        elif action == "account" or action == "个人设置":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[4]/a")\
                .click()
        elif action == "loginout" or action == "退出登录":
            self.driver.find_element_by_xpath\
                ("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]/div[2]/ul/li[5]/a")\
                .click()
    # 用于操作借款类型选择
    def Borrow(self,type):
        if type == "25":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[1]/div[3]/a").click()
            time.sleep(2)
        elif type == "19":
            self.driver.find_element_by_xpath\
                ("/html/body/div[2]/div[2]/div/div/ul/li[2]/div[3]/a").click()
            time.sleep(2)
    # 用于操作贷款详情页动作
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
        if status == "save" or status == "保存":
            self.driver.find_element_by_id("saveBtn").click()
        elif status == "publish" or status == "提交审核":
            self.driver.find_element_by_id("publishBnt").click()
            self.driver.switch_to_alert().accept()
        elif status == "preview" or status == "预览":
            self.driver.find_element_by_id("previewBtn").click()

