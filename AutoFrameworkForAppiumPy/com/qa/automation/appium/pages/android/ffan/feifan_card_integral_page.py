# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.feifan_card_integral_page_configs import FeiFanCardIntegralPageConfigs

class FeiFanCardIntegralPage(SuperPage):
    '''
    作者 刘涛
    首页＝>飞凡卡=>积分
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardIntegralPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证积分主页
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FeiFanCardIntegralPageConfigs.text_tv_integral_tv,
                                  10)
