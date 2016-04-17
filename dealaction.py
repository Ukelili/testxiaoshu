# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sysxsaction import SysXSAdmin
import HTMLTestRunner
import time,os,unittest,re,io

# TestCase()
class XiaoShu(unittest.TestCase):
    def setUp(self):
        self = SysXSAdmin()
        self.UrlOpen(url="http://test.xiaoshushidai.com")
        self.DFristPageAction(action="借点钱",status="0")
        self.FristWinLogin(user="testjoin",pwd="a12345678",method="1")
        time.sleep(2)
        self.Borrow(type="25")
        self.BorrowStepone(money="5000",repaytime="9",QQ="1",describe="testtesttesttesttesttest",status="提交审核",type="25")
        time.sleep(10)

    def tearDown(self):
        self.Quitbrow()
        # self.assertEqual([],self.v)


if __name__ == "__main__":
    testunit = unittest.TestSuite()   #定义一个单元测试容器
    testunit.addTest(XiaoShu("setUp"))  #将测试用例加入到测试容器中
    filename = './PycharmProjects/test.html' #定义个报告存放路径，支持相对路径。

    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'借款申请测试报告',description=u'用例执行情况：')  #使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit) #自动进行测试
