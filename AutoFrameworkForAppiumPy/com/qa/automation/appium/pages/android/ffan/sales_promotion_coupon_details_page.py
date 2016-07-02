# -*- coding: utf-8 -*-

import os,sys

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from time import sleep
import unittest
from com.qa.automation.appium.configs.driver_configs import *
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page_configs import *
from com.qa.automation.appium.api.api import *
from com.qa.automation.appium.pages.android.common.super_page import *

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



class SalesPromotionCouponDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : "优惠券" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger, resource_id = SalesPromotionCouponDetailsPageConfigs.resource_id_tv_coupon_details_tv, seconds = 10)

    def clickOnFreeOfChargeBtn(self):
        '''
            usage : Click on "免费领取" button.
        '''
        #API().click_view_by_resourceID(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=SalesPromotionCouponDetailsPageConfigs) 
        webview = API().find_view_by_class_name_both(driver=self.driver, logger=self.logger,
                                                     className="android.webkit.WebView")
        webview_1 = webview.find_element_by_android_uiautomator("new UiSelector().className(android.webkit.WebView)")
        textview = webview_1.find_element_by_accessibility_id(SalesPromotionCouponDetailsPageConfigs.text_receive_free_button)
        textview.click()


if __name__ == '__main__':
    pass;