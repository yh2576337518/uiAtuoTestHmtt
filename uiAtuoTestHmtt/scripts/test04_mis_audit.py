import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisAudit:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 调用登录成功依赖方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 获取PageMisAudit对象
        self.audit = self.page_in.page_get_PageMisAudit()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 审核文章业务测试方法
    def test_mis_audit(self, title=page.title, channel=page.channel):
        # 调用审核文章业务测试方法
        self.audit.page_mis_audit(title, channel)
        # 断言
        try:
            assert self.audit.page_assert_audit()
        except Exception as e:
            # 日志
            log.error("断言出错，错误信息：{}".format(e))
            # 截图
            self.audit.base_get_img()
            # 抛异常
            raise
