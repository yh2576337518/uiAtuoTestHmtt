from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    # 声明driver变量
    __web_driver = None
    __app_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作 重点
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver为空
        if cls.__app_driver is None:
            # 设置启动参数
            desired_caps = {}  # 定义启动设备需要的参数
            desired_caps['platformName'] = 'Android'  # 设备的操作系统
            desired_caps['platformVersion'] = '5'  # 设备的系统版本号
            desired_caps['deviceName'] = 'dd639018'  # 设备名称，使用手机类型或者模拟器类型
            desired_caps['appPackage'] = page.appPackage  # 要测试的应用的包名
            desired_caps['appActivity'] = page.appActivity  # 启动的activity参数
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.__app_driver

    # 退出APP应用driver
    @classmethod
    def quite_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quite()
            cls.__app_driver = None
