# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shezhi_page_configs import SheZhiPageConfigs as SZPC
from pages.logger import logger


class SheZhiPage(SuperPage):
    '''
    作者 乔佳溪
    设置页
    '''
    def __init__(self, testcase, driver, logger):
        super(SheZhiPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到设置页,检查标题
        '''
        logger.info("Check 设置页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SZPC.text_title,
                                  SZPC.verify_timeout)
        logger.info("Check 设置页面 end")

    def clickOnLogout(self):
        '''
        usage: 点击退出登录
        '''
        logger.info("Click 退出登录 begin")
        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           SZPC.text_logout)

        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SZPC.text_logout,
                                 SZPC.verify_timeout)
        logger.info("Click 退出登录 end")
