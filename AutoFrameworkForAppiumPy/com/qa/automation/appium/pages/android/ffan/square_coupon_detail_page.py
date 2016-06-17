# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.pages.android.ffan.square_coupon_detail_page_configs import SquareCouponDetailPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


'''
    usage : 广场模块，劵详情
'''
class SquareCouponDetailPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SquareCouponDetailPage, self).__init__(testcase = testcase , driver = driver,logger = logger);

   
    def validSelf(self):
        #API().assert_view_by_xpath_android(testcase = self.testcase, driver = self.driver, logger = self.logger, xpath = SquareCouponDetailPageConfigs.xpath_free_take,seconds=20)
        API().assert_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger, text=SquareCouponDetailPageConfigs.text_coupon_detail)
    '''
        usage : 点击免费领取
    '''
    def clickOnFreeTake(self):
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.driver, xpath = SquareCouponDetailPageConfigs.xpath_free_take,seconds=20) 
    
if __name__ == '__main__':
    pass;