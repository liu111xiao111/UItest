# -*- coding: utf-8 -*-

from __init__ import *

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.feifan_card_pocket_money_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

'''
    usage: 飞凡卡　我的零花钱
'''


class FeiFanCardPocketMoneyPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPocketMoneyPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FeiFanCardPocketMoneyConfigs.resource_id_tv_pocket_money_tv,
                                                      seconds=10)


if __name__ == '__main__':
    pass;