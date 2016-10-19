# -*- coding: utf-8 -*-

import logging
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.xianchangyao_page_configs import XianchangyaoPageConfigs


class XianchangyaoPage(SuperPage):


    '''
       作者 刘涛
       现场摇页面
    '''


    def __init__(self, testcase, driver, logger):
        super(XianchangyaoPage, self).__init__(testcase, driver, logger)


    def validSelf(self):
        '''
        usage: 进入到应用首页,检查ffan logo
        '''

        API().validElementByXpath(self.driver, self.logger,
                                  XianchangyaoPageConfigs.xpath_title, XianchangyaoPageConfigs.assert_view_timeout)


    def clickOnShakingImage(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  XianchangyaoPageConfigs.xpath_shaking_image,
                                  XianchangyaoPageConfigs.click_on_button_timeout)

    def validShakingResult(self):
        '''
        usage:验证现场摇结果
        '''
        API().validElementByXpath(self.driver, self.logger,
                                  XianchangyaoPageConfigs.xpath_shaking_result, XianchangyaoPageConfigs.assert_view_timeout)