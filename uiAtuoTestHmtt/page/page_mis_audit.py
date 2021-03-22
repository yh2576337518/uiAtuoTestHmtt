from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    # 文章id
    article_id = None

    # 点击 信息管理
    def page_click_info_manage(self):
        # 暂停时间
        sleep(2)
        # 点击信息管理
        self.base_click(page.mis_info_manage)

    # 点击 内容审核
    def page_click_content_audit(self):
        # 暂停时间
        sleep(2)
        # 点击内容审核
        self.base_click(page.mis_content_audit)

    # 输入 文章标题
    def page_click_title(self, title):
        self.base_input(page.mis_title, title)

    # 输入 文章所属频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 选择 状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text=placeholder_text, click_text=click_text)

    # 点击 查询按钮
    def page_click_find(self):
        # 点击查询按钮
        self.base_click(page.mis_find)
        # 暂停时间
        sleep(2)

    # 获取 文章的id
    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    # 点击 通过按钮
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 点击 确认按钮
    def page_click_confirm_pass(self):
        # 暂停时间
        sleep(1)
        # 点击确认
        self.base_click(page.mis_confirm_pass)

    # 组合发布文章业务方法
    def page_mis_audit(self, title, channel):
        log.info("正在调用审核文章业务方法，title：{},channel：{}".format(title, channel))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_click_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取的文章id为：", self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    # 组装断言业务操作方法
    def page_assert_audit(self):
        log.info("正在调用断言业务操作方法")
        # 暂停3秒
        sleep(3)
        # 修改状态->审核通过
        self.page_click_status(click_text="审核通过")
        # 点击查询操作
        self.page_click_find()
        # 判断当前页面是否存在指定结果 并 返回结果
        return self.web_base_is_exist(self.article_id)
