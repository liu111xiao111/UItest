# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xiaoxizhongxin_page_configs import XiaoXiZhongXinPageConfigs as XXZXPC


class XiaoXiZhongXinPage(SuperPage):
    '''
    作者 乔佳溪
    消息中心
    '''
    def __init__(self, testcase, driver, logger):
        super(XiaoXiZhongXinPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到消息中心页,检查登录标题
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  XXZXPC.text_title,
                                  XXZXPC.assert_timeout)

    def clickOnSystem(self):
        '''
        usage: 点击系统消息
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XXZXPC.text_system,
                                       XXZXPC.assert_timeout)

    def clickOnNotice(self):
        '''
        usage: 点击通知公告
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XXZXPC.text_notice,
                                       XXZXPC.assert_timeout)

    def validSystem(self):
        '''
        usage : 验证系统消息
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  XXZXPC.text_title,
                                  XXZXPC.assert_timeout)

    def validNotice(self):
        '''
        usage : 验证通知公告
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  XXZXPC.text_title,
                                  XXZXPC.assert_timeout)
