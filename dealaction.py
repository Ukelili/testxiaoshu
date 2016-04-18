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
        self.DFristPageAction(action="???归??",status="0")
        self.FristWinLogin(user="testjoin",pwd="a12345678",method="1")
        time.sleep(2)
        self.Borrow(type="25")
        self.BorrowStepone(money="5000",
                           repaytime="9",
                           QQ="1",
                           describe="testtesttesttesttesttest",
                           status="??浜ゅ?℃??"
                           ,type="25")
        # time.sleep(10)
        self.Quitbrow()
    def tearDown(self):
        self.Quitbrow()
        # self.assertEqual([],self.v)

if __name__ == "__main__":
    # 瀹?涔?涓?涓?????娴?璇?瀹瑰??
    testunit = unittest.TestSuite()
    testunit.addTest(XiaoShu("setUp"))  #灏?娴?璇??ㄤ????ュ?版?璇?瀹瑰?ㄤ腑
    # ?????㈡?堕??
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    # 瀹?涔?涓??ュ??瀛??捐矾寰?锛??????稿?硅矾寰???
    filename = "./TestReport/"+now+'_TestReport.html'
    fp = file(filename,'wb')
    # 浣跨??HTMLTestRunner??缃????帮?杈??烘?ュ??璺?寰????ュ????棰?????杩?
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'??娆剧?宠?锋?璇??ュ??',description=u'?ㄤ??ц????碉?')
    # ???ㄨ?琛?娴?璇?
    runner.run(testunit)
