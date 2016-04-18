# coding: gb2312
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sysxsaction import SysXSAdmin
import time,os


def AutoDeal():
        implement = SysXSAdmin()
        implement.UrlOpen(url="http://test.xiaoshushidai.com/xs.php")
        implement.SysLogin(user='admin',pwd='1234QWER1qaz',verify='2348')
        #implement.Quitbrow()
#class AutoPublishDeal(object):


AutoDeal()