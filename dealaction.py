# coding: gb2312
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sysxsaction import SysXSAdmin
from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os


class element():
    __name = ""
    def __init__(self,name):
        self.__name = name
    def TestCase(self):
        implement = SysXSAdmin()
        implement.UrlOpen(url="http://test.xiaoshushidai.com")
        implement.DFristPageAction(action="���Ǯ",status="0")
        implement.FristWinLogin(user="testjoin",pwd="a12345678",method="1")
        time.sleep(2)
        implement.Borrow(type="25")
        implement.BorrowStepone(money="5000",repaytime="9",QQ="1",describe="testtesttesttesttesttest",status="�ύ���",type="25")
        time.sleep(10)
        implement.Quitbrow()

# TestCase()


if __name__ == '__init__':
    testunit = unittest.TestSuite()   #����һ����Ԫ��������
    testunit.addTest(element("TestCase"))  #�������������뵽����������
    # testunit.addTest("TestCase")
    #testunit.addTest(element("test_search"))

    filename="C:/Users/Administrator/PycharmProjects/testxiaoshu/Test.html"  #�����������·����֧�����·����
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #ʹ��HTMLTestRunner���ò������������·����������⡢����
    runner.run(testunit) #�Զ����в���
