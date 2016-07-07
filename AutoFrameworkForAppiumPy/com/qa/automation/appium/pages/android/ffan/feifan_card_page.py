# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.pages.android.ffan.feifan_card_page_configs import FeiFanCardPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

FCPC = FeiFanCardPageConfigs()

'''
    usage: 飞凡卡
'''
class FeiFanCardPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPage, self).__init__(testcase,
                                             driver,
                                             logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              FCPC.resource_id_tv_bill_tv,
                                              FCPC.verify_view_timeout)

    '''
        usage: 点击开卡
    '''
    def clickOnOpenCard(self):
        API().click_view_by_text_android(self.testcase,
                                         self.driver,
                                         self.logger,
                                         FCPC.text_tv_open_tv,
                                         FCPC.verify_click_timeout)

    '''
        usage : 点击账单
    '''
    def clickOnBill(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_bill_tv,
                                       FCPC.verify_click_timeout)

    '''
        usage : 点击零花钱
    '''
    def clickOnPocketMoney(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_pocket_money_tv)

    '''
        usage : 点击积分
    '''
    def clickOnIntegral(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=FeiFanCardPageConfigs.text_integral);


if __name__ == '__main__':
    pass;