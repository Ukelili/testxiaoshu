# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,os

browser = webdriver.Firefox() # Get local session of chrome
browser.maximize_window()
browser.get("http://test.xiaoshushidai.com") # Load page
elem = browser.find_element_by_id("fast_login").click()
username = browser.find_element_by_id("login-email-address").send_keys("testjoin")
user_pwd = browser.find_element_by_id("login-password").send_keys("a12345678")
login_sub = browser.find_element_by_xpath("//*[@id='ajax-login-submit']").click()
meu = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]")
ActionChains(browser).move_to_element(meu).perform()
browser.get_screenshot_as_file("E:\\log\\logtest.bmp")
click_mypage = browser.find_element_by_link_text("我的主页").click()
browser.get_screenshot_as_file("E:\\log\\jiandao.bmp")
my_jk = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[2]/a").click()
browser.get_screenshot_as_file("E:\\log\\borrowlist.bmp")
borrow = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/ul/li[1]/div[3]/a/img").click()
input_JKmoney = browser.find_element_by_xpath("/html/body/div[3]/div[4]/div/form/div[1]/div[6]/span/input").send_keys("5000")
downlist = browser.find_element_by_xpath("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dt/i").click()
borrowD = browser.find_element_by_xpath("/html/body/div[3]/div[4]/div/form/div[1]/div[9]/div/dl/dd/a[4]").click()
paly = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div[6]/a[1]").click()
input_moeny = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/form/div/div[2]/div[1]/div/div[2]/input").send_keys("1000")
sub_moeny = browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/form/div/div[2]/div[1]/div/div[2]/span[2]/div").click()
browser.get_screenshot_as_file("E:\\log\\moeny.bmp")
paly_pwd = browser.find_element_by_xpath("/html/body/div[2]/div[4]/form/div[6]/div[1]/div[12]/div[1]/input").send_keys("a12345678")
sumb = browser.find_element_by_xpath("/html/body/div[2]/div[4]/form/div[6]/div[1]/div[12]/div[2]").click()
browser.get_screenshot_as_file("E:\\log\\error.bmp")
time.sleep(3)
browser.close()

'''
meu = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/ul/li[2]")
login_out = browser.find_element_by_link_text("退出登录").click()
'''
'''
click_jiadao = browser.find_element_by_class_name("btn_red bdr3").click()
jiandao = browser.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td[2]/div[3]/input[1]").click()
listdown = browser.find_element_by_xpath("/html/body/div[2]/div[4]/form/div[6]/div[1]/div[3]/div[1]/div/div[5]").click()
click_sumb_syserro = browser.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td[2]/div[3]/input[1]").click()
'''
'''
browser = webdriver.Firefox() # Get local session of firefox self,url,clickID,sendKvalue
browser.maximize_window()
browser.get("http://test.xiaoshushidai.com") # Load page
elem = browser.find_element_by_id("fast_login") # click this loign button
elem.click()# Click event
user_input = browser.find_element_by_id("login-email-address") # Find the element user name input box di
user_input.send_keys("hackred123") # Input user name value
password_input = browser.find_element_by_id("login-password")  # Find the element password input box di
password_input.send_keys("a123456") # Input password value
login_click = browser.find_element_by_id("ajax-login-submit")# loign submit
login_click.click() # login click
meu = browser.find_element_by_xpath("//li[@class=pr under_line]").click()
login_out = browser.find_element_by_xpath("//a[@href='user-loginout']")
login_out.click()
'''
'''
meu = browser.find_element_by_tag_name("span")
login_out = browser.find_element_by_xpath("//div[@class='user_menu']/ul[1]/li[5]/a[1]")
login_out = browser.find_element_by_xpath("//div[@class='under_line_img']/a[@href='user-loginout']")
login_out.click()
time.sleep(3)
browser.close() # close Firefox browser
'''
'''
class Test_xiaoshu():
    def login_test(self):
        browser = webdriver.Firefox() # Get local session of firefox self,url,clickID,sendKvalue
        browser.get("http://test.xiaoshushidai.com") # Load page
        elem = browser.find_element_by_id("fast_login") # click this loign button
        elem.click()# Click event
        user_input = browser.find_element_by_id("login-email-address") # Find the element user name input box di
        user_input.send_keys("hackred123") # Input user name value
        password_input = browser.find_element_by_id("login-password")  # Find the element password input box di
        password_input.send_keys("a123465") # Input password value
        login_click = browser.find_element_by_id("ajax-login-submit") # loign submit
        login_click.click() # login click
        browser.close() # close Firefox browser

Test_xiaoshu.login_test()
'''
'''
assert "Yahoo!" in browser.title
elem = browser.find_element_by_name("p") # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
'''