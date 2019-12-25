from appium import webdriver


def get_android_driver(bm,qdm):
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": bm,
        "appActivity": qdm
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=capabilities)