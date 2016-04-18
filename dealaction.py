# coding: gb2312
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
        self.DFristPageAction(action="???��??",status="0")
        self.FristWinLogin(user="testjoin",pwd="a12345678",method="1")
        time.sleep(2)
        self.Borrow(type="25")
        self.BorrowStepone(money="5000",
                           repaytime="9",
                           QQ="1",
                           describe="testtesttesttesttesttest",
                           status="??交�?��??"
                           ,type="25")
        # time.sleep(10)
        self.Quitbrow()
    def tearDown(self):
        self.Quitbrow()
        # self.assertEqual([],self.v)

if __name__ == "__main__":
    # �?�?�?�?????�?�?容�??
    testunit = unittest.TestSuite()
    testunit.addTest(XiaoShu("setUp"))  #�?�?�??��????��?��?�?容�?�中
    # ?????��?��??
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # �?�?�??��??�??�路�?�??????��?�路�???
    filename = "./TestReport/"+now+'_TestReport.html'
    fp = file(filename,'wb')
    # 使�??HTMLTestRunner??�????��?�??��?��??�?�????��????�?????�?
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'??款�?��?��?�??��??',description=u'?��??��????��?')
    # ???��?�?�?�?
    runner.run(testunit)
