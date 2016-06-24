# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.my_ffan_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#   进入应用的首页,是进入其他页面的入口
class MyFfanPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MyFfanPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入到应用首页,检查ffan logo
    '''

    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver,
                                          logger=self.logger,
                                          text=MyFfanPageConfigs.text_my_ffan);

    def clickOnLogin(self):
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=MyFfanPageConfigs.resource_id_tv_login_tv);

    def validLoginStatus(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, logger=self.logger, driver=self.driver,
                                                      resource_id=MyFfanPageConfigs.resource_id_txt_user_nick_name_tv,
                                                      seconds=90)

    def clickOnSettings(self):
        # API().scroll_to_text(driver=self.driver, logger=self.logger, text=MyFfanPageConfigs.text_settins)
        super().scrollAsScreenPercent(start_x_percent= 0.5,start_y_percent=0.8,end_x_percent=0.5,end_y_percent=0.2,duration=800);
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanPageConfigs.text_settins)

    def clickOnMyQueue(self):
        '''
        usage : Load "我的排队" page， according to textview in "我的排队", check "我的排队" page whether load correctly.
        '''
        API().scroll_to_text(driver=self.driver, logger=self.logger, text=MyFfanPageConfigs.text_my_queue)
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanPageConfigs.text_my_queue)

    def clickOnMyTicket(self):
        '''
        usage : Load "我的票券" page， according to textview in "我的票券", check "我的票券" page whether load correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanPageConfigs.text_my_ticket)

    def clickOnMyOrder(self):
        '''
        usage : Load "我的订单" page， according to textview in "我的订单", check "我的订单" page whether load correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanPageConfigs.text_my_order)

    def clickOnMyLike(self):
        '''
        usage : Load "我的喜欢" page， according to textview in "我的喜欢", check "我的喜欢" page whether load correctly.
        '''
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=MyFfanPageConfigs.text_my_like)

    def isLoginStatus(self):
        try:
            nick_name_tv = API().find_view_by_resourceID_Until_android(driver=self.driver,logger=self.logger,resource_id=MyFfanPageConfigs.resource_id_txt_user_nick_name_tv)
            return True
        except TimeoutException as e:
            return False

if __name__ == '__main__':
    pass;
