# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.feifan_card_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage: 飞凡卡
'''


class FeiFanCardPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FeiFanCardPageConfigs.resource_id_tv_bill_tv,
                                                      seconds=10)

    '''
        usage : 点击账单
    '''

    def clickOnBill(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=FeiFanCardPageConfigs.resource_id_tv_bill_tv)

    '''
        usage : 点击零花钱
    '''

    def clickOnPocketMoney(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=FeiFanCardPageConfigs.resource_id_tv_pocket_money_tv)

    '''
        usage : 点击积分
    '''

    def clickOnIntegral(self):
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=FeiFanCardPageConfigs.text_integral);


if __name__ == '__main__':
    pass;
