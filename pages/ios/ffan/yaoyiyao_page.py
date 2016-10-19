# -*- coding: utf-8 -*-

import logging
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.yaoyiyaop_page_configs import YaoyiyaoPageConfigs


class YaoyiyaoPage(SuperPage):
    '''
        作者 刘涛
        摇一摇页面

    '''

    def __init__(self, testcase, driver, logger):
        super(YaoyiyaoPage, self).__init__(testcase, driver, logger)



    def validSelf(self):
        '''
        usage: 进入到应用首页,检查ffan logo
        '''

        API().validElementByXpath(self.driver, self.logger,
                                            YaoyiyaoPageConfigs.xpath_title, YaoyiyaoPageConfigs.assert_view_timeout)