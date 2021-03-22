import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取统一入口对象
        self.page_in = PageIn(driver)
        # 调用登录方法
        self.page_in.page_get_PageAppLogin().page_is_login_success()
        # 获取发布文章页面对象
        self.article = self.page_in.page_get_PageAppArticle()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quite_app_driver()

    # 发布文章测试方法
    @pytest.mark.parametrize("click_text,title", read_yaml("app_article.yaml"))
    def test_app_article(self, click_text, title):
        try:
            # 调用发布文章测试方法
            self.article.page_app_article(click_text, title)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛出异常
            raise
