# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_order_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyOrderPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyOrderPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "我的订单" page， according to textview in "我的订单", check "我的订单" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=MyFfanMyOrderPageConfigs.resource_id_tv_my_order_tv)

    def clickOnOrderAll(self):
        '''
        usage : Click "全部" in my order page， and load "全部" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyOrderPageConfigs.text_order_all)

    def clickOnOrderNoPay(self):
        '''
        usage : Click "待付款" in my order page， and load "已使用" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyOrderPageConfigs.text_order_no_pay)

    def clickOnOrderPaid(self):
        '''
        usage : Click "已付款" in my order page， and load "已付款" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyOrderPageConfigs.text_order_paid)

    def validSelfNoPay(self):
        '''
        usage : Load "待付款" correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyOrderPageConfigs.text_order_no_pay, seconds=10);

    def validSelfPaid(self):
        '''
        usage : Load "已付款" correctly.
        '''

        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyOrderPageConfigs.text_order_paid, seconds=10);


if __name__ == '__main__':
    pass;
