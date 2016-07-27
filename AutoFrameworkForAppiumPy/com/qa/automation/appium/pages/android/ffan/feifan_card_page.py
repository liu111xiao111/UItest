# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.feifan_card_page_configs import FeiFanCardPageConfigs
from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

FCPC = FeiFanCardPageConfigs()

class FeiFanCardPage(SuperPage):
    '''
    作者：刘涛
    首页=>飞凡卡
    '''
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查飞凡卡界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_bill_tv,
                                        FCPC.verify_view_timeout)

    def clickOnOpenCard(self):
        '''
        usage: 点击市民/公交卡
        '''
        API().clickElementByText(self.testcase,
                                self.driver,
                                self.logger,
                                FCPC.text_tv_open_tv,
                                FCPC.verify_click_timeout)

    def clickOnBill(self):
        '''
        usage : 点击账单
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_bill_tv,
                                       FCPC.verify_click_timeout)

    def clickOnPocketMoney(self):
        '''
        usage : 点击零花钱
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_pocket_money_tv,
                                       FCPC.verify_click_timeout)

    def clickOnIntegral(self):
        '''
        usage : 点击积分
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCPC.text_integral,
                                 FCPC.verify_click_timeout)
