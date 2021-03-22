from time import sleep

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):
    # 查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        try:
            # 调用查找方法
            self.base_find(loc, timeout=3)
            log.info("在app页面中找到指定元素：{}元素！".format(loc))
            # 输出信息
            print("找到：{}元素啦！".format(loc))
            # 返回true
            return True
        except:
            log.error("没有在app页面内找到指定元素：{}！".format(loc))
            # 输出信息
            print("未找到元素：{}".format(loc))
            # 返回False
            return False

    # 从右向左滑动屏幕
    def app_base_right_wipe_left(self, loc_area, click_text):
        log.info("正在调用 从右向左滑方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的位置 y坐标点
        y = el.location.get("y")
        # 获取区域元素的宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算 start_x、start_y,end_x、end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        # 组合频道元素配置信息
        """
            找到指定元素区域内的元素
            第一种：//*[@class='父类']//*[contains(@text,'{}')]
            第二种：//父类/*[contains(@text,'{}')]
        """
        # loc = By.XPATH, "//*[@class='父类']//*[contains(@text,'{}')]".format(click_text)
        loc = By.XPATH, "//父类/*[contains(@text,'{}')]".format(click_text)
        # 循环操作
        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 捕获异常
            try:
                sleep(2)
                # 查找元素
                ele = self.base_find(loc, timeout=3)
                # 输出提示信息
                print("找到：{}元啦！".format(ele))
                sleep(2)
                # 点击元素
                ele.click()
                # 跳出循环
                break
            except:
                # 输出提示信息
                print("未找到：{}元素！".format(loc))
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException

    # 从下向上滑动屏幕
    def app_base_down_wipe_up(self, loc_area, click_text):
        log.info("正在调用 从下向上滑方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算 start_x、start_y,end_x、end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        # 组合频道元素配置信息
        loc = By.XPATH, "//*[@bounds='']/*[contains(@text,'{}')]".format(click_text)
        # 循环操作
        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 捕获异常
            try:
                # 查找元素
                ele = self.base_find(loc, timeout=3)
                # 输出提示信息
                print("找到：{}元啦！".format(ele))
                # 点击元素
                ele.click()
                # 跳出循环
                break
            except:
                # 输出提示信息
                print("未找到：{}元素！".format(loc))
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 输出提示信息
                print("滑到最后一屏幕，未找到元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException
