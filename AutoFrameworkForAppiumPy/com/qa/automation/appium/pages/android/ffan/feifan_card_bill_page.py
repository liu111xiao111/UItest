#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from time import sleep
import unittest

from appium import webdriver

from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.common.super_page import *
from com.qa.automation.appium.pages.android.ffan.feifan_card_bill_page_configs import *


# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage: 飞凡卡
'''


class FeiFanCardBillPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(FeiFanCardBillPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=FeiFanCardBillPageConfigs.resource_id_tv_bill_list_tv,
                                                      seconds=10)

    def validSubFilterByText(self, text=u"全部"):
        '''
        usage: verify whether the filter is correct.
        '''

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger, text, FeiFanCardBillPageConfigs.click_on_button_timeout)

    def clickOnFilter(self):
        '''
        usage: click on the filter button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, FeiFanCardBillPageConfigs.resource_id_filter_button, FeiFanCardBillPageConfigs.click_on_button_timeout);

    def clickOnSubFilterByText(self, text=u"全部"):
        '''
        usage: click on the sub-filter button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, text, FeiFanCardBillPageConfigs.click_on_button_timeout);

if __name__ == '__main__':
    pass;
