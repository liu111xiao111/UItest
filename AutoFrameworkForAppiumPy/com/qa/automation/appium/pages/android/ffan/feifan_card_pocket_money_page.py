# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.feifan_card_pocket_money_page_configs import FeiFanCardPocketMoneyConfigs

class FeiFanCardPocketMoneyPage(SuperPage):
    '''
    作者 刘涛
    首页=>飞凡卡=>我的零花钱
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPocketMoneyPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 验证我的零花钱页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        FeiFanCardPocketMoneyConfigs.resource_id_tv_pocket_money_tv,
                                        10)
