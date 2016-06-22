# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_ticket_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyTicketPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanMyTicketPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "我的票券" page， according to textview in "我的票券", check "我的票券" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=MyFfanMyTicketPageConfigs.resource_id_tv_my_ticket_tv)

    def clickOnTicketUnused(self):
        '''
        usage : Click "未使用" in my ticket page， and load "未使用" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_unused)

    def clickOnTicketUsed(self):
        '''
        usage : Click "已使用" in my ticket page， and load "已使用" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_used)

    def clickOnTicketOutOfDate(self):
        '''
        usage : Click "已过期" in my ticket page， and load "已过期" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_out_of_date)

    def clickOnReturnRefund(self):
        '''
        usage : Click "退货退款" in my ticket page， and load "退货退款" tab correctly. 
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanMyTicketPageConfigs.text_ticket_return_refund)

    def validSelfUsed(self):
        '''
        usage : Load "已使用" tab correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_used, seconds=10);

    def validSelfOutOfDate(self):
        '''
        usage : Load "已过期" tab correctly.
        '''

        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_out_of_date, seconds=10);

    def validSelfReturnRefund(self):
        '''
        usage : Load "退货退款" tab correctly.
        '''
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=MyFfanMyTicketPageConfigs.text_ticket_return_refund, seconds=10);


if __name__ == '__main__':
    pass;
