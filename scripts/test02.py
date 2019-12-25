# 导包
import appium
# 创建驱动对象
import time

import pytest
from appium import webdriver
class Test:
    def setup_class(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "5.1",
            "deviceName": "模拟器",
            "appPackage": "com.vcooline.aike",
            "appActivity": ".umanager.LoginActivity"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)


    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize(['a','b'],[(123,123456),(456,123456),(789,123456)])
    def test01(self,a,b):
        self.driver.find_element_by_id('com.vcooline.aike:id/etxt_username').send_keys(a)
        self.driver.find_element_by_id('com.vcooline.aike:id/etxt_pwd').send_keys(b)
        self.driver.find_element_by_id('com.vcooline.aike:id/btn_login').click()