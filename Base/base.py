from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver


    # 定义单个元素方法
    def find_ele(self,loc):
        # return self.driver.find_element(loc[0],loc[1])
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(loc[0],loc[1]))



    # 定义多个元素的方法
    def find_eles(self,loc):
        # return self.driver.find_elements(loc[0],loc[1])
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_elements(loc[0], loc[1]))

    # 定义单个元素点击的方法
    def click_ele(self,loc):
        self.find_ele(loc).click()



    # 定义输入单个元素的方法
    def send_ele(self,loc,text):
        self.find_ele(loc).clear()
        self.find_ele(loc).send_keys(text)


    # 定义输入多个元素的方法
    def send_eles(self,loc,count,text):
        self.find_eles(loc)[count].clear()
        self.find_eles(loc)[count].send_keys(text)
