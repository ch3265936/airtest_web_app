__author__ = "chihai"

from airtest.core.api import *

from utils import  *
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
def delete(key):
    driver.find_element_by_xpath("//input[@type='text']").send_keys(key)
    sleep(3)
    driver.find_element_by_xpath("//*[@id=\"contentlist\"]/li/span").click()
    sleep(10)
    Logging("获取数据")
    driver.find_element_by_name("getdata").click()
    sleep(10)
    Logging("清空数据")
    driver.find_element_by_name("cleardata").click()
    sleep(10)
driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://tech-support.upltv.com:82/index")

driver.find_element_by_xpath("//a[@href='/auth/login']").click()

driver.find_element_by_xpath("//input[@autocomplete='on']").send_keys('Colin.chi@avid.ly')
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys('Temp2019')
driver.find_element_by_xpath("//input[@value='登录']").click()
sleep(5)
driver.find_element_by_xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li/a/span").click()
driver.find_element_by_xpath("//a[@href='/report/analysis']").click()

#DHM
delete('600164')
#TBC
delete('600141')










